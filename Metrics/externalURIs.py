from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class externalURIs(Metric) :

    def __init__(self, nom = "Use of external URIs", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def Interlinking_externalURIs(self) : #Revoir le return, sinon complet
        points = 0
        nbPossible = 0
        for s, _, o in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(s, rdflib.term.URIRef) and isinstance(o, rdflib.term.URIRef) : #Donc on a un lien entre deux URIs
                nbPossible = nbPossible + 1
                if not (s, None, o) in EvaMap.g_onto : #Et si ça n'existe pas dans notre ontologie, alors on a créé un nouveau lien
                    points = points + 1
        if nbPossible == 0 :
            return 1
        else :
            return points/nbPossible