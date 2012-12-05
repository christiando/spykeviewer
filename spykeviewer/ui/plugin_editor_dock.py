import os
import re
from PyQt4.QtGui import (QDockWidget, QWidget, QFileDialog, QGridLayout,
                         QMessageBox, QFont, QTabWidget, QTextCursor,
                         QDesktopServices)
from PyQt4.QtCore import Qt, pyqtSignal, SIGNAL

from spyderlib.widgets.sourcecode import codeeditor
from spyderlib.widgets.editor import ThreadManager
from spyderlib.utils.module_completion import moduleCompletion
from spyderlib.utils.dochelpers import getsignaturesfromtext


class PluginEditorDock(QDockWidget):
    """ A dock for editing plugins.
    """

    template_code = \
"""from spykeutils.plugin import analysis_plugin, gui_data

class SamplePlugin(analysis_plugin.AnalysisPlugin):
    def get_name(self):
        return 'New plugin'

    def start(self, current, selections):
        print 'Plugin started.'
"""

    plugin_saved = pyqtSignal(str)

    def __init__(self, title='Plugin Editor', default_path=None, parent=None):
        QDockWidget.__init__(self, title, parent)
        self.setupUi()

        self.thread_manager = ThreadManager(self)
        self.rope_project = codeeditor.get_rope_project()
        data_path = QDesktopServices.storageLocation(
            QDesktopServices.DataLocation)
        self.default_path = default_path or os.getcwd()
        self.rope_temp_path = os.path.join(data_path, '.temp')

    def set_default_path(self, path):
        self.default_path = path

    def populate_groups(self):
        self.filterGroupComboBox.clear()
        self.filterGroupComboBox.addItem('')
        for g in sorted(self.groups[self.filterTypeComboBox.currentText()]):
            self.filterGroupComboBox.addItem(g)

    def setupUi(self):
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_file)

        self.content_widget = QWidget()
        layout = QGridLayout(self.content_widget)
        layout.addWidget(self.tabs)

        self.setWidget(self.content_widget)

    def _setup_editor(self):
        font = QFont('Some font that does not exist')
        font.setStyleHint(font.TypeWriter, font.PreferDefault)
        editor = codeeditor.CodeEditor(self)
        editor.setup_editor(linenumbers=True, language='py',
            scrollflagarea=False, codecompletion_enter=True,
            tab_mode=False, edge_line=False, font=font,
            codecompletion_auto=True, go_to_definition=True,
            codecompletion_single=True, calltips=True)
        editor.setCursor(Qt.IBeamCursor)
        editor.horizontalScrollBar().setCursor(Qt.ArrowCursor)
        editor.verticalScrollBar().setCursor(Qt.ArrowCursor)
        return editor

    def trigger_code_completion(self, automatic):
        editor = self.tabs.currentWidget()
        source_code = unicode(editor.toPlainText())
        offset = editor.get_position('cursor')
        text = editor.get_text('sol', 'cursor')

        if text.startswith('import '):
            comp_list = moduleCompletion(text)
            words = text.split(' ')
            if ',' in words[-1]:
                words = words[-1].split(',')
            if comp_list:
                editor.show_completion_list(comp_list,
                    completion_text=words[-1],
                    automatic=automatic)
            return
        elif text.startswith('from '):
            comp_list = moduleCompletion(text)
            words = text.split(' ')
            if '(' in words[-1]:
                words = words[:-2] + words[-1].split('(')
            if ',' in words[-1]:
                words = words[:-2] + words[-1].split(',')
            editor.show_completion_list(comp_list,
                completion_text=words[-1],
                automatic=automatic)
            return
        else:
            print editor.file_name or self.rope_temp_path
            textlist = self.rope_project.get_completion_list(source_code,
                offset, editor.file_name or self.rope_temp_path)
            if textlist:
                completion_text = re.split(r"[^a-zA-Z0-9_]", text)[-1]
                if text.lstrip().startswith('#') and text.endswith('.'):
                    return
                else:
                    editor.show_completion_list(textlist, completion_text,
                        automatic)
                return

    def trigger_calltip(self, position, auto=True):
        editor = self.tabs.currentWidget()
        source_code = unicode(editor.toPlainText())
        offset = position

        textlist = self.rope_project.get_calltip_text(source_code, offset,
            editor.file_name or self.rope_temp_path)
        if not textlist:
            return
        obj_fullname = ''
        signatures = []
        cts, doc_text = textlist
        cts = cts.replace('.__init__', '')
        parpos = cts.find('(')
        if parpos:
            obj_fullname = cts[:parpos]
            obj_name = obj_fullname.split('.')[-1]
            cts = cts.replace(obj_fullname, obj_name)
            signatures = [cts]
            if '()' in cts:
                # Either inspected object has no argument, or it's
                # a builtin or an extension -- in this last case
                # the following attempt may succeed:
                signatures = getsignaturesfromtext(doc_text, obj_name)
        if not obj_fullname:
            obj_fullname = codeeditor.get_primary_at(source_code, offset)
        if obj_fullname and not obj_fullname.startswith('self.') and doc_text:
            if signatures:
                signature = signatures[0]
                module = obj_fullname.split('.')[0]
                note = '\n    Function of %s module\n\n' % module
                text = signature + note + doc_text
            else:
                text = doc_text
            editor.show_calltip(obj_fullname, text,
                at_position=position)

    def go_to_definition(self, position):
        """Go to definition"""
        editor = self.tabs.currentWidget()
        source_code = unicode(editor.toPlainText())
        offset = position
        fname, lineno = self.rope_project.get_definition_location(source_code,
            offset, editor.file_name or self.rope_temp_path)
        self.show_position(fname, lineno)

    def show_position(self, file_name, line):
        if not file_name:
            return
        self.add_file(file_name)

        if line is None:
            return
        editor = self.tabs.currentWidget()
        cursor = editor.textCursor()
        cursor.setPosition(0,QTextCursor.MoveAnchor)
        cursor.movePosition(QTextCursor.Down, QTextCursor.MoveAnchor,line-1)
        editor.setTextCursor(cursor)
        editor.raise_()
        editor.setFocus()

    def _finalize_new_editor(self, editor, tab_name):
        editor.file_was_changed = False
        editor.textChanged.connect(lambda: self.file_changed(editor))
        #editor.trigger_code_completion.connect(self.trigger_code_completion)
        self.connect(editor, SIGNAL('trigger_code_completion(bool)'),
            self.trigger_code_completion)
        self.connect(editor, SIGNAL('trigger_calltip(int)'),
            self.trigger_calltip)
        self.connect(editor, SIGNAL("go_to_definition(int)"),
            self.go_to_definition)

        self.tabs.addTab(editor, tab_name)
        self.tabs.setCurrentWidget(editor)

        self.setVisible(True)
        self.raise_()

    def new_file(self):
        editor = self._setup_editor()
        editor.file_name = None
        editor.set_text(self.template_code)
        self._finalize_new_editor(editor, '*New Plugin')

    def add_file(self, file_name):
        if file_name and not file_name.endswith('py'):
            QMessageBox.warning(self, 'Cannot load file',
                'Only Python files are supported for editing')
            return

        for i in xrange(self.tabs.count()):
            if file_name == self.tabs.widget(i).file_name:
                self.tabs.setCurrentIndex(i)
                return

        editor = self._setup_editor()
        editor.file_name = file_name
        editor.set_text_from_file(file_name)
        tab_name = os.path.split(file_name.decode('utf-8'))[1]
        self._finalize_new_editor(editor, tab_name)

    def close_file(self, tab_index):
        if self.tabs.widget(tab_index).file_was_changed:
            fname = os.path.split(self.tabs.widget(tab_index).file_name)[1]
            if not fname:
                fname = 'New Plugin'
            ans = QMessageBox.question(self, 'File was changed',
                'Do you want to save "%s" before closing?' % fname,
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if ans == QMessageBox.Yes:
                return self.save_file(self.tabs.widget(tab_index), False)
            elif ans == QMessageBox.Cancel:
                return False
        self.tabs.removeTab(tab_index)
        return True

    def closeEvent(self, event):
        if not self.close_all():
            event.ignore()
        else:
            event.accept()

    def close_all(self):
        while self.tabs.count():
            if not self.close_file(0):
                return False
        return True

    def file_changed(self, editor):
        editor.file_was_changed = True

        if not editor.file_name:
            fname = 'New Plugin'
        else:
            fname = os.path.split(editor.file_name)[1]

        text = '*' + fname

        self.tabs.setTabText(self.tabs.indexOf(editor), text)

    def code(self):
        return [self.tabs.currentWidget().get_text_line(l)
                for l in xrange(self.tabs.currentWidget().get_line_count())]


    def code_has_errors(self):
        code = '\n'.join(self.code()).encode('UTF-8')
        try:
            compile(code, '<filter>', 'exec')
        except SyntaxError as e:
            return e.msg + ' (Line %d)' % (e.lineno)
        return None

    def save_file(self, editor, force_dialog):
        if not editor:
            return

        if force_dialog or not editor.file_name:
            d = QFileDialog(self, 'Choose where to save plugin',
                self.tabs.currentWidget().file_name or self.default_path)
            d.setAcceptMode(QFileDialog.AcceptSave)
            d.setNameFilter("Python files (*.py)")
            d.setDefaultSuffix('py')
            if d.exec_():
                file_name = unicode(d.selectedFiles()[0])
            else:
                return False
        else:
            file_name = editor.file_name

        err = self.code_has_errors()
        if err:
            QMessageBox.critical(self, 'Error saving plugin',
                'Compile error:\n' + err)
            return False

        try:
            f = open(file_name, 'w')
            f.write('\n'.join(self.code()).encode('UTF-8'))
            f.close()
        except IOError, e:
            QMessageBox.critical(self, 'Error saving plugin',
                str(e))
            return False

        editor.file_name = file_name
        editor.file_was_changed = False
        fname = os.path.split(editor.file_name)[1]
        self.tabs.setTabText(self.tabs.indexOf(editor), fname)
        self.plugin_saved.emit(editor.file_name)
        return True

    def save_current(self, force_dialog=False):
        editor = self.tabs.currentWidget()
        self.save_file(editor, force_dialog)
