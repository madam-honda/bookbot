def word_count(words):
    array=words.split()
    lenth=len(array)
    return lenth


def character_count(words):
    small=words.lower()
    #array=small.split()
    dik={}
    intext=[]
    for k in small:
        if k not in intext:
            pass
            intext.append(k)
            dik[k]=1
        else:
        #if k in intext:
            dik[k]=dik[k]+1
        
    return dik

def sorter(A):
    return A["num"]


def fancy(dictionary):
    #dictionary.sort(reverse=True, key=sort???)
    newdic=[]
    for k in dictionary:
        newdic.append({"char":k, "num":dictionary[k]})
       # newdic["char","num"]=k, dictionary[k]
        newdic.sort(reverse=True, key=sorter)

    return newdic