from Metrics import Metric
from EvaMap import EvaMap

import rdflib
import requests

class localLink(Metric) :

    def __init__(self, nom = "Local link (availability of)", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def localLink(self) : #Fait
        points = 0
        nbPossible = 0
        set_URIs = set()
        for s, _, _ in EvaMap.g_map.triples((None, None, None)) :
            set_URIs.add(s)
        for elt in set_URIs :
            deb = elt.split('$')[0]
            fin = elt.split('$(')[1].split(')')[0]
            if elt != deb :
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