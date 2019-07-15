from Metrics import Metric
from EvaMap import EvaMap

import rdflib
import requests

class externalLink(Metric) :

    def __init__(self, nom = "External Link", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def externalLink(self) : #Fonctionnel
        points = 0
        nbPossible = 0
        set_URIs = set()
        for _, p, o in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(p, rdflib.term.URIRef) :
                set_URIs.add(p)
            if isinstance(o, rdflib.term.URIRef) :
                set_URIs.add(o)
        for elt in set_URIs :
            deb = elt.split('$')[0]
            fin = ""
            try :
                fin = elt.split('$(')[1].split(')')[0]
            except :
                pass
            if str(elt) != str(deb) :
                for elements in EvaMap.raw_data :
                    link = deb + elements['fields'][fin]
                    nbPossible = nbPossible + 1
                    a = requests.get(link)
                    try :
                        a.raise_for_status()
                    except:
                        points = points + 1
        if nbPossible == 0 :
            return 1
        else :
            return 1-points/nbPossible