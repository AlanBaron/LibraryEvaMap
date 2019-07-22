#import sys
import os
import argparse
import rdflib
#import pyaml
import yaml
import re
from rdflib.graph import Graph
from pathlib import Path
#import urllib
from urllib.parse import urlparse
import requests
import json


class EvaMap :

    g_link = Graph()
    g_map = Graph()
    g_onto = Graph()
    liste_map = []
    final_list = []

    def __init__(self, onto, map, data):
        self.read_json(data) #From json
        self.read_yaml(map)  #From yaml
        self.read_rdf(onto)
        for triple in self.liste_map:
            nbTriples = nbTriples + 1
            self.g_link.add(triple)
            self.g_map.add(triple)
        weight = dict() #Intialiser par défaut tous les poids, avec les noms de toutes les dimensions.

    #Regarder comment bien lire les fichiers avec la webApp
    def read_json(self, file):
        if Path(file).suffix == '.json':
            self.raw_data = json.load(open(file))
        try :
            self.raw_data = self.raw_data["records"]
        except:
            pass

    def read_yaml(self, file):
        if (Path(file).suffix == '.yml') or (Path(file).suffix == '.yaml'):
            mapping = yaml.load(open(file), Loader=yaml.FullLoader)
            liste_map = self.yamlToTriples(mapping)

    def yamlToTriples(mapping):
        liste_map = []
        prefString = ""
        for name in mapping["mappings"]:
            for predicateobject in mapping["mappings"][name]["predicateobjects"]:
                # on transforme les préfixes, si il y en a. Sinon on passe
                try:
                    for prefix in mapping["prefixes"]:
                        prefString = str(prefix) + ':'
                        if re.search(prefString, predicateobject[1]) is not None:
                            predicateobject[1] = mapping["prefixes"][prefix] + (
                                predicateobject[1].split(prefString, 1)[1])
                        if re.search(prefString, predicateobject[0]) is not None:
                            predicateobject[0] = mapping["prefixes"][prefix] + (
                                predicateobject[0].split(prefString, 1)[1])
                except:
                    pass
                # On regarde si c'est un littéral ou une URI
                if len(predicateobject) == 2:
                    if re.search('(http://)|(https://)', predicateobject[1]) is not None:
                        liste_map.append([rdflib.term.URIRef(mapping["mappings"][name]["subject"]),
                                          rdflib.term.URIRef(predicateobject[0]),
                                          rdflib.term.URIRef(predicateobject[1])])
                    else:
                        liste_map.append([rdflib.term.URIRef(mapping["mappings"][name]["subject"]),
                                          rdflib.term.URIRef(predicateobject[0]),
                                          rdflib.term.Literal(predicateobject[1])])

                # taille de 3 = littéral
                elif len(predicateobject) == 3:
                    if len(predicateobject[2].split('~')) == 2:
                        if predicateobject[2].split('~')[1] == 'lang':
                            liste_map.append([rdflib.term.URIRef(mapping["mappings"][name]["subject"]),
                                              rdflib.term.URIRef(predicateobject[0]),
                                              rdflib.term.Literal(predicateobject[1],
                                                                  lang=predicateobject[2].split('~')[0])])
                        else:
                            liste_map.append([rdflib.term.URIRef(mapping["mappings"][name]["subject"]),
                                              rdflib.term.URIRef(predicateobject[0]),
                                              rdflib.term.Literal(predicateobject[1], datatype=predicateobject[2])])
                    else:
                        liste_map.append([rdflib.term.URIRef(mapping["mappings"][name]["subject"]),
                                          rdflib.term.URIRef(predicateobject[0]),
                                          rdflib.term.Literal(predicateobject[1], datatype=predicateobject[2])])
        # on relie les variables aux mappings correspondant, jusque là considérées comme des litérals
        for name in mapping["mappings"]:
            for triples in liste_map:
                if str(triples[2]) == name:
                    triples[2] = rdflib.term.URIRef(mapping["mappings"][name]["subject"])
        return liste_map

    def read_rdf(self, file):
        if Path(file).suffix == '.rdf':
            self.g_onto.parse(open(file))
            for s, p, o in self.g_onto.triples((None, None, None)):
                self.g_link.add((s, p, o))

    def set_weight(self, dict):
        i = 0
        for poids in self.liste :
            self.weight[i] = poids