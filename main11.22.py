# Donald Brown
# 1943301

list = input()
text = list.split()

for word in text:
    freq = text.count(word)
    print(word, freq)