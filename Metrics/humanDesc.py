from Metrics.metric import metric

import rdflib

def humanDesc(g_onto, liste_map, g_map, raw_data, g_link) : #Revoir le return, opérationnel sinon -------------------------------------------------
    nbPossible = 0
    result = metric()
    result['score'] = 0
    result['name'] = "Usage of description of label"
    points = 0
    set_URIs = set()
    for s, _, _ in g_map.triples((None, None, None)) :
        if isinstance(s, rdflib.term.URIRef) :
            set_URIs.add(s)
    for elt in set_URIs:
        passe = False
        nbPossible = nbPossible + 1
        for s2, _, _ in g_link.triples((elt, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), None)) :
            passe = True
        for s2, _, _ in g_link.triples((elt, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#comment'), None)) :
            passe = True
        if passe :
            points = points + 1
        else :
            result['feedbacks'].append(str(elt) + " is not understandable, please add an rdfs:comment or rdfs:label. ")
    if nbPossible:
        result['score'] = points/(nbPossible)
    return result