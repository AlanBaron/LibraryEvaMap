import rdflib

from Metrics.metric import metric

def externalURIs(g_onto, liste_map, g_map, raw_data, g_link) : #Revoir le return, sinon complet
    points = 0
    nbPossible = 0
    result = metric()
    result['name'] = "Use of external URIs"
    for s, _, o in g_map.triples((None, None, None)) :
        if isinstance(s, rdflib.term.URIRef) and isinstance(o, rdflib.term.URIRef) : #Donc on a un lien entre deux URIs
            nbPossible = nbPossible + 1
            if not (s, None, o) in g_onto : #Et si ça n'existe pas dans notre ontologie, alors on a créé un nouveau lien
                points = points + 1
    if nbPossible == 0 :
        result['score'] = 1
    else :
        result['score'] = points/nbPossible
    return result