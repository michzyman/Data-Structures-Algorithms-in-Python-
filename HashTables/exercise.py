
class hash:
    def __init__(self, size):
        self.data = [None] * (size)

    #Hash Function
    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]
        return "undefined"

    def keys(self):
        keylist = []

        for i in range(len(self.data)):
            if(self.data[i]):
                for j in range(len(self.data[i])):
                    keylist.append(self.data[i][j][0])
        
        return keylist

myHash = hash(2) #To demonstrate immunity to keys collision
myHash.set("grapes", 10000)
myHash.set("apples", 54)
myHash.set("oranges", 2)

print(myHash.keys())

