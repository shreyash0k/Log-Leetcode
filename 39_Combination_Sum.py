class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = 0 
        result = []
        def dfs(total,index,subset):
            if total == target:
                result.append(subset.copy())
                return
            if total > target:
                return

            for i in range(index,len(candidates)):
                subset.append(candidates[i])
                dfs(total+candidates[i], i, subset)
                subset.pop()
        
        dfs(0,0,[])
        return result 


        # tc 
        # we produce n nodes at 1 level 
        # we can have total level = target/min(candidates)
        # so total tc is n^(t/m) 
        # we also perform copy operation at each leaf node 
        # a substring can have max length  target/min(candidates)
        # so total tc becomes O(t/m * n^(t/m))

        # sc 
        # recursion stack can go upto t/m 
        # we can have total k valid combinations. 
        # each valid combination can be of size t/m
        # so sotring them all is k*(t/m)