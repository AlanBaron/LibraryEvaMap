from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class equivalentClassesProperties(Metric) :

    def __init__(self, nom = "Equivalent classes and properties", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def equivalentClassesProperties(self) : #Ici on considère que si une classe equivalente est dans notre mapping, alors elle est correctement utilisée. Corrigé
        set_SO = set()
        set_P = set()
        points = 0
        nbPossible = 0
        for s, p, o in EvaMap.g_map.triples((None, None, None)) :
            set_SO.add(s)
            set_SO.add(o)
            set_P.add(p)
        for subobj in set_SO :
            for _, _, o2 in EvaMap.g_onto.triples((subobj, rdflib.term.URIRef('http://www.w3.org/2002/07/owl#equivalentClass'), None)) :
                if not isinstance(o2, rdflib.term.BNode) :
                    nbPossible = nbPossible + 1
                if (None, None, o2) in EvaMap.g_map and not isinstance(o2, rdflib.term.BNode):
                    points = points + 1
                elif (o2, None, None) in EvaMap.g_map and not isinstance(o2, rdflib.term.BNode):
                    points = points + 1
                else :
                    self.feedback.append(o2 + "is missing.")
        for pred in set_P :
            for _, _, o3 in EvaMap.g_onto.triples((pred, rdflib.term.URIRef('https://www.w3.org/2002/07/owl#equivalentProperty'), None)) :
                nbPossible = nbPossible + 1
                if (None, None, o3) in EvaMap.g_map and not isinstance(o3, rdflib.term.BNode) :
                    points = points + 1
                elif (o3, None, None) in EvaMap.g_map and not isinstance(o3, rdflib.term.BNode):
                    points = points + 1
                else :
                    self.feedback.append(o3 + "is missing.")

        if nbPossible == 0 :
            return 1
        else :
            return points/nbPossible