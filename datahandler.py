import pickle
import foodoption

class DataHandler:
    def __init__(self):
        pass

    # returns a list of all FoodObjects in database.txt
    def getData(self):
        database = open("database.txt", "rb")
        return pickle.load(database)


    # writes all the foodobjects to database.txt as a bytestream
    def writeData(self, listOfFoodObjects):
        database = open("database.txt", "wb")
        pickle.dump(listOfFoodObjects, database) # dump directly into file


# fo1 = foodoption.FoodOption()
# fo2 = foodoption.FoodOption("Option A", [1], 10, [1, 2, 3])
# fo3 = foodoption.FoodOption("Option B", [2], 20, [2, 3, 4])
# fo4 = foodoption.FoodOption("Option C", [3], 30, [3, 4, 5])
# ls = [fo1, fo2, fo3, fo4]
# dh = DataHandler()
# dh.writeData(ls)

# queryres = dh.getData()
# for q in queryres:
#     print(str(q))