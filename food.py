import string

class Food:    
    def __init__(self, name = 'None', calories = 0.0, protein = 0.0, fat = 0.0, sugar = 0.0, salt = 0.0, nutrition = []):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.sugar = sugar
        self.salt = salt
        self.nutrition = nutrition

    def getFoodName(self):
        badChars = string.punctuation.replace("'","")
        while(True):
            try:
                self.name = input("Enter the name of the food: ")
                for i in self.name:
                    if i in badChars or not i.isalpha():
                        raise Exception
                else:
                    return self.name
            except Exception:
                print("Name can not contain bad characters")

    def getFoodWeight(self):
        while(True):
            try:
                weight = float(input("Enter weight of food: "))
                return weight
            except ValueError:
                print("Weight must be a number in grams(g)")

    def getFoodNutrition(self):
        try:
            self.calories = float(input("Enter calories: "))
            self.protein = float(input("Enter protein: "))
            self.fat = float(input("Enter fat: "))
            self.sugar = float(input("Enter sugar: "))
            self.salt = float(input("Enter salt: "))
            return [self.calories, self.protein, self.fat, self.sugar, self.salt]
        except ValueError:
            print("Nutrition info must be an integer or a floating number. e.g. 100 or 100.5")

    def calculateNutrition(self,nutritionInfo,weight):        
        for i in nutritionInfo:
            self.nutrition.append((i/100) * weight)
        return self.nutrition

    def __str__(self):
        nl = '\n'
        return f'Name: {self.name}{nl}Calories: {self.nutrition[0]}{nl}Protein: {self.nutrition[1]}{nl}Fat: {self.nutrition[2]}{nl}Sugar: {self.nutrition[3]}{nl}Salt: {self.nutrition[4]}'

food = Food()
food.getFoodName()
weight = food.getFoodWeight()
nutritionInfo = food.getFoodNutrition()
food.calculateNutrition(nutritionInfo,weight)

print(food)