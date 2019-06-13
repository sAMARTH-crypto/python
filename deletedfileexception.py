import os

if os.path.exists('sample2.txt'):
   data = open('sample2.txt')
   for each_line in data:
      
      if not each_line.find(':') == -1:
          (role, line_spoken) = each_line.split(':', 1)
          print(role, end='')
          print(' said: ', end='')
          print(line_spoken, end='')
   data.close() 
else:
    print('file is missing')
