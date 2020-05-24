from app.models.shapeOfIce import ShapeOfIce
from app.models.organizersForTheBar import OrganizersForTheBar


class BarManagerUtils:

    def __init__(self):
        return

    @staticmethod
    def sort_by_price_in_uah(sort_list):
        """
        sort_organizersForTheBar_stuff_by_price_in_uah
        >>> organizersForTheBar_list=([OrganizersForTheBar("Noodls",3,"Pavlo",2003, ShapeOfIce.square),OrganizersForTheBar("GalaxyBar",6,"Nastia",2010, ShapeOfIce.star),OrganizersForTheBar("FireBar",4,"Alex",2018, ShapeOfIce.triangle)])
        >>> BarManagerUtils.sort_by_price_in_uah(organizersForTheBar_list)
        >>> print(organizersForTheBar_list[0])
        Bar : bar_name = Noodls, price_in_uah = 30min, barman = Pavlo, production_year = 2003 , shapeOfIce = ShapeOfIce.square
        >>> print(organizersForTheBar_list[1])
        Bar : bar_name = FireBar, price_in_uah = 40min, barman = Alex, production_year = 2018 , shapeOfIce = ShapeOfIce.triangle
        >>> print(organizersForTheBar_list[2])
        Bar : bar_name = GalaxyBar, price_in_uah = 60min, barman = Nastia, production_year = 2010 , shapeOfIce = ShapeOfIce.star
        """
        sort_list.sort(key=lambda stuff: stuff.price_in_uah)

    @staticmethod
    def sort_by_production_year(sort_list):
        """
        sort_by_production_year
        >>> organizersForTheBar_list=([OrganizersForTheBar("Noodls",3,"Pavlo",2003, ShapeOfIce.square),OrganizersForTheBar("GalaxyBar",6,"Nastia",2010, ShapeOfIce.star),OrganizersForTheBar("FireBar",4,"Alex",2018, ShapeOfIce.ghost)])
        >>> BarManagerUtils.sort_by_production_year(organizersForTheBar_list)
        >>> print(organizersForTheBar_list[0])
        Bar : bar_name = Noodls, price_in_uah = 30min, barman = Pavlo, production_year = 2003 , shapeOfIce = ShapeOfIce.square
        >>> print(organizersForTheBar_list[1])
        Bar : bar_name = GalaxyBar, price_in_uah = 60min, barman = Nastia, production_year = 2010 , shapeOfIce = ShapeOfIce.star
        >>> print(organizersForTheBar_list[2])
        Bar : bar_name = FireBar, price_in_uah = 40min, barman = Alex, production_year = 2018 , shapeOfIce = ShapeOfIce.ghost
        """
        sort_list.sort(key=lambda stuff: stuff.production_year)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)