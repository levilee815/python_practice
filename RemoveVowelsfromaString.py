def remove_vowels(s):
    vowels = ["a","e","i","o","u"]
    for i in s:
        if i in vowels:
            s = s.replace(i, "")
    print(s)

remove_vowels("abcdefghijk")