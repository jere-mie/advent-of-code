"""
# PSEUDOCODE FOR SOLUTION

def check(bag a):
    sum = 0
    for child(num, colour) in bag:
        sum+=num*check(colour)
    return sum

__main__:
    get input
    print(check('shiny gold'))

"""