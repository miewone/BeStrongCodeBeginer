def merge(array):
    sArray = []
    content = ""
    for i in array:
        if i in opertaor:
            sArray.append(content)
            content = ""
        
        content += i
    sArray.append(content)
    numbers = [int(i) for i in sArray]

    return numbers

S = input()
sArray = list()
opertaor = ["+","-"]
content = ""
numbers = list()
number = S.split("-")

for idx,value in enumerate(number):
    if idx == 0:
        numbers.append(sum(merge(value)))
    else :
        numbers.append(sum(merge(value))*-1)

print(sum(numbers))
# for i in S:
#     if i in opertaor:
#         sArray.append(content)
#         content = ""
    
#     content += i
# sArray.append(content)

# numbers = [int(i) for i in sArray]
# print("test")

