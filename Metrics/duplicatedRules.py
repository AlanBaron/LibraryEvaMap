from EvaMap import EvaMap
from Metrics import Metric

class subClassesProperties(Metric) :

    def __init__(self, nom = "Duplicated Rule", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def duplicatedRules(self) :
        self.feedback.append(str(len(EvaMap.liste_map) - len(EvaMap.g_map)) + " rules are duplicated.")
        return len(EvaMap.g_map)/len(EvaMap.liste_map) #Propriété de rdflib

