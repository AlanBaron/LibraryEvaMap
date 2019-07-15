from Metrics import Metric
from EvaMap import EvaMap

import rdflib

class localLinks(Metric) :

    def __init__(self, nom = "Local links (existence of)", desc = " "):
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def localLinks(self) : #Retrourne en quelque sorte le nombre d'îlots. Opérationnel --------------------------------------------------------------------
        liste_value = []
        i = 1
        val_S = 0
        val_O = 0
        for s, _, o in EvaMap.g_map.triples((None, None, None)) :
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
                        liste_value = self.localLinkNewCalc(liste_value, o, val_S)
                    elif val_S > val_O :
                        liste_value[index_S][1] = val_O
                        liste_value = self.localLinkNewCalc(liste_value, s, val_O)
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
        return 1/len(nb)

    def localLinkNewCalc(self, liste, ref, value) : #Utilisé pour la méthode précédente uniquement
        for _, _, o in EvaMap.g_link.triples((ref, None, None)) :
            for elt in liste :
                if o in elt :
                    if elt[1] > value :
                       elt[1] = value
                       self.localLinkNewCalc(liste, o, value)
        for s, _, _ in EvaMap.g_link.triples((None, None, ref)) :
            for elt in liste :
                if s in elt :
                    if elt[1] > value :
                       elt[1] = value
                       self.localLinkNewCalc(liste, s, value)
        return liste