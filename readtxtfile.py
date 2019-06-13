import os

os.getcwd()
'''
#code to open a txt file
data = open('sample.txt')
print(data.readline(), end=' ')
'''

data = open('sample2.txt')
for each_line in data:
    try:
        '''code which causes error '''
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
    except:
        '''error recovery code '''
        pass
data.close()
