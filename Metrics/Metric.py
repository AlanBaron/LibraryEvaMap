from Dimensions import Dimension

class Metric(Dimension) :
    name = None
    score = None
    feedback = None
    description = None

    def __init__(self, nom, desc) :
        self.name = nom
        self.score = 0
        self.feedback = list()
        self.description = desc

    def metric_to_string(self):
        dico = {}
        dico["name"] = self.name
        dico["score"] =  self.score
        dico["description"] = self.description
        dico["feedback"] = self.feedback