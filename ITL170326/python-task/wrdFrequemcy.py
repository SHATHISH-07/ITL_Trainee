name = "shathish Kumaran shathish"

words = name.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)


# Letter frequency

# letters = []

# for c in name:
#     if(c == " "):
#         continue
#     letters.append(c)

# letterFreq = {}

# for letter in letters:
#     if letter in letterFreq:
#         letterFreq[letter] += 1
#     else:
#         letterFreq[letter] = 1

# print(letterFreq)