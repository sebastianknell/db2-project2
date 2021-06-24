words = ["hi", "how", "are", "sebastian"]
words1 = ["hi", "how", "are", "you"]
for w in words:
    if w in words1:
        words.remove(w)

print(words)

words = ["hi", "how", "are", "sebastian"]
words1 = ["hi", "how", "are", "you"]

i = 0
while i < len(words):
    if words[i] in words1:
        words.pop(i)
    else:
        i += 1
print(words)
