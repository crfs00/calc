class Calculator:

    def validate(x):
        try:
            x = list(map(int, x))
        except:
            print('Please only enter numbers.')
            return None
        return x

    def failed_validation_msg(x):
        print(f'This is what you entered: {x}')

    def add(*x):
        '''Function for handling Addition'''
        y = Calculator.validate(x)
        if y:
            print(sum(y))
        else:
            Calculator.failed_validation_msg(x)

    def subtract(*x):
        '''Function for handling Subtraction'''
        y = Calculator.validate(x)
        if y:
            result = y[0]
            for i in range(1, len(y)):
                result -= y[i]

            return result
        else:
            Calculator.failed_validation_msg(x)

    def multiply(*x):
        '''Function for handling Mutiplication'''
        y = Calculator.validate(x)
        if y:
            result = y[0]
            for i in range(1, len(y)):
                result *= y[i]

            return result
        else:
            Calculator.failed_validation_msg(x)

    def divide(*x):
        '''Function for handling Division'''
        y = Calculator.validate(x)
        if y:
            result = y[0]
            for i in range(1, len(y)):
                result /= y[i]

            return result
        else:
            Calculator.failed_validation_msg(x)

    def exponent(x, y):
        '''Function for handling Exponents'''
        return x**y

    def floor_div(x, y):
        '''Function for handling Floor Division'''
        return x // y
