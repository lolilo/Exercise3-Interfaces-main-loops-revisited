import arithmetic as art

operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def validate_input(user_input):
    for i in user_input:
        is_a_number = True
        for char in i:
            if char not in numbers:
                is_a_number = False
        if is_a_number == False and i not in operators:
            print "To use this calculator, please input an operator followed by numbers."
            break


    if user_input[0] not in operators:
        print "Please use one of the following operators (or q for quit): "
        print operators
        return False
    #elif len(user_input) > 3 or len(user_input) < 1:
     #   print ""
    return True

while True:
    raw_numbers = raw_input("> ")

    if raw_numbers == 'q':
        break

    tokens = raw_numbers.split(" ")

    operator = tokens[0]

    nums = tokens[1:]

    if validate_input(tokens) == False:
        continue

    n1 = int(nums[0])

    if len(nums) > 1:
        n2 = int(nums[1])

    if operator == '+':
        print art.add(n1, n2)
    elif operator == '-':
        print art.subtract(n1, n2)
    elif operator == '*':
        print art.multiply(n1, n2)
    elif operator == '/':
        print art.divide(n1, n2)
    elif operator == 'square':
        print art.square(n1)
    elif operator == 'cube':
        print art.cube(n1)
    elif operator == 'pow':
        print art.power(n1, n2)
    elif operator == 'mod':
        print art.mod(n1,n2)