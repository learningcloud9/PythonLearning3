#!/usr/bin/python3

# variables

mySet_int = {0,1,2,3};
mySet_string = {'a','b','c'};
mySet_mixed = {0,'a',1,'b'};

# working
print();
print("My Set INT ", mySet_int, "  which has type of ", type(mySet_int));
print("My Set String ", mySet_string, "  which has type of ", type(mySet_string));
print("My Set Mixed ", mySet_mixed, "  which has type of ", type(mySet_mixed));


# Iterate
print();
for x in mySet_mixed:
    # since it is not indexed, we cann't call the index value
    print(x);

# ADD
print();
mySet_mixed.add(100);
print("ADD -> ", mySet_mixed);

# POP
print();
mySet_mixed.pop();
print("POP -> ", mySet_mixed);

# REMOVE
print();
mySet_mixed.remove('a');
print("REMOVE -> ", mySet_mixed);