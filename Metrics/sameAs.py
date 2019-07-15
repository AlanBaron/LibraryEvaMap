from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class sameAs(Metric) :

    def __init__(self, nom = "sameAs property", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def sameAs(self) : #Corrigé, devrait être opérationnel. Ici, on regarde pour chaque URI si cette dernière à un owl:sameAs existant. --------------------------------------
        nbPossible = 0
        points = 0
        set_URIs = set()
        for s, _, _ in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(s, rdflib.term.URIRef) :
                set_URIs.add(s)
        for elt in set_URIs :
            nbPossible = nbPossible + 1
            for _, _, _  in EvaMap.g_map.triples((elt, rdflib.term.URIRef('http://www.w3.org/2002/07/owl#sameAs'), None)) :
                points = points + 1
        if nbPossible == 0 :
            return 0
        else :
            return points/(nbPossible)