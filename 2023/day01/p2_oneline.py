print(sum([int(i[0]+i[-1]) for i in [[{'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0', '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}[j] for j in i] for i in [__import__('regex').findall(r'(\d|one|two|three|four|five|six|seven|eight|nine|zero)', q, overlapped=True) for q in open('input.txt', 'r').read().splitlines()]]]))
