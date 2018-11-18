from collections import defaultdict

def loaddata(path):
    with open(path) as file:
        data=file.read()
    file.close()
    return data

def savedata(path,dataset):
    with open(path,"w") as file:
        data=file.write(str(dataset))
    file.close()

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.V=6301
        self.ctr=0
        self.data=""

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def addVertice(self,u,v):
        self.graph[u]=[v]

    def printGraph(self):
        print(self.graph)

    def detectbackedge(self,u,v,visited,recStack):
        if visited[v]==True or recStack[v]==True:
            return True
        return False

    def DFS(self,i,visited,recStack):
        visited[i]=True
        recStack[i]=True
        for neighbour in self.graph[i]:
            if self.detectbackedge(i,neighbour,visited,recStack)==True:
                self.ctr+=1

    def DFS2(self,i,visited,recStack):
        visited[i]=True
        recStack[i]=True
        for neighbour in self.graph[i]:
            if not self.detectbackedge(i,neighbour,visited,recStack)==True:
                self.data=self.data+str(i)+'\t'+str(neighbour)+'\n'

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for i in range(0,self.V):
            self.DFS(i,visited,recStack)

    def removecycles(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for i in range(0,self.V):
            self.DFS2(i,visited,recStack)
        return self.data

def cyclicgraph():
    data=loaddata("dataset/data.txt")
    g=Graph()
    #print([data])
    data=data.split('\n')
    #print([data])
    for i in data:
        if '#' not in i:
            if i=='':
                break
            l1=i.split('\t')
            key=int(l1[0])
            value=int(l1[1])
            if key in g.graph.keys():
                g.addEdge(key,value)
            else:
                g.addVertice(key,value)
    return g

def nonecyclicgraph():
    data=loaddata("dataset/data2.txt")
    g=Graph()
    #print([data])
    data=data.split('\n')
    #print([data])
    for i in data:
        if '#' not in i:
            if i=='':
                break
            l1=i.split('\t')
            key=int(l1[0])
            value=int(l1[1])
            if key in g.graph.keys():
                g.addEdge(key,value)
            else:
                g.addVertice(key,value)
    return g
