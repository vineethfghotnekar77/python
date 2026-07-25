words=["Donkey","Horse","Cow","Pig"]

with open("05_prob.txt") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#"*len(word))

with open("05_prob.txt" , "w") as f:
    f.write(content)