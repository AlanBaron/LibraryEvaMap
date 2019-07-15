from Metrics import Metric
from EvaMap import EvaMap

import rdflib
import re

class verticalCoverage(Metric) :

    def __init__(self, nom = "Vertical Coverage", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def verticalCoverage(self) : #Fait ------------------------------------------------------
        set_dollarVal = set()
        correspondance = 0
        regexp = re.compile('\(([^)]+)')
        for s, _, o in EvaMap.g_map.triples((None, None, None)) :
            if regexp.search(str(s)) is not None:
                set_dollarVal.add(re.search('\(([^)]+)', str(s)).group(1))
            if regexp.search(str(o)) is not None:
                set_dollarVal.add(re.search('\(([^)]+)', str(o)).group(1))
        if len(EvaMap.raw_data[0]['fields']) == 0 :
            return 1
        else :
            return len(set_dollarVal)/len(EvaMap.raw_data[0]['fields'])