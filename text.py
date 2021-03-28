
fhand = open('text.txt')
inp = fhand.read()

firstword = ""
def revword (word):
    result = list(word)
    result = result[::-1]
    # result = ''.join(result)
    result = ''.join([str(item) for item in result]).lower()
    return result

# print(revword('Myfriend'))

length = len(inp.split())
firstword = inp.split()[0]
# print(firstword)

def countword () :
    equalcounter = 0
    counter = 0
    i = 0
    while i < length:
        if counter == 0 :
                counter += 1
                continue
        
        neword = revword(inp.split()[i])
        print(neword)
        if neword == firstword:
              equalcounter += 1   
        i += 1
    return(equalcounter+1)

# print(countword())
            
            
