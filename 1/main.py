import os
result = []
with open('./input.txt', 'r') as file:
    for line in file:
        nums = [c for c in line if c.isdigit()]
        result.append(int(nums[0] + nums[-1]))
print(sum(result))


english_to_number = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


with open('./input2.txt', 'r') as file:
    s = []
    for line in file:
        n = []

        for i in range(len(line)):
            c = line[i]
            if c.isdigit():
                n.append(c)
            else:
                for word, num in english_to_number.items():
                    if line[i:].startswith(word):
                        n.append(num)
                        i = i + len(word)
                        break
        s.append(int(n[0] + n[-1]))
    print(sum(s))

