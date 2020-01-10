import json

class FoodOption:
    def __init__(self, shopName="unfilled", mealTimes=[], travelTime="int", cuisine=[]):
        self.shopName = shopName
        self.mealTimes = mealTimes
        self.travelTime = travelTime
        self.cuisine = cuisine

    def __str__(self):
        return f"shopName: {self.shopName}\nmealTimes: {self.mealTimes}\ntravelTime: {self.travelTime}\ncuisine: {self.cuisine}\n"
