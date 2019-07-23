import rdflib
import requests

from Metrics.metric import metric

def Error(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Availability error"
    points = 0
    set_URIs = set()
    for s, p, o in g_map.triples((None, None, None)) :
        if isinstance(s, rdflib.term.URIRef) :
            str1 = str(s)
            str2 = str(s)
            str1 = str1.split('$')[0].split('#')[0]
            if str1 == str2 :
                str1 = str1.rsplit('/', 1)[0] + '/'
            set_URIs.add(str1)
        if isinstance(p, rdflib.term.URIRef) and p != rdflib.term.URIRef('a') :
            str1 = str(p)
            str2 = str(p)
            str1 = str1.split('$')[0].split('#')[0]
            if str1 == str2 :
                str1 = str1.rsplit('/', 1)[0] + '/'
            set_URIs.add(str1)
        if isinstance(o, rdflib.term.URIRef) :
            str1 = str(o)
            str2 = str(o)
            str1 = str1.split('$')[0].split('#')[0]
            if str1 == str2 :
                str1 = str1.rsplit('/', 1)[0] + '/'
            set_URIs.add(str1)
    nbPossible = len(set_URIs)
    for elt in set_URIs :
        a = requests.get(elt)
        try :
            a.raise_for_status()
        except:
            result['feedbacks'].append(str(elt) + "gives an Error")
            points = points + 1

    if nbPossible == 0 :
        result['score'] = 1
    else :
        result['score'] = 1-points/nbPossible
    return result