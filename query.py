# Class representing a Query Object

class Query:
    def __init__(self):
        pass

class AddFoodOptionQuery(Query):
    def __init__(self, name, mealTimes, travellingTime, categories):
        super(AddFoodOptionQuery, self).__init__()
        self.name = name
        self.mealTimes = mealTimes
        self.travellingTime = travellingTime
        self.categories = categories

    def __str__(self):
        return "AddFoodOptionQuery: name = {}, mealTimes = {}, travellingTIme = {}, categories = {}".format(
            self.name, self.mealTimes, self.travellingTime, self.categories)
    
class ModifyFoodOptionQuery(Query):
    # selector is an integer, which stores the index of the FoodOption being selected for modification
    def __init__(self, selector, name, mealTimes, travellingTime, categories):
        super(ModifyFoodOptionQuery, self).__init__()
        self.selector = selector
        self.name = name
        self.mealTimes = mealTimes
        self.travellingTime = travellingTime
        self.categories = categories

    def __str__(self):
        return "ModifyFoodOptionQuery: selector = {}, name = {}, mealTimes = {}, travellingTIme = {}, categories = {}".format(
            self.selector, self.name, self.mealTimes, self.travellingTime, self.categories)

class DeleteFoodOptionQuery(Query):
    def __init__(self, selector):
        super(DeleteFoodOptionQuery, self).__init__()
        self.selector = selector
    
    def __str__(self):
        return "AddFoodOptionQuery: selector = {}".format(self.selector)

# unit tests
# addQuery = AddFoodOptionQuery("char shao add", [1, 2], 100, [1, 2, 3, 4])
# print(addQuery)
# modQuery = ModifyFoodOptionQuery(1000, "char shao modify", [2], 100, [1, 2, 3, 4])
# print(modQuery)
# delQuery = DeleteFoodOptionQuery(0)
# print(delQuery)
