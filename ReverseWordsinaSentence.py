def reverse_words(sentence):
    i = len(sentence) - 1
    words = []
    while i > -1:
        words.append(sentence[i])
        i = i - 1
    answer = "".join(words)
    return print(answer) 

def reverse_words(sentence):
    words = []
    i = len(sentence) - 1
    for s in range(i):
        words.append(sentence[i])
        i = i - 1
    words.append(sentence[0])
    answer = "".join(words)
    print(answer)

reverse_words('i love you')   