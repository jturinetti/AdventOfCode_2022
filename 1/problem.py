def read_input(fileName):
        inputFile = open(fileName, 'r')
        return inputFile.readlines()

def problem1(input):
    max = 0
    running_total = 0
    for n in range(len(input)):
        line = input[n]
        if line == '\n':
            if running_total > max:
                max = running_total
            running_total = 0
        else:
            running_total = running_total + int(input[n])
    return max

def problem2(input):
    full_calorie_list = []
    running_total = 0
    for n in range(len(input)):
        line = input[n]
        if line == '\n':
            full_calorie_list.append(running_total)
            running_total = 0
        else:
            running_total = running_total + int(input[n])
    
    full_calorie_list = sorted(full_calorie_list, reverse=True)
    return sum(full_calorie_list[0:3])

# program starts here
input = read_input('input.txt')
print(problem1(input))
print(problem2(input))
