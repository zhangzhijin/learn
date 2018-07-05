import os
'''
this is file
'''
def fun1():
    """this is a fun
    """
    print("a")
print(__doc__)
print(__file__)
print(os.path.basename(__file__) )

print(dir(__builtins__))
# print(vars())