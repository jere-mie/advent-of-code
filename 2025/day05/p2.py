inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    ranges, _ = [i.split('\n') for i in f.read().split('\n\n')]

ranges = sorted([list(map(int, r.split('-'))) for r in ranges])

final_ranges = []
for r in ranges:
    overlap_found = False
    for fr in final_ranges:
        if fr[0] <= r[0] <= fr[1] or fr[0] <= r[1] <= fr[1]:
            overlap_found = True
            fr[0] = min(fr[0], r[0])
            fr[1] = max(fr[1], r[1])
            break
    if not overlap_found:
        final_ranges.append(r)

print(sum([r[1] - r[0] + 1 for r in final_ranges]))
