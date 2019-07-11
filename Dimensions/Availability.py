from Dimensions import Dimension
from Metrics import A_Error

class Availability(Dimension) :

    def __init__(self, nom = 'Availability', name_metrics_list = {"A_Error.Error"}) :
        self.name = nom
        self.score = 0
        for names in name_metrics_list :
            self.list_metrics.add(names)