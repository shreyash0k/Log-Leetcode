class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for i in range(0,len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                poppedString = ""  
                while stack[-1]!="[":
                    poppedString = stack.pop()+ poppedString 
                stack.pop() 
                poppedNumber = ""
                while stack and stack[-1].isdigit():
                    poppedNumber = stack.pop() + poppedNumber
                stack.append(int(poppedNumber) * poppedString)
        
        return "".join(stack)




        # go over list using a pointer like i

        # if current element is not closing bracket, append it to stack. 

        # if current element is a closing bracket, 
            # keep popping elements and creating a string of popped elements till you find an opening bracket
            # pop again to remove the openeing bracket from stack. 
            # now keep popping to figure out the multiplier. keep popping till element is a digit
            # now multiply popped string with popped multiplier 
            # append this new string to stack 
        