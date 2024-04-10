from .constants import ENET_URL


def extract_substring(start, end, string):
    return string.split(start)[-1].split(end)[0]


def get_enet_download_url(numSequencia, numVersao, numProtocolo, descTipo):
    return ENET_URL + f"frmDownloadDocumento.aspx?Tela=ext&numSequencia={numSequencia}&numVersao={numVersao}&numProtocolo={numProtocolo}-79&descTipo={descTipo}&CodigoInstituicao=1"

def parse_stock_amount(reports):
    dict_ = reports.to_dict()

    for k in dict_[1]:
        try:
            dict_[1][k] = int(dict_[1][k].replace(".",""))
        except:
            pass
    
    return {
        "ref_date": dict_[1][0],
        "capital_integralizado_on": dict_[1][2],
        "capital_integralizado_pn": dict_[1][3],
        "capital_integralizado_total": dict_[1][4],
        "tesouraria_on": dict_[1][6],
        "tesouraria_pn": dict_[1][7],
        "tesouraria_total": dict_[1][8]
    }