class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1 
        
        solution = []
        n = len(nums)
        
        buckets = [[] for _ in range(n+1)]

        for num,frequency in count.items():
            buckets[frequency].append(num)
        
        for i in range(n,-1,-1):
            for num in buckets[i]:
                solution.append(num)
                if len(solution) == k:
                    return solution 

        return solution 

        
# time complexity: O(N) because we go through the nums list and the count dictionary
# space complexity: O(N) because of the count dictionary and the buckets list


        
