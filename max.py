def maximum(list):
    if len(list) == 0:
        return None
    max = list[0]
    for i in list:
        if i>max:
            max = i
    return max


list = [1, 2, 3, 4, 5]
print(maximum(list))