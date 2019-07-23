import rdflib
import requests

from Metrics.metric import metric

def externalLink(g_onto, liste_map, g_map, raw_data, g_link) : #Fonctionnel
    points = 0
    nbPossible = 0
    result = metric()
    result['name'] = "Use of external link"
    set_URIs = set()
    for _, p, o in g_map.triples((None, None, None)) :
        if isinstance(p, rdflib.term.URIRef) :
            set_URIs.add(p)
        if isinstance(o, rdflib.term.URIRef) :
            set_URIs.add(o)
    for elt in set_URIs :
        deb = elt.split('$')[0]
        fin = ""
        try :
            fin = elt.split('$(')[1].split(')')[0]
        except :
            pass
        if str(elt) != str(deb) :
            for elements in raw_data :
                link = deb + elements['fields'][fin]
                nbPossible = nbPossible + 1
                a = requests.get(link)
                try :
                    a.raise_for_status()
                except:
                    points = points + 1
    if nbPossible == 0 :
        result['score'] = 1
    else :
        result['score'] = 1-points/nbPossible
    return result