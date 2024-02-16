

word = input("enter words:")
vowels = "aouie"
result = 0
def vow(soz,unli,res):
    for x in soz:
        if x in unli:
            res = res + 1
    print(res)

vow(word,vowels,result)
# loop task 4
lst = [3, 6, 12, 36]
def factor_chain(lst):
    lst1 = []
    for x in lst:
        if lst[-1] % x == 0:
            lst1.append(x)
    return len(lst) == len(lst1)

print(factor_chain(lst))