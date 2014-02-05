import arithmetic as art

operators = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']

def validate_input(user_input):
    pass

while True:
    raw_numbers = raw_input("> ")

    if raw_numbers == 'q':
        break

    tokens = raw_numbers.split(" ")

    operator = tokens[0]

    nums = tokens[1:]

    #if validate_input(tokens) == False:
     #   continue

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