from Dimensions.Dimension import Dimension
from Metrics.humanReadable import humanReadableURIs
from Metrics.humanDesc import humanDesc
from Metrics.longTerm import longTerm


class Clarity(Dimension) :

    def __init__(self, nom='Clarity', list_metrics=[humanReadableURIs, humanDesc, longTerm]):
        super().__init__(nom, list_metrics)