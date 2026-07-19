for num in range(2,21):
    #for i in range(1,11):
        with open(f"table/table_of_{num}.txt","w") as f:

            for i in range(1,11):
               
               f.write(f"{num} x {i} = {num*i}\n")
        