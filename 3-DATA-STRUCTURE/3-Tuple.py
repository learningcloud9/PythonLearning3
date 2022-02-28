#!/usr/bin/python3

# variables

myTuple_int = (0,1,2,3,4);
myTuple_string = ('a','b','c','d');
myTuple_mixed = (0,'a',1,'b','a');

# Advance Tuple Variables
myTuple_advance = (0, 'fun', [0,1,2], {'a','b'}, (0,'a'));

# working
print();
print("My Tuple INT ", myTuple_int, "  which has type of ", type(myTuple_int));
print("My Tuple String ", myTuple_string, "  which has type of ", type(myTuple_string));
print("My Tuple Mixed ", myTuple_mixed, "  which has type of ", type(myTuple_mixed));

# Iterate
print();
for x in range(len(myTuple_mixed)):
    print("index at ",x," value is ",myTuple_mixed[x]);

# Iterate Advance
print();
for x in range(len(myTuple_advance)):
    print("Tuple Value is -> ",myTuple_advance[x], " and its type is ", type(myTuple_advance[x]));