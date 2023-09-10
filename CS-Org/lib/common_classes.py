#########################################################
# Required classes defined in common_classes.kv file #
#########################################################

from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooser
import re

class PatientIDTextInput(TextInput):

    pat = re.compile('[^A-Za-z0-9_]')

    def __init__(self, **kwargs):
        super(PatientIDTextInput, self).__init__(**kwargs)

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=12:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(PatientIDTextInput, self).insert_text(s, from_undo=from_undo)



class CTScanLevelWidthTextInput(TextInput):

    pat = re.compile('[^0-9_]')

    def __init__(self, **kwargs):
        super(CTScanLevelWidthTextInput, self).__init__(**kwargs)
        self.multiline = False
    

    def insert_text(self, substring, from_undo=False):
        print('inserting')
        if len(self.text)>=4:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CTScanLevelWidthTextInput, self).insert_text(s, from_undo=from_undo)


class CustomFileChooser(FileChooser):
    def __init__(self, **kwargs):
        super(CustomFileChooser, self).__init__(**kwargs)
        self.double_tap = False

    # This is important to prevent auto opening of folders, Further check may still be needed!
    def open_entry(self, entry):
        # print('open_entry is fired')
        # if len(self.selection)>0:print('Selection: {}'.format(self.selection[0]))
        # else: print('Selection is empty')

        if self.double_tap:
            self.double_tap = False
            return super().open_entry(entry)
        else:
            self.selection.clear()
            self.selection.append(entry.path)
            return None            

    def entry_touched(self, entry, touch):
        # print('entry_touched is fired')
        # if len(self.selection)>0:print('Selection: {}'.format(self.selection[0]))
        # else: print('Selection is empty')

        _dir = self.file_system.is_dir(entry.path)

        if touch.is_double_tap: self.double_tap = True
        else: self.double_tap = False

        return super().entry_touched(entry, touch)

    # def on_submit(self, selected, touch=None):
    #     return super().on_submit(selected, touch)