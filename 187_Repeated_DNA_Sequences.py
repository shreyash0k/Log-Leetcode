class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        solution = []
        map_occurance = {} 

        for i in range(0,len(s)-9):
            string = s[i:i+10]
            map_occurance[string] = map_occurance.get(string,0)+1
            
        for key,value in map_occurance.items():
            if value >=2:
                solution.append(key)

        return solution 
    
# time complexity - o(n)
# space - o(n)