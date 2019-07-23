import rdflib

from Metrics.metric import metric

def disjointWith(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Misuse of disjointWith"
    points = 0
    nbPossible = 0
    for s, _, o in g_map.triples((None, None, None)) :
        nbPossible = nbPossible + 1
        for _, _, o1 in g_onto.triples((s, rdflib.term.URIRef('https://www.w3.org/2002/07/owl#disjointWith'), None)) :
            if g_onto.triples((o, (rdflib.term.URIRef('a')|rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')), o1)) is not None :
                points = points + 1
                result['feedbacks'].append(str(o) + "is disjoint with" + s)
            else :
                for s1, _, _ in g_onto.triples((None, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf') ,o)):
                    if g_onto.triples((s1, (rdflib.term.URIRef('a')|rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')), o1)) is not None :
                        points = points + 1
                        result['feedbacks'].append(str(o) + "is disjoint with" + s)
        for _, _, o1 in g_onto.triples((o, rdflib.term.URIRef('https://www.w3.org/2002/07/owl#disjointWith'), None)) :
            if g_onto.triples((s, (rdflib.term.URIRef('a')|rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')), o1)) is not None :
                points = points + 1
                result['feedbacks'].append(str(o) + "is disjoint with" + s)
            else :
                for s1, _, _ in g_onto.triples((None, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf') ,s)):
                    if g_onto.triples((s1, (rdflib.term.URIRef('a')|rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')), o1)) is not None :
                        points = points + 1
                        result['feedbacks'].append(str(o) + "is disjoint with" + s)
    if nbPossible == 0 :
        result['score'] = 1
    else :
        result['score'] = 1-points/nbPossible
    return result