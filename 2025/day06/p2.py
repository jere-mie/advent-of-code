inpFile = 'input.txt'

def process_operation(nums, operator):
    if not nums:
        return 0
    elif operator == '+':
        return sum(nums)
    elif operator == '*':
        prod = 1
        for num in nums:
            prod *= num
        return prod
    return 0

with open(inpFile, 'r') as f:
    data = f.read().splitlines()
    # make the last element of data the first element
    data = [data[-1]] + data[:-1]
tot = 0
nums = []
operator = ''
for i, col in enumerate(data[0]):
    if col == '+' or col == '*':
        tot += process_operation(nums, operator)
        operator = col
        nums = []
    # go through all the rows, get the ith column, put all chars together and turn into a number
    try:
        num = int(''.join([data[row][i].strip() for row in range(1, len(data))]))
        nums.append(num)
    except ValueError:
        pass
# handle last set of nums
tot += process_operation(nums, operator)
print(tot)