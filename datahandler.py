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



# fo = foodoption.FoodOption()
# ls = [fo,fo,fo]
# dh = DataHandler()
# dh.writeData(ls)

# queryres = dh.getData()
# for q in queryres:
#     print(str(q))