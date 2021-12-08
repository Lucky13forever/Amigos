#Puscasu Vlad si Birla Alexandru
def maxim_liste_vechi(l1:list,l2:list):
    maxim = 0
    for i in l1:
        if i > maxim:
            maxim = i
    for i in l2:
        if i > maxim:
            maxim = i      
    aux = maxim
    c = 0
    p = 1
    while aux:
        c+=1
        p*=10
        aux//=10
    p//=10
    try:
        return (maxim//p + 1)*p
    except:
        return 0

def maxim_liste(l1: list, l2: list):
    unu = sorted(l1)
    doi = sorted(l2)

    maxim = max(unu[-1], doi[-1])
    return maxim


def yaxis(maxim :int):
    buc=maxim//10
    l=[]
    for i in range(11):
        aux = i*buc
        if aux%10:
            aux += 10 - aux%10
        l.append(aux)
    return l

def get_percent(x,y):
    try: 
        val=float(y*100/x)
    except:
        val = 0
    return val

def colums(max_point:int, data:list):
    l=[]
    for elem in data:
        #cat la suta din 'max_point' (rotunjit la int) este fiecare element din lista 'data1'
        l.append(get_percent(max_point,elem))
    return l

class Graph:
    def __init__(self, data1 :list, data2 :list):
        self.max_point=maxim_liste(data1,data2)
        self.yaxis_values=yaxis(self.max_point)
        self.colums1=colums(self.max_point,data1)
        self.colums2=colums(self.max_point,data2)
        
        
