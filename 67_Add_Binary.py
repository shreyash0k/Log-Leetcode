class Solution:
    def addBinary(self, a: str, b: str) -> str:
        

       
        a = a[::-1]
        b = b[::-1]
        carry = 0
        result = []
        
        for i in range(max(len(a),len(b))):
            intA = int(a[i]) if i<len(a) else 0
            intB = int(b[i]) if i<len(b) else 0 

            total = intA + intB + carry 
            result.append(str(total%2))
            carry = total // 2 
        
        if carry:
            result.append("1")
        result = result[::-1]
        return "".join(result)
    
# tc O(max(m,n))
# sc O(max(m,n)+1)
        
