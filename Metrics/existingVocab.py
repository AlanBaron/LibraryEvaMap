from Metrics import Metric
from EvaMap import EvaMap

import rdflib
import requests
import json

class existingVocab(Metric) :

    def __init__(self, nom = "Use of existing vocabulary", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def existingVocab(self) :
        set_URIs = set()
        nbPossible = 0
        points = 0
        for s, p, o in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(s, rdflib.term.URIRef) :
                deb = s.split('$')[0]
                if str(s) == deb :
                    set_URIs.add(s)
            if isinstance(p, rdflib.term.URIRef) :
                if p == rdflib.term.URIRef('a') :
                    p = rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
                deb = p.split('$')[0]
                if str(p) == deb :
                    set_URIs.add(p)
            if isinstance(o, rdflib.term.URIRef) :
                deb = o.split('$')[0]
                if str(o) == deb :
                    set_URIs.add(o)
        for elt in set_URIs :
            nbPossible = nbPossible + 1
            lien = 'https://lov.linkeddata.es/dataset/lov/api/v2/term/search?q=' + elt + '&type=class'
            request = requests.get(lien)
            json_data = json.loads(request.text)
            if json_data["total_results"] != 0 :
                points = points + 1
            else :
                self.feedback.append(elt + " is not referenced in LOV.")
        if nbPossible == 0 :
            return 1
        else :
            return points/nbPossible