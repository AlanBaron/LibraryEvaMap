class Dimension:

    name = None
    score = 0
    list_metrics = []
    list_results = []

    def __init__(self, nom, list_metrics) :
        self.name = nom
        self.list_metrics = list_metrics

    def dim_to_string(self) :
        dico = {}
        dico["name"] = self.name
        dico["score"] = self.score
        dico["metrics"] = self.list_results
        return dico

    def calc_score(self, g_onto, liste_map, g_map, raw_data, g_link):
        for metric in self.list_metrics:
            result_metric = metric(g_onto, liste_map, g_map, raw_data, g_link)
            self.score += result_metric['score'] / len(self.list_metrics)
            self.list_results.append(result_metric)
        return self.score
