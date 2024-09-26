def RemoveConsecutiveDuplicates(string):
    prev = ""
    answer = []
    for char in string:
        if prev == char:
            pass
        else: 
            answer.append(char)
        prev = char
    answer = ''.join(answer)
    return answer

print(RemoveConsecutiveDuplicates('fffsdsuajihhhhh'))