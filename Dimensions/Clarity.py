from Dimensions import Dimension
from Metrics import A_Error

class Clarity(Dimension) :

    def __init__(self, nom = 'Clarity', name_metrics_list = {"humanReadable.humanReadableURIs", "humanDesc.humanDesc", "longTerm.longTerm"}) :
        self.name = nom
        self.score = 0
        for names in name_metrics_list :
            self.list_metrics.add(names)