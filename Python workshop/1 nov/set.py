mySet={1,2,3,4,5,6,7,"hello",9}
print(mySet)
mySet.add("myNewElement") #add the element in the set
print(mySet)
mySet.remove(5) #will remove the 5 fromm the set(will give error if not present)
mySet.discard(5) #will safely remove the element passes even if it does not exist
print(mySet)

mySet1={15,26,36}
a=mySet.union(mySet1) #will add the elements of the secoong set in first set
print(a)


#SETS OPERATIONS(union(),intersection(),difference(),symmetric_difference())

#function defining

def find_intersection(set1,set2):
    intersection=set1.intersection(set2)
    return intersection
#Example usage
set1={"A","B","C","D"}
set2={"C","D","E","F"}
intersection=find_intersection(set1,set2)
print(intersection)
b=set1.difference(set2)
print(b)
list=[1,2,3,4]
sim=set(list)
print(sim)