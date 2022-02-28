#!/usr/bin/python3
import timeit;

myList = ['apple','mango','banana','kiwi','plum', 'cherry'];


# Normal Use User

# Example - to create another list which is starting from 'a'

myCustomList_normal = [];
startNormal = timeit.default_timer();
for x in myList:
    if 'a' in x:
        myCustomList_normal.append(x);
stopNormal = timeit.default_timer();
print();
print("My Original List ",myList);
print("My Custom List ",myCustomList_normal);
print("Total Run Time is ", (stopNormal-startNormal));


# List Compehension
startComprehension = timeit.default_timer();
myCustomList_comprehension = [x for x in myList if 'a' in x];
stopComprehension = timeit.default_timer();
print();
print("My Original List ",myList);
print("My Custom List ",myCustomList_comprehension);
print("Total Run Time is ", (stopComprehension-startComprehension));
