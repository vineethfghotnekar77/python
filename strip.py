lst=["apple","banana","cherry","orange","kiwi","melon","mango"]

def remove(lst,word):
    n=[]
    for item in lst:
        if item!=word:
            n.append(item.strip(word))
    return n

a=remove(lst,"ge")
print(a)