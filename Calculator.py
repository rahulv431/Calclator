class Calculator:
    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"

calc = Calculator()

calc.addition(1,2)