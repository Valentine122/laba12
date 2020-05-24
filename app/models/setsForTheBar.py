from app.models.bar import Bar


class SetsForTheBar(Bar):
    def __init__(self, bar_name="N/A", price_in_uah=0, barman="UNKNOWN", production_year=2005, shapeOfIce="Ghost"):
        super().__init__(bar_name=bar_name, price_in_uah=price_in_uah, barman=barman, production_year=production_year)
        self.shapeOfIce = shapeOfIce

    def __str__(self):
        return super().__str__() + ", shapeOfIce = {}".format(self.shapeOfIce)