from Dimensions.Dimension import Dimension
from Metrics.subClassesProperties import subClassesProperties
from Metrics.equivalentClassesProperties import equivalentClassesProperties
from Metrics.disjointWith import disjointWith
from Metrics.domainRange import domainRange

class Consistency(Dimension) :

    def __init__(self, nom='Consistency', list_metrics=[domainRange, subClassesProperties, equivalentClassesProperties, disjointWith]):
        super().__init__(nom, list_metrics)