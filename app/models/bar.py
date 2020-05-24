class Bar:

    def __init__(self, bar_name="N/A", price_in_uah=0, barman="UNKNOWN", production_year=2005):
        self.price_in_uah = price_in_uah
        self.bar_name = bar_name
        self.production_year = production_year
        self.barman = barman

    def __str__(self):
        return "Bar : bar_name = {}, price_in_uah = {}0min, barman = {}, production_year = {} ".format(self.bar_name,
    self.price_in_uah, self.barman, self.production_year)