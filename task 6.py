string = "the aardvark"

vowel = ["a","e","i","o","u"]
def replace_vowels(string,vowel):
    for x in string:
        if x in vowel:
            string = string.replace(x,"#")
    return string



print(replace_vowels(string,vowel))

#loop task 6


dates = ["Sept 22", "Sept 21", "Oct 15"]
month = input("Month: ")
def upload_count(dates,month):
    l = len(month)
    res = 0
    for i in dates:
        if i[:l] == month:
            res += 1
    return res

print(upload_count(dates,month))