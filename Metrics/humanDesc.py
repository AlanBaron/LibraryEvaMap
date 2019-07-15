from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class humanDesc(Metric) :

    def __init__(self, nom = "Understandable URIs", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def humanDesc(self) : #Revoir le return, opérationnel sinon -------------------------------------------------
        nbPossible = 0
        points = 0
        set_URIs = set()
        for s, _, _ in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(s, rdflib.term.URIRef) :
                set_URIs.add(s)
        for elt in set_URIs :
            passe = False
            nbPossible = nbPossible + 1
            for s2, _, _ in EvaMap.g_link.triples((elt, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), None)) :
                passe = True
            for s2, _, _ in EvaMap.g_link.triples((elt, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#comment'), None)) :
                passe = True
            if passe :
                points = points + 1
            else :
                self.feedback.append(elt + " is not understandable, please add an rdfs:comment or rdfs:label. ")
        return points/(nbPossible)