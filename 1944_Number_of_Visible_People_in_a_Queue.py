class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        # brute force using n^2 
        # go over each person
        # check how many people have less heigh than this person
        # if you find a person bigger than this person itslef. that is blocker. don't go beyond that.
        # in the end return the output array

        '''answer = [0]*len(heights)

        for i in range(len(heights)):
            previousHeight = 0
            for j in range(i+1,len(heights)):
                if heights[j]<=previousHeight:
                    continue
                answer[i]+=1
                previousHeight = heights[j]
                if heights[j] >= heights[i]:
                    break
                
        return answer'''

        # monotonic stack
        # stack stores candidates that a person can see in decreasing order starting from smallest heights to largest heights. 
        # for each person, first we pop all small elements from stack that this person can see. in the end we check if there is wall that means stack has elements. 
        # then we add current person in stack for next people to see
        answer = [0]*len(heights)
        stack = []

        for i in range(len(heights)-1,-1,-1):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count+=1
            
            if stack:
                count+=1
            
            stack.append(heights[i])
            answer[i] = count
        
        return answer