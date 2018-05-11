
def beadando_7(string):
    string = string.lower()
    string = "".join(string.split())
    palindromes = []

    for i in range(len(string)):
        for j in range(0, i):
            substring = string[j:i+1]
            #print(substring)
            if substring == substring[::-1]:
                palindromes.append(substring)
                
    max = ''
    max_sz = 0
    for k in palindromes:
        if len(k) > max_sz:
            max = k
            max_sz = len(k)
    return max

x = input("Give me a string: ")
print(beadando_7(x))
