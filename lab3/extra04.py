# Sean Beckford
def inchToFootInch(inches):
    ft = int(inches / 12)
    inch = inches % 12
    
    return f'''{str(inches)}" = {str(ft)}' {str(inch)}"'''

def vowelCount(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1

    return count

def vowelSwap(s):
    swap = {
        "a" : "u",
        "u" : "i",
        "i" : "a",
        "o" : "e",
        "e" : "o"
    }

    s = list(s)
    for i in range(len(s)):
        # If uppercase vowel
        if s[i].lower() in swap and s[i].isupper():
            s[i] = swap[s[i].lower()].upper()
        # Else vowel swap normally
        elif s[i] in swap:
            s[i] = swap[s[i]]

    return "".join(s)