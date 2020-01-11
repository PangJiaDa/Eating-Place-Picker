import logic
import queryparser

MESSAGE_EXIT = "Exiting. Bye!"

class Picker:
    def __init__(self):
        self.logic = logic.Logic()
        self.queryParser = queryparser.QueryParser()

    def run(self):
        while True:
            action = self.queryParser.getUserAction()
            if action == queryparser.USER_ACTION_EXIT:
                print(MESSAGE_EXIT)
                self.logic.saveChanges()
                break
            else:
                query = self.queryParser.getQuery(action)
                result = self.logic.processQuery(query)
                self.displayResult(result)
    
    def displayAll(self):
        print("Food Options:")
        for opt in self.logic.foodOptions:
            print(opt)

    def displayResult(self, result):
        print("Results:")
        print(result.message)
        for i in range(len(result.data)):
            opt = result.data[i]
            print("-" * 90)
            print(str(i).rjust(3), '.', opt.name, "|")
            print("-" * (len(opt.name) + 8))
            print(f"travelTime = {opt.travelTime}, categories = {opt.categories}")
            print("-" * 90)

picker = Picker()
picker.run()