def translator(str):
    characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    morseABC = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...',
            '-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
                   
    list = ''
    if str[0] == '.' or str[0] == '-':
        str = str.split(' ')
        for i in str:
            for j in range(0,len(morseABC)):
                if i == morseABC[j]:
                    list += characters[j]
        return list
    else:
        str = str.upper()
        for i in str:
            for j in range(0,len(characters)):
                if characters[j] == i:
                    list += morseABC[j]
                    list += ' '
        return list

text = 'HELLOSZIavalenszia'
morse = '.... . .-.. .-.. --- ... --.. .. .- ...- .- .-.. . -. ... --.. .. .-'
print(translator(morse))
print(translator(text))
