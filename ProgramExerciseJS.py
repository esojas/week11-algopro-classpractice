


class Fancyshopping:
    def __init__(self, foodname, amountoffood):
        self.foodname = foodname
        self.amountoffood = amountoffood
        self.__standardprice = 0
        self.__pricelist() #updates the pricelist


    def __pricelist(self):
        if self.foodname == "Dry Cured Iberian Ham":
            self.__standardprice = 177.80
        if self.foodname == "Wagyu Steaks":
            self.__standardprice = 450.00
        if self.foodname == "Matsutake Mushrooms":
            self.__standardprice = 272.00
        if self.foodname == "Kopi Luwak Coffee":
            self.__standardprice = 306.50
        if self.foodname == "Moose Cheese":
            self.__standardprice = 487.20
        if self.foodname == "White Truffles":
            self.__standardprice = 3600.00
        if self.foodname == "Blue Fin Tuna":
            self.__standardprice = 3603.00
        if self.foodname == "Le Bonnotte Potatoes":
            self.__standardprice = 270.81


    def calculate1(self):
        calculate = self.amountoffood * self.__standardprice
        return calculate


