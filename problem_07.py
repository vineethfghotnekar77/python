with open("log.txt") as f:
    lines = f.readlines()

lineno=1
for line in lines:
    if ("xyz" in line):
        print(f"Python is present:{lineno}")
        break
        line+=1

else:
    print("Python is not present in the content")