#filter()
'''a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(lambda x:x%2==0,a))
print(b)'''

'''a = (1,2,3,4,5,6,7,8,9,10)
b = tuple(filter(lambda x:x%2==0,a))
print(b)'''

'''a = [[], {}, set(), " ", (), None, 9, 9.11, 'koushik', 9+11j, True, False]
b = list(filter(None,a))
print(b)'''


#map()->each object from a collection and form a new collection
a = [100,5,7,8,15,20,40,100,98]
b=[4,6,12,25,40,80,35,1,98]
c = list(map(max,a,b))
d = list(map(min,a,b))
print(c)
print(d)

