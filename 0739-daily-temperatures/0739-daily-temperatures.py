class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r=[0]*len(temperatures)
        s=[]
        for i in range(len(temperatures)):
            if not s:
                s.append(i)
                continue
            else:
                while s and temperatures[s[-1]]<temperatures[i]:
                    r[s[-1]]=i-s[-1]
                    s.pop()
                s.append(i)
        return r