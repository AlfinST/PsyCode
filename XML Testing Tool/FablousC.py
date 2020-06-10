with open("Sample.c","r") as File:
    Lines = File.readlines()
intendLevel = 0
for line in Lines:
    # print(intendLevel*'\t',line,end="")
    flag = False
    for char in line:
        if char == '{':
            print("{")
            intendLevel += 1
            # print("\t"*intendLevel,end="")
            flag = True

        elif char == '}':
            intendLevel -= 1
            print("\n"+"\t"*intendLevel+"}")
            flag = True
        elif char == '\n':
            print("\n"+"\t"*intendLevel,end="")
        
        else:
            print(char,end="")