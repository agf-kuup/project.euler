def subs(roman):
    result = roman
    switch = {"VIIII": "IX","IIII": "IV","LXXXX": "XC","XXXX": "XL","DCCCC": "CM", "CCCC": "CD"}
    for i in changes.keys():
        result = result.replace(i, switch[i])
    return result
ans=0
for line in open('p089_roman.txt',"r"):
    roman = line.strip()
    ans+=len(roman)-len(subtractive(roman))
print(ans)