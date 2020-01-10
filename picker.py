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
            self.displayAll()
            if action == queryparser.USER_ACTION_EXIT:
                print(MESSAGE_EXIT)
                break
            else:
                query = self.queryParser.getQuery(action)
                self.logic.processQuery(query)
    
    def displayAll(self):
        print("Food Options:")
        for opt in self.logic.foodOptions:
            print(opt)

picker = Picker()
picker.run()