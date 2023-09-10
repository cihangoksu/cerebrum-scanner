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
    id_ProceedButtonContent = ObjectProperty(None)
    id_defaultpath = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(FileBrowsePopup, self).__init__(**kwargs)


class LoadingPopup(Popup):
    id_LoadingPopupContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(LoadingPopup, self).__init__(**kwargs)

class ConfirmationCodePopup(Popup):
    id_ConfirmationPopupContent = ObjectProperty(None)
    id_ResentOpacity = NumericProperty(0)
    id_CancelButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(ConfirmationCodePopup, self).__init__(**kwargs)

class ForgotPasswordPopup(Popup):
    id_ForgotPasswordPopupContent = ObjectProperty(None)
    id_CancelButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(ForgotPasswordPopup, self).__init__(**kwargs)

class CreditCardInfoPopup(Popup):
    def __init__(self, **kwargs):
        super(CreditCardInfoPopup, self).__init__(**kwargs)

class SetNewPasswordPopup(Popup):
    id_SetNewPasswordPopupContent = ObjectProperty(None)
    id_CancelButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(SetNewPasswordPopup, self).__init__(**kwargs)

class ModifyBillingInfoPopup(Popup):
    id_ModifyBilling_name = StringProperty("")
    id_ModifyBilling_email = StringProperty("")
    id_ModifyBilling_address = StringProperty("")
    id_ModifyBilling_country = StringProperty("")
    id_ModifyBilling_state = StringProperty("")
    id_ModifyBilling_city = StringProperty("")
    id_ModifyBilling_postal = StringProperty("")
    def __init__(self, **kwargs):
        super(ModifyBillingInfoPopup, self).__init__(**kwargs)

class SupportPopup(Popup):
    id_SupportPopupContent = ObjectProperty(None)
    id_CancelButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(SupportPopup, self).__init__(**kwargs)

class SendTranscriptionPopup(Popup):
    id_SendTranscriptionPopupContent = ObjectProperty(None)
    id_CancelButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(SendTranscriptionPopup, self).__init__(**kwargs)

class AreYouSureWImagePopup(Popup):
    id_AreYouSureWImagePopupTexture = ObjectProperty(None)
    id_AreYouSureWImagePopupContent = ObjectProperty(None)
    id_CancelButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(AreYouSureWImagePopup, self).__init__(**kwargs)

class AreYouSureWImagePreparePopup(Popup):
    id_AreYouSureWImagePreparePopupTexture = ObjectProperty(None)
    id_AreYouSureWImagePreparePopupContent = ObjectProperty(None)
    id_CancelButtonContent = ObjectProperty(None)
    id_ProceedButtonContent = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(AreYouSureWImagePreparePopup, self).__init__(**kwargs)
