word = input("enter word")
def wo(soz):

    y = soz[0]
    x = soz[1]
    print(f"{y}{x}... {y}{x}... {soz}?")
wo(word)

# loop task 1
msg = input("word: ")
def how_many_times(msg):
    lst = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    count = 0
    for i in msg.lower:
        count += lst.index(i)
    return count

print(how_many_times(msg))

