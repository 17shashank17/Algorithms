from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printt(self):
        print(self.graph)

    def bfs(self,u):
        visited=[False]*len(self.graph)
        queue=[]
        visited[u]=True
        queue.append(u)
        while queue:
            print(queue.pop(0),end=" ")
            for i in self.graph[u]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

g=graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,3)
g.printt()
g.bfs(1)