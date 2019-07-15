from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class longTerm(Metric) :

    def __init__(self, nom = "Long term URIs", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def longTerm(self) : #Complété, corrigé et fonctionnel. Revoir le return ? -----------------------------------------------------
        nbPossible = 0
        points = 0
        set_URIs = set()
        for s, _, _ in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(s, rdflib.term.URIRef) :
                set_URIs.add(s)
        for elt in set_URIs :
            nbPossible = nbPossible + 1
            splitted_elt = elt.split('/')
            for elements in splitted_elt :
                try :
                    if int(elements) > 1990 and int(elements) < 2050 :
                        points = points + 1
                    else :
                        self.feedback.append(elements + "should contain a date.")
                except ValueError :
                    pass
        if nbPossible == 0 :
            return 1
        else :
            return points/nbPossible