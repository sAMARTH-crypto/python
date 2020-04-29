#Detect Valid Parens

#Basically this program is working on concept of STACK

class Solution(object):
    def isValid(self, s):
        
        pastParens = []  #this empty list is working as a stack to which o-parens wil be appended
        
        for i in range(len(s)):      #iterating through the input
            
            if self.isOpenParen(s[i]):            #if we encounter the open paren append it to stack i.e list
                pastParens.append(s[i])
                
            else:
                
                if len(pastParens) == 0:          #if stack is empty return false
                    return False
                op = pastParens.pop()             #if not adn encounter l-paren start poping out  
                cl = s[i]
                isValid = self.parensIsSameType(op,cl)        #comparing
                
                if not isValid:
                    return False
        return len(pastParens) == 0
    
    def isOpenParen(self,p):
        if p == '(' or p == '[' or p == '{':        #open parens function
            return True
        return False
    
    def parensIsSameType(self,op,cl):               #matching o&c parens
        if op =='(' and cl == ')':
            return True
        elif op == '[' and cl == ']':
            return True
        elif op == '{' and cl == '}':
            return True 
        else:
            return False
