from suds.client import Client

WSDL_URL = 'https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL'

def trm(date):
    """
    This function returns the Representative Market Rate for the Colombian peso (COP). If there is an error, it returns 0.
    """

    try:
        client = Client(WSDL_URL, location=WSDL_URL, faults=True)
        trm =  client.service.queryTCRM(date)
    except Exception as e:
        return 0

    return float(trm[4])