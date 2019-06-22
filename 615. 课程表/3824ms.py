class Solution:
    
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):

        # write your code here
        from collections import defaultdict
        
        dic = defaultdict(list)
        countDic = {}
        res = []
        
        for i in range(numCourses):
            countDic[i] = 0
        for pre in prerequisites:
            for i in pre[1:]:
                countDic[i] +=1
                dic[pre[0]].append(i)
        
        from queue import Queue
        q = Queue()
        
        for i in countDic:
            if countDic[i] ==0:
                q.put(i)
                res.append(i)
        
        while not q.empty():
            # print(dic)
            # print(countDic)
            i = q.get()
            for j in dic[i]:
                countDic[j] -=1
                if countDic[j] == 0:
                    q.put(j)
                    res.append(j)
            
        return len(res) == numCourses  
