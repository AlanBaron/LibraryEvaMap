from Dimensions import Dimension
from Metrics import A_Error

class Coverability(Dimension) :

    def __init__(self, nom = 'Coverability', name_metrics_list = {"verticalCoverage.verticalCoverage"}) :
        self.name = nom
        self.score = 0
        for names in name_metrics_list :
            self.list_metrics.add(names)