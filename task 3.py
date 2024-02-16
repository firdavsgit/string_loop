mood = input("enter feel:")
def feeling(kayfiyat):
    if kayfiyat != "":
        print(f"Today,i am feeling {kayfiyat}")

    else:
        print("Today I am feeling neutral")

feeling(mood)

#loop task 3
# txt = "Hot pictures of Danny DeVito"
txt = "How to ace BC Calculus in 5 Easy Steps"
def prevent_distractions(txt):
    lst = ("anime", "meme", "vines", "roasts", "Danny DeVito")
    for x in lst:
        if x in txt:
            return "NO!"

    return "Safe watching!"

print(prevent_distractions(txt))