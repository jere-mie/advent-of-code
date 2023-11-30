inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    nums = f.read().split(',')
    nums = [int(i) for i in nums]
print(nums)

backupnums = [i for i in nums]

for noun in range(1, 100):
    for verb in range(1, 100):
        # re-initializing nums
        nums = [i for i in backupnums]

        nums[1] = noun
        nums[2] = verb

        i = 0
        while i<len(nums):
            op = nums[i]
            if op == 1 or op == 2:
                nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]] if op == 1 else nums[nums[i+1]]*nums[nums[i+2]]
                i+=4
            else:
                break
        if nums[0] == 19690720:
            print(f'Output found! Noun={noun}, Verb={verb}, Answer={100*noun+verb}')
            exit(0)
