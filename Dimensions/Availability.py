from Dimensions.Dimension import Dimension
from Metrics.A_Error import Error
from Metrics.localLink import localLink
from Metrics.externalLink import externalLink


class Availability(Dimension):

    def __init__(self, nom='Availability', list_metrics=[Error, localLink, externalLink]):
        super().__init__(nom, list_metrics)
