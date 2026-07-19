word = "Donkey"

with open("donkey.txt") as f:
    content = f.read()
    new=content.replace("Donkey","######")

with open("donkey.txt","w") as f:
    f.write(new)
    