#Birla Alexandru si Puscasu Vlad
def maxim_liste(l1:list,l2:list):
    l1.sort()
    l2.sort()
    maxim=max(l1[-1],l2[-1])
    return maxim+(0.25*maxim)

def yaxis(maxim):
    buc=maxim//10
    l=[]
    for i in range(11):
        l.append(i*buc)
    return l

def get_percent(x,y):
    val=y*100/x
    return int(val)

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
