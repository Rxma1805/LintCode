"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        #BFS
        if not graph:
            return []
        countdic = self.count(graph)
        from queue import Queue
        q = Queue()
        result = []
        for i in countdic:
            if countdic[i] ==0:
                q.put(i)
                result.append(i)
        
        while q.qsize() != 0:
            i = q.get()
            for j in i.neighbors:
                countdic[j]-=1
                if countdic[j] == 0:
                    result.append(j)
                    q.put(j)
                    
        return result
            
    def count(self,graph):
        dic={}
        for g in graph:
            dic[g] = 0
        for g in dic:
            for i in g.neighbors:
                dic[i] +=1
        return dic
