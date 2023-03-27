class Node:
     def __init__(self,x,y) -> None:
          self.element = x
          self.next = y
class LinkedList:
     def __init__(self,arr) -> None:
          self.head = Node(arr[0],None)
          tail = self.head
          i = 1
          while i<len(arr):
               n = Node(arr[i],None)
               
          


class Stack:
    def __init__(self) -> None:
        # self.exp = exp
        self.stack = []
        self.top = -1
    
        
    def push(self,itm,idx):
        self.stack.append([itm,idx])
        self.top +=1

    def pop(self):
        self.stack.pop()
        self.top -= 1
    
    
    def peek(self):
        return self.stack[self.top][0]
    

    def parenthesisBalancing(self,exp):
    
        count = 1
        for i in exp:
            if i == "(" or i == "[" or i == "{":
                self.push(i,count)
            elif i == ")":
                if len(self.stack) == 0:
                        return f'Error at character # {count}. ")"- not opened.'
                elif self.peek() == "(":
                    self.pop()
                    
                else:
                    return f'Error at character # {self.stack[self.top][-1]}. "("- not closed.'
            elif i == "}":
                if len(self.stack) == 0:
                        return f'Error at character # {count}.'+ '"}"- not opened.'
                elif self.peek() != "{":
                        return f'Error at character # {self.stack[self.top][-1]}.'+'"{"- not closed.'
                else:
                    self.pop()
            elif i == "]":
                if len(self.stack) == 0:
                        return f'Error at character # {count}. "]"- not opened.'
                elif self.peek() != "[":
                        return f'Error at character # {self.stack[self.top][-1]}. "["- not closed.'
                else:
                    self.pop()
                    
            count += 1
        return "This expression is correct."
    


        


exp = "1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"


x = Stack()
z = x.parenthesisBalancing(exp)
print(z)
