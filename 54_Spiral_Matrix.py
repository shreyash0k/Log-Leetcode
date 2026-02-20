class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)    
        result = []

        while left<right and top<bottom:
            # process top row
            for i in range(left,right):
                result.append(matrix[top][i])   # 1,2,3
            top+=1

            # process right col
            for i in range(top,bottom):
                result.append(matrix[i][right-1]) #  1,2,3,6,9
            right-=1

            # edge case 
            if (left<right and top<bottom) != True:
                break
            
            #process bottom row
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom-=1
            
            # process left col
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left+=1
        
        return result

        # O(m*n)
        # O(m*n)