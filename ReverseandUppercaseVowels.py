def remove_duplicates_and_reverse(s):
    s = s[::-1]
    word = []
    
    for i in s:
        if i == "a" or i == "e" or i =="i" or i == "o" or i == "u":
            word.append(i.upper()) 
        else:
            word.append(i)
    answer = "".join(word)

    return(answer)

print(remove_duplicates_and_reverse('levi')) 