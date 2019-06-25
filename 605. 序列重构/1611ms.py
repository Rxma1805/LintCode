class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        if len(seqs) == 0:
            return False
        n = len(org)
        dic={}
        flag = [0] * n
        cnt = n-1
        exited= False
        for i,o in enumerate(org):
            dic[o] = i
            
        for seq in seqs:
            for i in range(0,len(seq)):
                exited = True
                if seq[i] < 1 or seq[i]>n:
                    return False
                if i == 0:
                    continue
                pre,cur = seq[i-1],seq[i]
                if dic[pre] >= dic[cur]:return False
                #敲黑板，这是重点
                elif flag[dic[cur]] ==0 and dic[pre] +1 ==  dic[cur]:
                    flag[dic[cur]] = 1
                    cnt -= 1
                   
        if org == [] and not exited:
            return True
        return cnt == 0 and exited
        
                
