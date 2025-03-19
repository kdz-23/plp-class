
# Part a. creating an empty list
my_list = []
print(type(my_list)) # <class 'list'>

""" (part b.)
   (Note that i used a for loop to insert the elements into the empty list )
   the for loop will start with a value of 10, and will end with a value of 40(no inluding the last)
   and in each iteration, we have a step size of 10,
   these values will be appended to the list at each iteration
"""
for i in range(10, 50, 10):
    my_list.append(i)   
print (my_list)  
# Output: [10, 20, 30, 40]  

# Part c. inseting the value 15 at the second position
my_list.insert(1, 15) # here, index 1 represents the second position
print (my_list)
# Output: [10, 15, 20, 30, 40]


# Part d. extending my_list with another list: [50, 60, 70]
"""
    extend() function appends all elements of the new list to the end of the existint my_list
"""
my_list.extend([50, 60, 70]) 
print (my_list)
# Output: [10, 15, 20, 30, 40, 50, 60, 70]


# Part e. remove the last element from my_list.
"""
    del keyword is used to delete the element at a specified index
    the index -1 represents the last item in the list
"""
del my_list[-1] 
print (my_list)
# Output: [10, 15, 20, 30, 40, 50, 60]


# Part f. sort my_list in ascending order.
"""
    sort() function sorts the list in ascending order
"""
my_list.sort() 
print (my_list)
# Output: [10, 15, 20, 30, 40, 50, 60]


# Part g. find and print the index of the value 30 in my_list.
"""
    index() function returns the index of the first occurrence of the specified element
"""
index = my_list.index(30) 
print (f'The index of 30 is: {index}')
# Output: The index of 30 is: 3