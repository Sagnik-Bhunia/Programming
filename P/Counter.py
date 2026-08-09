s = input("Enter a string: ")

count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

for ch in count:
    print(ch, ":", count[ch])
