from query import *
import datahandler

class Logic:

    def __init__(self):
        self.datahandler = datahandler.DataHandler()
        self.foodOptions = self.datahandler.getData()

    def processQuery(self, query):
        if isinstance(query, AddFoodOptionQuery):
            print("add")
        elif isinstance(query, ModifyFoodOptionQuery):
            print("mod")
        elif isinstance(query, DeleteFoodOptionQuery):
            print("del")

    def processAddFoodOptionQuery(self, query):
        assert(isinstance(query, AddFoodOptionQuery))
        self.foodOptions.append()

    def getFoodOption(self, query):
        assert(isinstance(query, AddFoodOptionQuery) or isinstance(query, ModifyFoodOptionQuery))
        return FoodOption(query.name, query.mealTimes, query.travellingTime, query.categories)

# tests
addQuery = AddFoodOptionQuery("char shao add", [1, 2], 100, [1, 2, 3, 4])
modQuery = ModifyFoodOptionQuery(1000, "char shao modify", [2], 100, [1, 2, 3, 4])
delQuery = DeleteFoodOptionQuery(0)
logic = Logic()
logic.processQuery(addQuery)
logic.processQuery(modQuery)
logic.processQuery(delQuery)
print(logic.foodOptions)