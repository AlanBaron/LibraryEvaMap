from EvaMap import EvaMap


class Dimension(EvaMap) :

    name = None
    score = 0
    list_metrics = []
    list_results = []

    def __init__(self, nom, list_metrics) :
        self.name = nom
        self.score = 0
        self.list_metrics = list_metrics

    def dim_to_string(self) :
        dico = {}
        dico["name"] = self.name
        dico["score"] =  self.score
        dico["metrics"] = self.list_results

    def calc_score(self, g_onto, liste_map, g_map, raw_data, g_link) :
        for metric in self.list_metrics :
            result_metric = metric(g_onto, liste_map, g_map, raw_data, g_link)
            self.score = self.score * result_metric.score
            self.list_results.append(result_metric)