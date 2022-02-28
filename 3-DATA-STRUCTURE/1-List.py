#!/usr/bin/python3


# variable
myList_int = [0, 1, 2, 3, 1];
myList_string = ['a', 'b', 'c', 'a'];
myList_mixed = [0, 'a', 1, 'b', 0];

# Working
print();
print("My List INT ", myList_int, "  which has type of ", type(myList_int));
print("My List String ", myList_string, "  which has type of ", type(myList_string));
print("My List Mixed ", myList_mixed, "  which has type of ", type(myList_mixed));

# Iterate
print();
for x in range(len(myList_mixed)):
    print("value at index ", x , " is ", myList_mixed[x]);

# Add new variable
print();
myList_mixed.append(10);
print(myList_mixed);
