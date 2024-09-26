def count_vowels(word):
    counts = 0
    # vowel = ['a','e','i','o','u']
    for i in word:
        if i == 'a':
            counts += 1
        elif i == 'e':
            counts += 1
        elif i == 'i':
            counts += 1
        elif i == 'o':
            counts += 1
        elif i == 'u':
            counts += 1
        else: 
            pass
    return counts
print(count_vowels('overall'))