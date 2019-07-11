from EvaMap import EvaMap
#from Metrics import NomMetrics

class Dimension(EvaMap) :

    name = None
    score = None
    list_metrics = None

    def __init__(self, nom, name_metrics_list) :
        self.name = nom
        self.score = 0
        for names in name_metrics_list :
            self.list_metrics.add(names)

    def dim_to_string(self) :
        dico = {}
        dico["name"] = self.name
        dico["score"] =  self.score
        #for metrics in list_metrics :
            #dico["metrics"] = metrics.metric_to_string()

    def calc_score(self) :
        for metrics in self.list_metrics :
            self.score = self.score + metrics()
            #Pas besoin du poids normalement
