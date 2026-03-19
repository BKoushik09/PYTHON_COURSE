#LIST COMPREHENSION
'''every list comprehension can be re written as a for loop, but every for loop cannot be re written in list comprehension '''
#syntax: [expression   for    var    in    collection/range]
'''a = ['koushik', 'python', 'course']
b = [i.upper() for i in a]
print(b)'''

#EXAMPLE-1
'''a = ['python', 'java', 'ml']
print([i.capitalize() for i in a])'''

#EXAMPLE-2
'''a = [1, 2, 3, 5, 6, 8,12, 13]
#print([i**2 for i in a])
#print([i*i for i in a])
print([pow(i,2)  for i in a])'''

#EXAMPLE-3
'''a = [i for i in range(16) if i%2==0]
print(a)'''

#EXAMPLE-4
'''print([i*i for i in range(16) if i%2==0])  ''' 

#EXAMPLE-5
'''fruits = ['apple', 'grapes', 'mango', 'banana', 'berry', 'kiwi', 'dragon']
print([i for i in fruits if 'a' in i])'''

#EXAMPLE-6
'''print([i*i if i%2==0 else i*5 for i in range(21)])'''

#EXAMPLE-7
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
print([a[i]+b[i] for i in range(len(a))])
print([a[i]+b[i] for i in range(5)])
