#########################################################
# Popups
#########################################################
from kivy.uix.popup import Popup
from kivy.properties import (
    ObjectProperty, NumericProperty, ListProperty, StringProperty
)

class AllWellPopup(Popup):
    id_AllWellPopupContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(AllWellPopup, self).__init__(**kwargs)

class FeedbackPopup(Popup):
    id_FeedbackPopupContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(FeedbackPopup, self).__init__(**kwargs)

class WarningPopup(Popup):
    id_WarningPopupContent = ObjectProperty(None)
    id_WarningPopupImage = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(WarningPopup, self).__init__(**kwargs)

class AreYouSurePopup(Popup):
    id_AreYouSurePopupContent = ObjectProperty(None)
    id_CancelButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(AreYouSurePopup, self).__init__(**kwargs)

class FileBrowsePopup(Popup):
    id_FileBrowsePopupContent = ObjectProperty(None)
    id_CancelButtonContent = ObjectProperty(None)
    id_ConvertDicomButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    id_defaultpath = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(FileBrowsePopup, self).__init__(**kwargs)
    
    def on_touch_down(self, touch):
        # print('selected')
        return super().on_touch_down(touch)

class LoadingPopup(Popup):
    id_LoadingPopupContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(LoadingPopup, self).__init__(**kwargs)

