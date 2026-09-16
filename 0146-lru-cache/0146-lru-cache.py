class LRUCache:
    def __init__(self, capacity: int):
        self.n=capacity
        self.caches=[]

        

    def get(self, key: int) -> int:

        for i in range(len(self.caches)):
            if self.caches[i][0]==key:
                val=self.caches[i][1]
                temp=self.caches.pop(i)
                self.caches.append(temp)
                return val
        
        return -1

        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.caches)):
            if self.caches[i][0]==key:
                self.caches.pop(i)
                self.caches.append((key,value))
                return
        
        if len(self.caches)==self.n:
            self.caches.pop(0)
        
        self.caches.append((key,value))
        




                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)