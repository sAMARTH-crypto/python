#nums = [2,7,11,15]
#target = 9

def twosum(self,nums,target):
    
    comMap = dict()       #currently dictionary is empty.
    
    for i in range(len(nums)):  #itterating over list
    
        num = nums[i]
        
        com = target - num   #1st itteration com=7,i=0
                              #2nd itteration com=2,i=1 
        
        if num in comMap:
        
            return [comMap[num],i]  
            
        else:
        
            comMap[com] = i   #cmap updated with key,val pair (7,0)
            
            
     #output
     
     [0,1]
