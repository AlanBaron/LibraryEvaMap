from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class subClassesProperties(Metric) :

    def __init__(self, nom = "Long URIs", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def Conciseness_longURI(self) :
        nbPossible = 0
        points = 0
        for s, p, o in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(s, rdflib.term.URIRef) :
                nbPossible = nbPossible + 1
                if len(s) >= 80 :
                    points = points + 1
                    self.feedback.append(s + "is more than 79 characters")
        if isinstance(p, rdflib.term.URIRef) :
                nbPossible = nbPossible + 1
                if len(p) >= 80 :
                    points = points + 1
                    self.feedback.append(p + "is more than 79 characters")

        if isinstance(o, rdflib.term.URIRef) :
                nbPossible = nbPossible + 1
                if len(o) >= 80 :
                    points = points + 1
                    self.feedback.append(o + "is more than 79 characters")

        if nbPossible == 0:
            return 1
        else :
            return 1-points/nbPossible