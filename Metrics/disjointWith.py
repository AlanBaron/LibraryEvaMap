from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class disjointWith(Metric) :

    def __init__(self, nom = "Disjoint Classes", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def disjointWith(self) :
        points = 0
        nbPossible = 0
        for s, _, o in EvaMap.g_map.triples((None, None, None)) :
            nbPossible = nbPossible + 1
            for _, _, o1 in EvaMap.g_onto.triples((s, rdflib.term.URIRef('https://www.w3.org/2002/07/owl#disjointWith'), None)) :
                if EvaMap.g_onto.triples((o, (rdflib.term.URIRef('a')|rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')), o1)) is not None :
                    points = points + 1
                    self.feedback.append(o + "is disjoint with" + s)
                else :
                    for s1, _, _ in EvaMap.g_onto.triples((None, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf') ,o)):
                        if EvaMap.g_onto.triples((s1, (rdflib.term.URIRef('a')|rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')), o1)) is not None :
                            points = points + 1
                            self.feedback.append(o + "is disjoint with" + s)

            for _, _, o1 in EvaMap.g_onto.triples((o, rdflib.term.URIRef('https://www.w3.org/2002/07/owl#disjointWith'), None)) :
                if EvaMap.g_onto.triples((s, (rdflib.term.URIRef('a')|rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')), o1)) is not None :
                    points = points + 1
                    self.feedback.append(o + "is disjoint with" + s)
                else :
                    for s1, _, _ in EvaMap.g_onto.triples((None, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf') ,s)):
                        if EvaMap.g_onto.triples((s1, (rdflib.term.URIRef('a')|rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')), o1)) is not None :
                            points = points + 1
                            self.feedback.append(o + "is disjoint with" + s)

        if nbPossible == 0 :
            return 1
        else :
            return 1-points/nbPossible