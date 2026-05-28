from sapdi.sap_session import SAPDISession

_sap_instance = None

def get_sap_session():
    global _sap_instance

    if _sap_instance is None:
        _sap_instance = SAPDISession()
        _sap_instance.login()

    return _sap_instance