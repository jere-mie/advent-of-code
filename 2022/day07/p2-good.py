import secrets
import time

start = time.time()
sizes = []

class TreeNode:
    def __init__(self, data, name, parent):
        self.hashcode = secrets.token_hex(12)
        self.data = data
        self.name = name
        self.children = []
        self.parent = parent
    def __repr__(self):
        return f'(name: {self.name}, hash: {self.hashcode[:6]} data: {self.data}, children: {self.children})'
    def total(self):
        tot = self.data
        for i in self.children:
            tot+=i.total()
        global sizes
        sizes.append(tot)
        return tot

inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()

root = TreeNode(0, '/', None)
currentDir = root
for i in text[1:]:
    # command
    if i[0] == '$':
        if i[:7] == '$ cd ..':
            currentDir = currentDir.parent
        elif i[:5] == '$ cd ':
            dirname = i[5:]
            for dir in currentDir.children:
                if dir.name == dirname:
                    currentDir = dir
                    break
    else:
        if i[:3] == 'dir':
            currentDir.children.append(TreeNode(0, i[4:], currentDir))
        else:
            currentDir.data+=int(i.split(' ')[0])

total = root.total()
objective = 30000000-(70000000-total)
sizes = sorted(sizes)
for i in sizes:
    if i>=objective:
        print(i)
        break
print(time.time()-start)