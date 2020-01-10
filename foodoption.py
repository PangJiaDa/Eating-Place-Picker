import json

class FoodOption:
    def __init__(self, shopName="unfilled", mealTimes=[], travelTime="int", categories=[]):
        self.shopName = shopName
        self.mealTimes = mealTimes
        self.travelTime = travelTime
        self.categories = categories

    def __str__(self):
        return f"shopName: {self.shopName}\nmealTimes: {self.mealTimes}\ntravelTime: {self.travelTime}\ncategories: {self.categories}\n"
