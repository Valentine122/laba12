from app.models.shapeOfIce import ShapeOfIce
from app.models.organizersForTheBar import OrganizersForTheBar


class BarManager:
    def __init__(self, organizersForTheBar_list=[]):
        self.organizersForTheBar_list = organizersForTheBar_list

    def find_organizersForTheBar_stuff_by_price_in_uah(self, price_in_uah):
        """
        find_organizersForTheBar_stuff_by_price_in_uah
        >>> organizersForTheBar_list=BarManager([OrganizersForTheBar("Noodls",3,"Pavlo",2003, ShapeOfIce.star),OrganizersForTheBar("GalaxyBar",6,"Nastia",2010, ShapeOfIce.square),OrganizersForTheBar("FireBar",4,"Alex",2018, ShapeOfIce.triangle)])
        >>> organizersForTheBar_list.find_organizersForTheBar_stuff_by_price_in_uah(3)
        Bar : bar_name = Noodls, price_in_uah = 30min, barman = Pavlo, production_year = 2003 , shapeOfIce = ShapeOfIce.star
        >>> organizersForTheBar_list.find_organizersForTheBar_stuff_by_price_in_uah(4)
        Bar : bar_name = FireBar, price_in_uah = 40min, barman = Alex, production_year = 2018 , shapeOfIce = ShapeOfIce.triangle
        >>> organizersForTheBar_list.find_organizersForTheBar_stuff_by_price_in_uah(6)
        Bar : bar_name = GalaxyBar, price_in_uah = 60min, barman = Nastia, production_year = 2010 , shapeOfIce = ShapeOfIce.square
        """
        lists = list(filter(lambda stuff: stuff.price_in_uah == price_in_uah, self.organizersForTheBar_list))
        return print("".join(str(output_list) for output_list in lists))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)