def solve(arr):
    freq = {}
    for i in arr:
        if i in freq.keys():
            freq[i] += 1 
        else:
            freq[i] = 1 

    key = sorted(freq.keys()) 
    base1 = key[0]
    base2 = base1 + 1

    if base2 not in key:
        freq[base2] = 0
    
    for i in range(1, len(key)):
        if (key[i] - base1)%2 == 0:
            freq[base1] += freq[key[i]]
            freq[key[i]] = 0
        elif key[i] - base2 == 0:
            continue
        else:
            freq[base2] += freq[key[i]]
            freq[key[i]] = 0
    if freq[base1] > freq[base2]:
        return freq[base2]
    else:
        return freq[base1]


inp = []
while True:
    a = input("")
    if a == '':
        break
    inp.append(int(a))

print(solve(inp))