#########################################################
# Required classes defined in common_classes.kv file #
#########################################################

from kivy.uix.textinput import TextInput
import re

class PatientIDTextInput(TextInput):

    pat = re.compile('[^A-Za-z0-9_]')

    def __init__(self, **kwargs):
        super(PatientIDTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>=12:
            return (False)
        else:
            return(True)

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=12:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(PatientIDTextInput, self).insert_text(s, from_undo=from_undo)















class UsernameTextInput(TextInput):

    pat = re.compile('[^A-Za-z0-9_]')

    def __init__(self, **kwargs):
        super(UsernameTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>=12:
            return (False)
        else:
            return(True)

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=12:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(UsernameTextInput, self).insert_text(s, from_undo=from_undo)

class SupportTextInput(TextInput):

    def __init__(self, **kwargs):
        super(SupportTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>=1200:
            return (False)
        else:
            return(True)

    def on_focus(self, instance, value):
        if (value and self.text=="Enter your message..." and self.password==False):
            self.text = ""
        elif ((not value) and self.text==""):
            self.text = "Enter your message..."

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=1200:
            s = ''
        else:
            s = substring
        return super(SupportTextInput, self).insert_text(s, from_undo=from_undo)

class EmailTextInput(TextInput):

    pat = re.compile('\s*')

    def __init__(self, **kwargs):
        super(EmailTextInput, self).__init__(**kwargs)

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        return super(EmailTextInput, self).insert_text(s, from_undo=from_undo)

class ConfirmationTextInput(TextInput):

    pat = re.compile('[^0-9_]')

    def __init__(self, **kwargs):
        super(ConfirmationTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>4:
            return (False)
        else:
            return(True)

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=4:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(ConfirmationTextInput, self).insert_text(s, from_undo=from_undo)

class CardNumberTextInput(TextInput):

    pat = re.compile('[^0-9_]')

    def __init__(self, **kwargs):
        super(CardNumberTextInput, self).__init__(**kwargs)

    def on_focus(self, instance, value):

        if (value and self.text=="XXXX-XXXX-XXXX-XXXX" and self.password==False):
            self.text = ""
        elif ((not value) and self.text==""):
            self.text = "XXXX-XXXX-XXXX-XXXX"

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=19:
            s=''
        elif len(self.text)==4:
            s=' '
        elif len(self.text)==9:
            s=' '
        elif len(self.text)==14:
            s=' '
        else:
            # pat1 = self.pat
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CardNumberTextInput, self).insert_text(s, from_undo=from_undo)

class CardExpireTextInput(TextInput):

    pat = re.compile('[^0-9_]')

    def __init__(self, **kwargs):
        super(CardExpireTextInput, self).__init__(**kwargs)

    def on_focus(self, instance, value):

        if (value and self.text=="MM/YY" and self.password==False):
            self.text = ""
        elif ((not value) and self.text==""):
            self.text = "MM/YY"

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=5:
            s=''
        elif len(self.text)==2:
            s='/'
        else:
            # pat1 = self.pat
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CardExpireTextInput, self).insert_text(s, from_undo=from_undo)

class CVVTextInput(TextInput):

    pat = re.compile('[^0-9_]')

    def __init__(self, **kwargs):
        super(CVVTextInput, self).__init__(**kwargs)

    def on_focus(self, instance, value):

        if (value and self.text=="***" and self.password==False):
            self.text = ""
        elif ((not value) and self.text==""):
            self.text = "***"

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=3:
            s=''
        else:
            # pat1 = self.pat
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CVVTextInput, self).insert_text(s, from_undo=from_undo)

class CredentialsPasswordTextInput(TextInput):
    pat = re.compile('[^a-zA-Z0-9@*#!%^$]')

    def __init__(self, **kwargs):
        super(CredentialsPasswordTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>=32:
            return (False)
        else:
            return(True)

    def on_focus(self, instance, value):

        if (value and self.text=="Password" and self.password==False):
            self.password = True
            self.text = ""
        elif ((not value) and self.text==""):
            self.password = False
            self.text = "Password"

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=32:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CredentialsPasswordTextInput, self).insert_text(s, from_undo=from_undo)

class CredentialsNewPasswordTextInput(TextInput):
    pat = re.compile('[^a-zA-Z0-9@*#!%^$]')

    def __init__(self, **kwargs):
        super(CredentialsNewPasswordTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>=32:
            return (False)
        else:
            return(True)

    def on_focus(self, instance, value):

        if (value and self.text=="New password" and self.password==False):
            self.password = True
            self.text = ""
        elif ((not value) and self.text==""):
            self.password = False
            self.text = "New password"

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=32:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CredentialsNewPasswordTextInput, self).insert_text(s, from_undo=from_undo)

class CredentialsOldPasswordTextInput(TextInput):
    pat = re.compile('[^a-zA-Z0-9@*#!%^$]')

    def __init__(self, **kwargs):
        super(CredentialsOldPasswordTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>=32:
            return (False)
        else:
            return(True)

    def on_focus(self, instance, value):

        if (value and self.text=="Old password" and self.password==False):
            self.password = True
            self.text = ""
        elif ((not value) and self.text==""):
            self.password = False
            self.text = "Old password"

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=32:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CredentialsOldPasswordTextInput, self).insert_text(s, from_undo=from_undo)

class CredentialsRepeatPasswordTextInput(TextInput):
    pat = re.compile('[^a-zA-Z0-9@*#!%^$]')
    def __init__(self, **kwargs):
        super(CredentialsRepeatPasswordTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>=32:
            return (False)
        else:
            return(True)

    def on_focus(self, instance, value):
        if (value and self.text=="Repeat password" and self.password==False):
            self.password = True
            self.text = ""
        elif ((not value) and self.text==""):
            self.password = False
            self.text = "Repeat password"

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=32:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CredentialsRepeatPasswordTextInput, self).insert_text(s, from_undo=from_undo)

class CredentialsRepeatNewPasswordTextInput(TextInput):
    pat = re.compile('[^a-zA-Z0-9@*#!%^$]')
    def __init__(self, **kwargs):
        super(CredentialsRepeatNewPasswordTextInput, self).__init__(**kwargs)

    def ValidateTextInput(self, text, *_):
        if len(text)>=32:
            return (False)
        else:
            return(True)

    def on_focus(self, instance, value):
        if (value and self.text=="Repeat new password" and self.password==False):
            self.password = True
            self.text = ""
        elif ((not value) and self.text==""):
            self.password = False
            self.text = "Repeat new password"

    def insert_text(self, substring, from_undo=False):
        if len(self.text)>=32:
            s=''
        else:
            pat = self.pat
            s = re.sub(pat, '', substring)
        return super(CredentialsRepeatNewPasswordTextInput, self).insert_text(s, from_undo=from_undo)


class MenuIncreaseDecreaseLabel(TextInput):
    def __init__(self, **kwargs):
        super(MenuIncreaseDecreaseLabel, self).__init__(**kwargs)

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if len(self.text)>1:
            s = ''
        else:
            s = re.sub(pat, '', substring)
        return super(MenuIncreaseDecreaseLabel, self).insert_text(s, from_undo=from_undo)

    def on_touch_down(self, touch):
        if not (self.collide_point(touch.x,touch.y)):
            if (self.text == '') or (self.text == '0') or (self.text == '00'):
                self.text = '1'
        else:
            return super(MenuIncreaseDecreaseLabel, self).on_touch_down(touch)
