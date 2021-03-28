
fhand = open('text.txt')
inp = fhand.read()

def revword (word):
    result = list(word)
    result = result[::-1]
    # result = ''.join(result)
    result = ''.join([str(item) for item in result]).lower()
    return result

# print(revword('Myfriend'))

length = len(inp.split())
# word = inp.split()[0]
# print(firstword)

def countword () :
    word = inp.split()[0]
    equalcounter = 0
    counter = 0
    i = 0
    while i < length:
        if counter == 0 :
                counter += 1
                continue
        
        neword = revword(inp.split()[i])
        # print(neword)
        if neword == word:
              equalcounter += 1   
        i += 1
    if equalcounter>0:
       equalcounter += 1
       
    return(equalcounter)

# print(countword())
            
            
