import rdflib
import requests

from Metrics.metric import metric

def longTerm(g_onto, liste_map, g_map, raw_data, g_link) : #Complété, corrigé et fonctionnel. Revoir le return ? -----------------------------------------------------
    nbPossible = 0
    result = metric()
    result['name'] = "Long term subject"
    points = 0
    set_URIs = set()
    for s, _, _ in g_map.triples((None, None, None)) :
        if isinstance(s, rdflib.term.URIRef) :
            set_URIs.add(s)
    for elt in set_URIs :
        nbPossible = nbPossible + 1
        splitted_elt = elt.split('/')
        for elements in splitted_elt:
            try :
                if int(elements) > 1990 and int(elements) < 2050 :
                    points = points + 1
                else :
                    result['feedbacks'].append(elements + "should contain a date.")
            except ValueError :
                pass
    if nbPossible == 0 :
        result['score'] = 1
    else :
        result['score'] = points/nbPossible
    return result