class Calculator:

    def validate(arg_list_to_validate):
        '''
        Ensure that all elements are digits and convert strings to ints

        :param arg_list_to_validate: A list of digits in int, float, or string form
        :rtype A list of floats if no errors, 'None' otherwise.
        '''
        try:
            arg_list_to_validate = list(map(float, arg_list_to_validate))
        except:
            print('Please only enter numbers.')
            return None
        return arg_list_to_validate

    def failed_validation_msg(invalid_list):
        '''Output the values that the user entered if the validate method finds an error'''
        print(f'This is what you entered: {invalid_list}')

    def add(*args_list_to_add):
        '''Function for handling Addition'''
        validate_list = Calculator.validate(args_list_to_add)
        if validate_list:
            print(sum(validate_list))
        else:
            Calculator.failed_validation_msg(args_list_to_add)

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
