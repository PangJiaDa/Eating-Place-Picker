import json

class FoodOption:
    def __init__(self, name="unfilled", mealTimes=[], travelTime="int", categories=[]):
        self.name = name
        self.mealTimes = mealTimes
        self.travelTime = travelTime
        self.categories = categories

    def __str__(self):
        return f"name: {self.name} mealTimes: {self.mealTimes} travelTime: {self.travelTime} categories: {self.categories}"
