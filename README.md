This code takes as input a query string (ex: aa,abc,bc). Split it by comma and put the result in a list and  comare it using the class SparseArray in the SparseArray.py file  to an 

environment variable called STRINGS (ex :aa,abc,bd), determine how many times the items of the query strings occurs in the list of STRINGS . Return a python dictionary of the results.

Example:

STRINGS = ab,ab,abc,dd

Query = ab,abc,bc

Result={ab: 2, abc: 1, bc: 0}

To use this code you have to create an image with the Dockerfile provided using :

docker build –t test_mdm .

then run a container with the command :

docker run –t test_mdm ab,abc,bd

where ab,abc,bd is the Query.

If you wish to change the environment variable use:

docker run –e STRINGS=ab,abc,bc –t test_mdm ab,abc,bd

