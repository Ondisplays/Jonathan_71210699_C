class Node:
    def __init__(self, data, parent=None):
        self._data = data
        self._children = []
        self._parent = parent

class Tree:
    def __init__(self, data):
        self._data = data
        self._count = 0
    
    def addChild(self, parent, data):
        anak = Node(data, parent)
        anak._children.append(data)

    def minus(node):
        count = val300
        for i in node.children():
            return count - i.operator()
        print(node.operator(), end = ' ')

    def sibling(self) : 
        while True : 
            total = 0 
            ortu = self.parent() 
            for i in ortu.children() : 
                total += i.operator()
            print("sibling : ", total)
            break

if __name__ =='__main__':
    val300 = Node(300)
    t = Tree(val300) #Level 0
 
    #Level 1 parent 120
    val9 = t.addChild(val300, 9) 
    val1 = t.addChild(val300, 1)
 
    #Level 2 parent 9
    val11 = t.addChild(val9, 11) 
    val99 = t.addChild(val9, 99) 
 
    #Level 2 parent 1
    val17 = t.addChild(val1, 17) 
 
    #Level 3 parent 11
    val28 = t.addChild(val11, 28) 
    val72 = t.addChild(val11, 72)
 
    #Level 3 parent 99
    val90 = t.addChild(val99, 90) 
    val33 = t.addChild(val99, 33)
 
    #Level 3 parent 17
    val17 = t.addChild(val17, 2)
    val17 = t.addChild(val17, 4)
    val17 = t.addChild(val17, 43)
 
    # No 2. #
    print(f'Sisa hasil pengurangan dari node {val300.data} adalah {t.minus(val300)}')
 
    # No 3. #
    print(f'Total nilai dari semua saudara pada node {val90.data} adalah {t.sibling(val90)}')