f=open("poem.txt")
count=f.read()

if("Twinkle" in count):
    print("Twinkle is present in the poem")

else:
    print("Twinkle is not present in the poem")
f.close()