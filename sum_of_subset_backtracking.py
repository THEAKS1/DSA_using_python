class Node:
    def __init__(self, data):
        self.data = data
        self.child = []

class SOS:
    def __init__(self):
        self.solution = []
        self.result = []

    def printSol(self):
        print(self.solution)

    def sos(self, node, child, tsum):
        if tsum == sm:
            temp = sorted(self.result[:])
            if temp not in self.solution: 
                self.solution.append(temp)
            self.result.pop()
            tsum -= node
            return tsum
        
        if not child:
            self.result.pop()
            tsum -= node
            return tsum

        new_node = Node(node)
        new_node.child = child
        for i in new_node.child:
            if tsum + i > sm:
                continue
            if i in self.result:
                continue
            tsum += i
            self.result.append(i)
            tsum = self.sos(i,child[1:], tsum)
        try:
            self.result.pop()
            tsum -= node
        except:
            pass
        return tsum

arr = [1,3,5,8,9,18]
sm = 18
n = len(arr)
tsum = 0
sumofsub = SOS()
sumofsub.sos("Root", arr, tsum)
sumofsub.printSol()