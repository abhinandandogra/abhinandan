class BMIcalculator:
    def _init_(self, weight, height):
        self.weight = weight
        self.height = height
    
    def calculate_bmi(self):
        
        if self.height <= 0:
            raise ValueError("Height must be a positive number.")
        bmi = self.weight / (self.height ** 2)
        return bmi
    
    def interpret_bmi(self, bmi):
        
        if bmi < 0:
            raise ValueError("BMI cannot be negative.")
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        
        calculator = BMIcalculator(weight, height)
        bmi = calculator.calculate_bmi()
        interpretation = calculator.interpret_bmi(bmi)
        
        print("Your BMI is:", bmi)
        print("Interpretation:", interpretation)
    except ValueError as ve:
        print("Error:", ve)


    main()
