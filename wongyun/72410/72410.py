import re
def solution(new_id):
    answer = ''
    tmp = ""
    id = new_id.lower()
    reg = re.compile('[a-z0-9-_.]*')
    id = reg.findall(id)
    id = "".join(id)
    print(id)
    id = re.sub('\\.{2,}',".",id)
    print(id)
    id = re.sub('^\.|\.$',"",id)
    print(id)
    if id =="":
        id = "a"
    if len(id) >= 15 :
        reg = re.compile('[a-z0-9-_.]{15}')
        id = reg.match(id)
        id = id.group()
        id = re.sub('\.$',"",id)
    print(id)
    if len(id) <=2 :
        text = id
        reg = re.compile('.$')
        id = reg.search(id)
        lastChar = id.group()
        id = text
        while len(id) <=2:
            id += lastChar
    print(id)
    return id