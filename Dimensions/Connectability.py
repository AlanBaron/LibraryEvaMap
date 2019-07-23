from Dimensions.Dimension import Dimension
from Metrics.sameAs import sameAs
from Metrics.externalURIs import externalURIs
from Metrics.localLinks import localLinks
from Metrics.existingVocab import existingVocab

class Connectability(Dimension) :

    def __init__(self, nom='Connectability', list_metrics=[existingVocab, sameAs, externalURIs, localLinks]):
        super().__init__(nom, list_metrics)