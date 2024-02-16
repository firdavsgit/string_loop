#Task_8
input = input("Enter string:")

def task(input):
    x = input.count("x")
    o = input.count("o")
    if x == o:
        print(True)
    elif x <= o or x >= o:
        print(False)
    else:
        print(True)

task(input)






