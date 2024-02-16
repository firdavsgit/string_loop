harf = input("enter")
object = {
    "A": 67,
    "a": 97
}

# loop task 5
obj = {"skate": 10, "painting": 20}
limit = int(input("Son: "))
def calc_diff(obj, limit):
    result = 0
    for x in obj:
        result += obj[x]
    return (result - limit)

print(calc_diff(obj, limit))




