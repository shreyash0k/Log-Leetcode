class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # find smaller list and make it nums1
        if (len(nums2)<len(nums1)):
            nums2, nums1 = nums1, nums2 
        
        left = 0
        right = len(nums1) -1  
        totalSize = len(nums1) + len(nums2)
        while True:
            i = (left + right) // 2 
            j = totalSize//2 - i - 2 

            leftA = nums1[i] if i >=0 else float('-inf')
            rightA = nums1[i+1] if i+1<len(nums1) else float ('inf')
            leftB = nums2[j] if j >=0 else float('-inf')
            rightB = nums2[j+1] if j+1<len(nums2) else float ('inf')

            if leftA<=rightB and leftB<=rightA:
                if totalSize % 2 != 0:
                    return min(rightA, rightB)
                else:     
                    return ( max(leftA,leftB) + min(rightA,rightB) )/ 2
            
            elif leftA>rightB:
                right = i - 1 
            else:
                left = i + 1 

            
        
# tc O (log(min(nums1,nums2)))
# sc O (1)

