import rdflib
import requests
import json

from Metrics.metric import metric

def existingVocab(g_onto, liste_map, g_map, raw_data, g_link) :
    set_URIs = set()
    result = metric()
    result['name'] = "Use of existing vocabulary"
    nbPossible = 0
    points = 0
    for s, p, o in g_map.triples((None, None, None)) :
        if isinstance(s, rdflib.term.URIRef) :
            deb = s.split('$')[0]
            if str(s) == deb :
                set_URIs.add(s)
        if isinstance(p, rdflib.term.URIRef) :
            if p == rdflib.term.URIRef('a') :
                p = rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
            deb = p.split('$')[0]
            if str(p) == deb :
                set_URIs.add(p)
        if isinstance(o, rdflib.term.URIRef) :
            deb = o.split('$')[0]
            if str(o) == deb :
                set_URIs.add(o)
    for elt in set_URIs :
        nbPossible = nbPossible + 1
        lien = 'https://lov.linkeddata.es/dataset/lov/api/v2/term/search?q=' + elt + '&type=class'
        request = requests.get(lien)
        json_data = json.loads(request.text)
        if json_data["total_results"] != 0 :
            points = points + 1
        else :
            result['feedbacks'].append(str(elt) + " is not referenced in LOV.")
    if nbPossible == 0 :
        result['score'] = 1
    else :
        result['score'] =  points/nbPossible
    return result