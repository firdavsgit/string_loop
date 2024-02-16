string = "abcde"
string1 = "abcwf"

def uniwue(string, string1):
    i  = 0
    for x in string:
        for y in string1:
            if x==y:
                i+=1
    print(len(string)-i)

uniwue(string, string1)



