from math import prod
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [tuple([int(j) for j in i.split(',')]) for i in f.read().splitlines()]

def find_distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5

distances = dict()
circuits = []

for i in range(len(data)):
    for j in range(i+1, len(data)):
        distances[(data[i], data[j])] = find_distance(data[i], data[j])

# distance_mins
distance_mins = sorted(distances.values())

num_to_connect = 1000

for i in range(num_to_connect):
    if i%10 == 0:
        print(f"Connecting point {i} of {num_to_connect}")
    distance = distance_mins[i]
    for k, v in distances.items():
        if v == distance:
            # see if either point is already in a circuit
            p1_in_circuit = None
            p2_in_circuit = None
            for circuit in circuits:
                if k[0] in circuit:
                    p1_in_circuit = circuit
                if k[1] in circuit:
                    p2_in_circuit = circuit
            if p1_in_circuit and p2_in_circuit:
                if p1_in_circuit != p2_in_circuit:
                    # merge circuits
                    p1_in_circuit.extend(p2_in_circuit)
                    circuits.remove(p2_in_circuit)
            elif p1_in_circuit:
                p1_in_circuit.append(k[1])
            elif p2_in_circuit:
                p2_in_circuit.append(k[0])
            else:
                circuits.append([k[0], k[1]])
            break

# top 3 circuit lengths
circuit_lengths = sorted([len(circuit) for circuit in circuits], reverse=True)
top_3_lengths = circuit_lengths[:3]
print("Top 3 circuit lengths:", prod(top_3_lengths))
