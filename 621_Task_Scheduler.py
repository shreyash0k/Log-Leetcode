class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # make hashmap containing occurances of tasks e.g A:3, B:2, C:1..
        mapOfTasks = Counter(tasks)
        maxHeap = [-occurance for occurance in mapOfTasks.values()]
        heapq.heapify(maxHeap)
        time = 0 
        queue = deque()
        while maxHeap or queue:
            time+=1
            if maxHeap:
                occurance = 1+heapq.heappop(maxHeap)
                if occurance!=0:
                    queue.append([occurance,time+n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap,queue.popleft()[0])
            
        return time 

        # tc O(m*n) where m is number of unique characters and n is interval
        # sc O(m*n)
            




