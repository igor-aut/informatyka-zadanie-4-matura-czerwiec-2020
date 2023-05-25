with open('pary.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    number, word = line.strip().split()

    max_length = 0
    max_fragment = ""

    current_length = 1
    current_fragment = word[0]

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            current_length += 1
            current_fragment += word[i]
        else:
            if current_length > max_length:
                max_length = current_length
                max_fragment = current_fragment
            current_length = 1
            current_fragment = word[i]

    if current_length > max_length:
        max_length = current_length
        max_fragment = current_fragment

    print(max_fragment, max_length)