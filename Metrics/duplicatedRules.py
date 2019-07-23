from Metrics.metric import metric

def duplicatedRules(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Duplicated rules"
    result['feedback'].append(str(len(liste_map) - len(g_map)) + " rules are duplicated.")
    result['score'] = len(g_map)/len(liste_map) #Propriété de rdflib
    return result

