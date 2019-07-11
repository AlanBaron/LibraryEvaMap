from Dimensions import Dimension
from Metrics import A_Error

class Consistency(Dimension) :

    def __init__(self, nom = 'Consistency', name_metrics_list = {}) :
        self.name = nom
        self.score = 0
        for names in name_metrics_list :
            self.list_metrics.add(names)