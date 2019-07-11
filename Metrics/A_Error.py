from Metrics import Metric
from EvaMap import EvaMap

import rdflib
import requests


class A_Error(Metric) :

    def __init__(self, nom = "Error", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = []
        self.description = desc

    def Error(self) : #Corrigé, opérationelle, et optimisé au mieux. Ne pas prendre en compte les URIs avec des $ ? (Copier coller le code plus bas, modifier conditionelle, et c'est bon)
        points = 0
        set_URIs = set()
        for s, p, o in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(s, rdflib.term.URIRef) :
                str1 = str(s)
                str2 = str(s)
                str1 = str1.split('$')[0].split('#')[0]
                if str1 == str2 :
                    str1 = str1.rsplit('/', 1)[0] + '/'
                set_URIs.add(str1)
            if isinstance(p, rdflib.term.URIRef) and p != rdflib.term.URIRef('a') :
                str1 = str(p)
                str2 = str(p)
                str1 = str1.split('$')[0].split('#')[0]
                if str1 == str2 :
                    str1 = str1.rsplit('/', 1)[0] + '/'
                set_URIs.add(str1)
            if isinstance(o, rdflib.term.URIRef) :
                str1 = str(o)
                str2 = str(o)
                str1 = str1.split('$')[0].split('#')[0]
                if str1 == str2 :
                    str1 = str1.rsplit('/', 1)[0] + '/'
                set_URIs.add(str1)
        nbPossible = len(set_URIs)
        for elt in set_URIs :
            a = requests.get(elt)
            try :
                a.raise_for_status()
            except:
                self.feedback.append(elt + "gives an Error")
                points = points + 1

        if nbPossible == 0 :
            self.score = 1
        else :
            self.score =  1-points/nbPossible