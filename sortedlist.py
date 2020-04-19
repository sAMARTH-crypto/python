#merge two sorted list

class Solution:
    def mergeTwoLists(self,l1,l2):  
    
        head = ListNode(0)  #starting point
        ptr = head
        
                 
        while True:
            
            if l1 is None and l2 is None: #both list are empty break
                break
            elif l1 is None:  #list-1 is empty return list-2
                ptr.next = l2
                break
            elif l2 is None:  #list-2 is empty return list-1
                ptr.next = l1
                break
            else:
                smallerVal = 0  
                
                if l1.val < l2.val:  #comparing the values of the list 
                    
                    smallerVal = l1.val #update the value
                    l1 = l1.next        #move pointer ahead
                    
                else:
              
              
                    smallerVal = l2.val  #update value
                    l2 = l2.next         #move pointer ahead
                    
                newNode = ListNode(smallerVal) 
                ptr.next = newNode
                ptr = ptr.next   
                
        return head.next
