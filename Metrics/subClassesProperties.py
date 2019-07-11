from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class subClassesProperties(Metric) :

    def __init__(self, nom = "Sub Classes and Properties", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def Consistency_subClassesProperties(self) : #Même remarque que la suivante. Fonctionne ----------------------------
        set_SO = set()
        set_P = set()
        points = 0
        nbPossible = 0
        for s, p, o in EvaMap.g_map.triples((None, None, None)) :
            set_SO.add(s)
            set_SO.add(o)
            set_P.add(p)
        for subobj in set_SO :
            for _, _, o2 in EvaMap.g_onto.triples((None, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf'), subobj)) :
                if not isinstance(o2, rdflib.term.BNode) :
                    nbPossible = nbPossible + 1
                if (None, None, o2) in EvaMap.g_map and not isinstance(o2, rdflib.term.BNode):
                    points = points + 1
                elif (o2, None, None) in EvaMap.g_map and not isinstance(o2, rdflib.term.BNode):
                    points = points + 1
                else :
                    self.feedback.append(o2 + "is missing.")
        for pred in set_P :
            for _, _, o3 in EvaMap.g_onto.triples((None, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subPropertyOf'), pred)) :
                if not isinstance(o3, rdflib.term.BNode) :
                    nbPossible = nbPossible + 1
                if (None, o3, None) in EvaMap.g_map and not isinstance(o3, rdflib.term.BNode) :
                    points = points + 1
        if nbPossible == 0 :
            return 1
        else :
            return points/nbPossible