
def read_file(file):
    x = open(file,'r', encoding = 'utf-8')
    y = x.read() 
    content = y.splitlines()
    return content

def dict1() :
    chat = read_file('finaldata.txt')
    
    #determining the creation date
    creation_date = chat[1]
    creation_date = creation_date.split(',')
    creation_date = creation_date[0]
    #determining the chat_name
    chat_name = chat[1]
    chat_name = chat_name.split('"')
    chat_name = chat_name[1]
    #determining the creator
    creator = chat[1]
    creator = creator.split()
    creator = creator[len(creator)-1]
    
    chat = chat[2:]
    newwords = []
    mylist = list()
    
    ## making an array of the wanted names
    for line in range(len(chat)):
        words = chat[line].split()
        # print(words)
        # print(words)
        if len(words) < 7 :
            continue
        if 'הוסיף/ה' not in str(words) and 'מקצה-לקצה' not in str(words)  :
            tmp = " ".join(words).strip()
            # newwords.append(tmp.split("/n"))  
            tmp = tmp.split(":")
            newname = tmp[1].split("-")
            newname = newname[1].strip()
            mylist.append(newname)
            newwords.append(tmp)
    new_list =[]
    
    num_of_participants = len(newwords)
    
    for i in range(len(newwords)):
        newwords[i][0] = "datetime : = " + newwords[i][0]
        newwords[i][1] = "id = " + str(i)
        newwords[i][2] = "text = " + newwords[i][2]
        new_list.append({newwords[i][0],newwords[i][1]+newwords[i][2]})
    
    metadata = {"chat_name" : chat_name,"creation_date" : creation_date,
                "num_of_participants" : num_of_participants,"creator" : creator}
    lastdict = {"messeges" : new_list,"metadata" : metadata}
    
    print(lastdict)
    
dict1()

    