from Metrics import Metric
from EvaMap import EvaMap
from urllib.parse import urlparse
import re

import rdflib

class subClassesProperties(Metric) :

    def __init__(self, nom = "Human Readable", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc


    def HumanReadableURIs(self) : #Complet --------------------------------------------------------------------------------
        nbPossible = 0
        points = 0
        for s, p, o in EvaMap.g_map.triples((None, None, None)) :
            if isinstance(s, rdflib.term.URIRef) :
                nbPossible = nbPossible + 1
                str = urlparse(s)
                if str.fragment != '' :
                    str = str.fragment
                    if self.test_HumanReadable(str) :
                        points = points + 1
                else :
                    str = str.path
                    str = str.split("/")[-1]
                    if self.test_HumanReadable(str) :
                        points = points + 1
                if str.startswith('$') :
                    nbPossible = nbPossible - 1
                    points = points - 1
            if isinstance(p, rdflib.term.URIRef) and p != rdflib.term.URIRef('a'):
                nbPossible = nbPossible + 1
                str = urlparse(p)
                if str.fragment != '' :
                    str = str.fragment
                    if self.test_HumanReadable(str) :
                        points = points + 1
                else :
                    str = str.path
                    str = str.split("/")[-1]
                    if self.test_HumanReadable(str) :
                        points = points + 1
                if str.startswith('$') :
                    nbPossible = nbPossible - 1
                    points = points - 1
            if isinstance(o, rdflib.term.URIRef) :
                nbPossible = nbPossible + 1
                str = urlparse(o)
                if str.fragment != '' :
                    str = str.fragment
                    if self.test_HumanReadable(str) :
                        points = points + 1
                else :
                    str = str.path
                    str = str.split("/")[-1]
                    if self.test_HumanReadable(str) :
                        points = points + 1
                if str.startswith('$') :
                    nbPossible = nbPossible - 1
                    points = points - 1
        if nbPossible == 0 :
            return 1
        else :
            return 1-((nbPossible) - points)/(nbPossible)

    def test_HumanReadable(self, str) : #------------------------ Utilisé au dessus --------------------------------------------------
        if not str.startswith('$') :
            regexp = re.compile(r'[A-Z][A-Z][A-Z]') #Si on a une suite de 3 majuscules
            if regexp.search(str):
                self.feedback.append(str + "is not Human Readable (3 or more capital letters).")
                return False
            regexp = re.compile(r'[0-9]+[A-Za-z-_.]+[0-9]*$') #Si on a un string contenant un chiffre au milieu d'autre caractères
            if regexp.search(str):
                self.feedback.append(str + "is not Human Readable (number inside the string).")
                return False
            regexp = re.compile(r'[$+!*\'()]') #Si on a un caractère particulier qui ne devrait pas exister
            if regexp.search(str):
                self.feedback.append(str + "is not Human Readable (use of a special character).")
                return False
            if len(str) < 3 : #si la taille est inférieure à 3
                self.feedback.append(str + "is not Human Readable (Less than 3 characters).")
                return False
            if re.subn('[0-9]', '', str)[1] > 8 : #Si on a plus de 8 chiffres (date)*
                self.feedback.append(str + "is not Human Readable (more than 8 numbers).")
                return False
        return True