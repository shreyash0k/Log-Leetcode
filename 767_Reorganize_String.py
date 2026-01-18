class Solution:
    def reorganizeString(self, s: str) -> str:
        # count 
        count = Counter(s) 
        # a=2, b1 ... 
        maxHeap = [[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(maxHeap)

        result = "" 
        prev = None

        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            cnt,char = heapq.heappop(maxHeap)
            result+=char
            cnt+=1

            if prev is not None:
                heapq.heappush(maxHeap,prev)
                prev = None

            if cnt!=0:
                prev = [cnt,char]

        return result


# time complexity: O(nlogk) n is length of string, k is number of unique characters
# space complexity: O(k) k is number of unique characters 