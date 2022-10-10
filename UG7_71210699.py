class StackNode :
	def __init__(self, element, next) :
		self.element = element
		self.next = next

class PrefixConverter:
    precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
    def __init__(self):
        self.stackList = ['?']
    def push(self,data):
        self.stackList.append(data)
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"

    def cekValidExpression(self,expression):
        if expression.isalpha() or expression in '1234567890':
            return True
        else:
            return False
    def infixToPrefix(self,expression):
        expression=""
        for i in expression:
            if(self.cekValidExpression(i)):
                expression += i
            elif(i in '+-*/^'):
                while(len(self.elements)and self.precedence[i] < self.precedence[self.peek()]):
                    expression+=self.pop()
                self.push(i)
            while len(self.elements):
                if(self.peek()=='('):
                    self.pop()
                else:
                    expression+=self.pop()
                    print(expression)
                return expression    

if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))    
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))