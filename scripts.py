import requests

def get_rxnormid_from_name(Name):

    result = requests.get(f'https://rxnav.nlm.nih.gov/REST/rxcui.json?name={Name}&search=0').json()
    if 'rxnormId' in result:
        return result['rxnormId']
    else:
        return None
        
        
def get_rxnormid(NDC):

    result = requests.get(f'https://rxnav.nlm.nih.gov/REST/rxcui.json?idtype=NDC&id={NDC}&allsrc=1').json()['idGroup']
    if 'rxnormId' in result:
        return result['rxnormId']
    else:
        return None

def get_rxterms(RxNorm):

    result = requests.get(f'https://rxnav.nlm.nih.gov/REST/RxTerms/rxcui/{RxNorm}/allinfo.json').json()
    if 'rxtermsProperties' in result:
        return result['rxtermsProperties']
    else:
        return None
        

def get_rxname(RxNorm):

    result = requests.get(f'https://rxnav.nlm.nih.gov/REST/rxcui/{RxNorm}.json').json()
    if 'idGroup' in result:
        return result ['idGroup']
    else:
        return None
        
 
 def get_ingred(RxNorm):

    result = requests.get(f'https://rxnav.nlm.nih.gov/REST/rxcui/{RxNorm}/related.json?tty=IN').json()
    if 'relatedGroup' in result:
        return result['relatedGroup']['conceptGroup'][0]['conceptProperties'][0]['name']
    else:
        return None                      
