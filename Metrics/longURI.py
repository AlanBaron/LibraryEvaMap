import rdflib
import requests

from Metrics.metric import metric

def longURI(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Long URIs"
    nbPossible = 0
    points = 0
    for s, p, o in g_map.triples((None, None, None)) :
        if isinstance(s, rdflib.term.URIRef) :
            nbPossible = nbPossible + 1
            if len(s) >= 80 :
                points = points + 1
                result['feedbacks'].append(str(s) + "is more than 79 characters")
        if isinstance(p, rdflib.term.URIRef) :
            nbPossible = nbPossible + 1
            if len(p) >= 80 :
                points = points + 1
                result['feedbacks'].append(str(p) + "is more than 79 characters")

        if isinstance(o, rdflib.term.URIRef) :
            nbPossible = nbPossible + 1
            if len(o) >= 80 :
                points = points + 1
                result['feedbacks'].append(str(o) + "is more than 79 characters")

    if nbPossible == 0:
        result['score'] = 1
    else :
        result['score'] = 1-points/nbPossible
    return result