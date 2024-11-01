#!/usr/bin/python3

# variable
myDictionary_int = {"key0":0, "key1":1, "key2":2};
myDictionary_string = {"key0":'a', "key1":'b', "key2":'c'};
myDictionary_mixed = {"key0":0, "key1":'a', "key2":'b'};

# Advance variable

myDictionary_advance = {"key0":0, "key1":'a', "key2": [0,1,'a']};

# working
print();
print("My Dictionary INT ", myDictionary_int, "  which has type of ", type(myDictionary_int));
print("My Dictionary String ", myDictionary_string, "  which has type of ", type(myDictionary_string));
print("My Dictionary Mixed ", myDictionary_mixed, "  which has type of ", type(myDictionary_mixed));


# Iterate
print();
for x in myDictionary_advance:
    print("value of x is - ",x);

# Advance Iterate
# Example 1
print();
for x in myDictionary_advance:
    print("key ",x, "has value of ", myDictionary_advance[x]);

# Example 2
print();
for key, value in myDictionary_advance.items():
    print("key - ",key," has value of ",value);

# ITEMS
print();
print("items()  ->", myDictionary_advance.items());

d = {'a':Exception}
print(d)
myString = str(d['a'])
print(type(myString))
#print(myString[0,5])