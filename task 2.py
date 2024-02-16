name = input("Enter name: ")
person = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid"
}
def find_relatives(ism, inson):
    for people in inson.keys():
        if ism == people:
            print(f"Luke i'm your {inson[people]}")
            break
    else:
        print("Nope")
find_relatives(name, person)

#loop task 2
string = "abCBAaAAAAa"
def steps_to_convert(string):
    res = 0
    for x in string:
        if x.isupper():
            res += 1
    return res
print(steps_to_convert(string))


