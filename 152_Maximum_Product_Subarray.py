class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # maintain minProduct and maxProduct 
        # go over input list and comput minProduct and maxProduct at each step
        # maxProduct = max(num,num*prevMaxProduct,num*prevMinProduct)
        # minProduct = min(num,num*prevMaxProduct,num*prevMinProduct)

        maxProduct = 1 
        minProduct = 1
        result = -1e9
        for num in nums:
            prevMaxProduct = maxProduct
            maxProduct = max(num, maxProduct*num, minProduct*num)   
            minProduct = min(num, prevMaxProduct*num, minProduct*num)
            result = max(maxProduct,minProduct,result)
        
        return result

        # tc O(n)
        # sc O(1)