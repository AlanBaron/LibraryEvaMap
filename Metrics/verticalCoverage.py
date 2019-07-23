import rdflib
import requests
import re

from Metrics.metric import metric

def verticalCoverage(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Data coverage"
    result['score'] = 1
    set_dollarVal = set()
    correspondance = 0
    regexp = re.compile('\(([^)]+)')
    for s, _, o in g_map.triples((None, None, None)) :
        if regexp.search(str(s)) is not None:
            set_dollarVal.add(re.search('\(([^)]+)', str(s)).group(1))
        if regexp.search(str(o)) is not None:
            set_dollarVal.add(re.search('\(([^)]+)', str(o)).group(1))
        if raw_data and len(raw_data[0]['fields']) > 0:
            result['score'] = len(set_dollarVal)/len(raw_data[0]['fields'])
    return result