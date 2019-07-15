from Dimensions import Dimension
from Metrics.A_Error import Error


class Availability(Dimension):

    def __init__(self, nom='Availability', list_metrics=[Error]):
        super().__init__(nom, list_metrics)
