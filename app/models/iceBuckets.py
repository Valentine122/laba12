from app.models.bar import Bar


class IceBuckets(Bar):
    def __init__(self, bar_name="N/A", price_in_uah=0, barman="UNKNOWN", production_year=2005, ice="8 liters"):
        super().__init__(bar_name=bar_name, price_in_uah=price_in_uah, barman=barman, production_year=production_year)
        self.ice = ice

    def __str__(self):
        return super().__str__() + ", ice = {}".format(self.ice)