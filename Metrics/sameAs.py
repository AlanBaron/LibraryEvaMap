import rdflib
import requests

from Metrics.metric import metric

def sameAs(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Use of sameAs properties"
    nbPossible = 0
    points = 0
    set_URIs = set()
    for s, _, _ in g_map.triples((None, None, None)) :
        if isinstance(s, rdflib.term.URIRef) :
            set_URIs.add(s)
    for elt in set_URIs :
        nbPossible = nbPossible + 1
        for _, _, _  in g_map.triples((elt, rdflib.term.URIRef('http://www.w3.org/2002/07/owl#sameAs'), None)) :
            points = points + 1
    if nbPossible == 0 :
        result['score'] = 0
        result['feedbacks'].append("You should use some sameAs properties")
    else :
        result['score'] = points/(nbPossible)
    return result