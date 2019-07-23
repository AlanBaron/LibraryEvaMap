import rdflib
import requests

from Metrics.metric import metric

def localLinks(g_onto, liste_map, g_map, raw_data, g_link) : #Retrourne en quelque sorte le nombre d'îlots. Opérationnel --------------------------------------------------------------------
    liste_value = []
    result = metric()
    result['name'] = "Use of one global mapping"
    result['score'] = 0
    i = 1
    val_S = 0
    val_O = 0
    for s, _, o in g_map.triples((None, None, None)) :
        index_S = 0
        index_O = 0
        parc_S = False
        parc_O = False
        for elt in liste_value :
            if s in elt :
                val_S = elt[1]
                parc_S = True
                index_S = liste_value.index(elt)
            if o in elt :
                val_O = elt[1]
                parc_O = True
                index_S = liste_value.index(elt)
            if parc_S and parc_O :
                if val_S < val_O :
                    liste_value[index_O][1] = val_S
                    liste_value = localLinkNewCalc(liste_value, o, g_link)
                elif val_S > val_O :
                    liste_value[index_S][1] = val_O
                    liste_value = localLinkNewCalc(liste_value, s, val_O, g_link)
                break
        if parc_S and not parc_O :
            liste_value.append([o, val_S])
        elif parc_O and not parc_S :
            liste_value.append([s, val_O])
        elif not parc_O and not parc_S :
            liste_value.append([s, i])
            liste_value.append([o, i])
            i = i + 1
    nb = []
    for elt in liste_value :
        if elt[1] not in nb :
            nb.append(elt[1])
    if nb:
        result['score'] = 1/len(nb)
    return result

def localLinkNewCalc(liste, ref, value, g_link) : #Utilisé pour la méthode précédente uniquement
    for _, _, o in g_link.triples((ref, None, None)) :
        for elt in liste :
            if o in elt :
                if elt[1] > value :
                   elt[1] = value
                   localLinkNewCalc(liste, o, value, g_link)
    for s, _, _ in g_link.triples((None, None, ref)) :
        for elt in liste :
            if s in elt :
                if elt[1] > value :
                   elt[1] = value
                   localLinkNewCalc(liste, s, value, g_link)
    return liste