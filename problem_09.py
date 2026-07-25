with open("copy_1.txt") as f:
    content = f.read()

with open("copy_2.txt") as f:
    copy_content = f.read()

if (content==copy_content):
    print("BOth th files are same")
else:
    print("Both the files are not same")