inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [tuple([int(j) for j in i.split(',')]) for i in f.read().splitlines()]
largest_area = 0
for i in range(len(data)):
    for j in range(len(data)):
        if i != j:
            area = (abs(data[i][0] - data[j][0])+1) * (abs(data[i][1] - data[j][1])+1)
            # print(f"Comparing point {data[i]} with point {data[j]}, area: {area}")
            if area > largest_area:
                largest_area = area
print(largest_area)
