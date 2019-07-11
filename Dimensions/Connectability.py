from Dimensions import Dimension
from Metrics import A_Error

class Connectability(Dimension) :

    def __init__(self, nom = 'Connectability', name_metrics_list = {}) :
        self.name = nom
        self.score = 0
        for names in name_metrics_list :
            self.list_metrics.add(names)