#Reverse a linked list

class Solution:             #here we are traversing over the linked list using a third var

    def reverseList(self,head):
    
        prev = None         #initially val of prev is none
        
        while head: 
        
            temp = head           #starting point temp = head
            head = head.next      #moving ahead the pointer  
            temp.next = prev      
            prev = temp           #prev is moving in backward direction which in turn will reverse the linked list
                    
        return prev               #return the reversed linked list                  
        
                                          
