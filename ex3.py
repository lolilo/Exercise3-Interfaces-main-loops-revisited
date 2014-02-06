import arithmetic as art

operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
numbers = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def validate_input(user_input):
    if len(user_input) < 1:
        print "To use this calculator, please input an operator followed by (an) integer(s)."
        return False
    for i in user_input:
        #print "Evaluating %s" % i
        is_a_number = True
        for char in i:
            if char not in numbers:
                #print char + " is not a number."
                is_a_number = False
        if is_a_number == False and i not in operators:
            print "To use this calculator, please input an operator followed by (an) integer(s)."
            return False


    if user_input[0] not in operators:
        print "Please use one of the following operators (or q for quit): "
        print operators
        return False

    return True

def how_many_numbers(user_input):
    return len(user_input)

def convert_nums_to_int(nums):
    converted_nums = []
    for n in nums:
        converted_nums.append(int(n))
    return converted_nums

while True:
    raw_numbers = raw_input("> ")

    if raw_numbers == 'q':
        break

    tokens = raw_numbers.split(" ")

    for i in range(tokens.count('')):
        tokens.remove('')

    if validate_input(tokens) == False:
        continue

    operator = tokens[0]

    nums = convert_nums_to_int(tokens[1:])

    num_args = how_many_numbers(nums)

    error_string = "For %s, please input \" %r \" followed by %s number(s), separated by spaces." 

    if operator == '+':
        if num_args != 2:
            print error_string %("addition", "+", "two")
        else: 
            print art.add(nums[0], nums[1])

    elif operator == '-':
        if num_args != 2:
            print error_string %("subtraction", "-", "two")
        else:
            print art.subtract(nums[0], nums[1])

    elif operator == '*':
        if num_args != 2:
            print error_string %("multiplication", "*", "two")
        else: 
            print art.multiply(nums[0], nums[1])

    elif operator == '/':
        if num_args != 2:
            print error_string %("division", "/", "two")
        elif nums[1] == 0:
            print "Cannot divide by zero!"
        else: 
            print art.divide(nums[0], nums[1])

    elif operator == 'square':
        if num_args != 1:
            print error_string %("square", "square", "one")
        else: 
            print art.square(nums[0])

    elif operator == 'cube':
        if num_args != 1:
            print error_string %("cube", "cube", "one")
        else: 
            print art.cube(nums[0])

    elif operator == 'pow':
        if num_args != 2:
            print error_string %("power", "pow", "two")
        else: 
            print art.power(nums[0], nums[1])

    elif operator == 'mod':
        if num_args != 2:
            print error_string %("mod", "mod", "two")
        else: 
            print art.mod(nums[0],nums[1])