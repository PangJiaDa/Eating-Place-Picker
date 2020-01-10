USER_ACTION_RANDOM = 1
USER_ACTION_ADD = 2
USER_ACTION_MODIFY = 3
USER_ACTION_DELETE = 4

### returns true iff userInput is an integer and upperBound <= userInput <= lowerBound
def isValidIntInput(userInput, upperBound, lowerBound):
    return userInput.isdigit() and (upperBound <= int(userInput) <= lowerBound)

class QueryParser:

    def __init__(self):
        pass

    def getUserAction(self):
        print("What do you want to do:")
        print("1. Get random pick.")
        print("2. Add Food Option.")
        print("3. Modify Food Option.")
        print("4. Delete Food Option.")
        choice = input()
        while not (isValidIntInput(choice, 1, 4)):
            print("Input must be 1, 2, 3 or 4. Please try again.")
            print("What do you want to do:")
            print("1. Get random pick.")
            print("2. Add Food Option.")
            print("3. Modify Food Option.")
            print("4. Delete Food Option.")
            choice = input()
        return int(choice)

    def getName(self):
        print("What is the name of this place?")
        name = input()
        while not name.isalnum():
            print("Name must be alphanumeric. Please try again.")
            print("What is the name of this place?")
            name = input()
        return name

    def getMealTimes(self):
        print("What meal times does is this place for?")
        print("1. Breakfast")
        print("2. Lunch")
        print("3. Dinner")
        print("4. Supper")
        choices = input().split()
        while not all(map(lambda x: isValidIntInput(x, 1, 4), choices)):
            print("Input must be 1, 2, 3 or 4. Please try again.")
            print("1. Breakfast")
            print("2. Lunch")
            print("3. Dinner")
            print("4. Supper")
            choices = input().split()
        return list(map(int, choices))

    def getTravellingTime(self):
        print("How long to travel to this location?")
        travellingTime = input()
        while not isValidIntInput(travellingTime, 0, 10000):
            print("Travelling time must be an integer between 0 to 10000 inclusive. Please try again.")
            print("How long to travel to this location?")
            travellingTime = input()
        return int(travellingTime)

    def getCategories(self):
        print("What categories is this place in?")
        print("1. Chinese")
        print("2. Malay")
        print("3. Indian")
        print("4. Western")
        print("5. Japanese")
        print("6. Korean")
        choices = input().split()
        while not all(map(lambda x: isValidIntInput(x, 1, 6), choices)):
            print("Input must be 1 to 6. Please try again.")
            print("What categories is this place in?")
            print("1. Chinese")
            print("2. Malay")
            print("3. Indian")
            print("4. Western")
            print("5. Japanese")
            print("6. Korean")
            choices = input().split()
        return list(map(int, choices))

    def getRandomFoodOption(self):
        randomFoodOption = "ARandomFoodPlace (Stub method)" # todo: get rand option
        return randomFoodOption

    def getFoodOptionFromUser(self):
        name = self.getName()
        mealTimes = self.getMealTimes()
        travellingTime = self.getTravellingTime()
        categories = self.getCategories()
        # debugging
        print(name)
        print(mealTimes)
        print(travellingTime)
        print(categories)

    def getQuery(self):
        userAction = self.getUserAction()
        if userAction == USER_ACTION_RANDOM:
            print(self.getRandomFoodOption())
        elif userAction == USER_ACTION_ADD:
            self.getFoodOptionFromUser()
        elif userAction == USER_ACTION_MODIFY:
            pass
        elif userAction == USER_ACTION_DELETE:
            pass
        else:
            print("Error, invalid user action")

qp = QueryParser()
qp.getQuery()