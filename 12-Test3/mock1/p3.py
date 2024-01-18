# (p3.py) The uid array contains user IDs in one of the popular websites. Identifiers should be unique. Create a function f(uid) 
# that returns true if all ids are unique. Otherwise, the function returns false. 
# Example:
# f(["john5","ann123","JOHN5","xxx","abc333","a10"])  True

def f(uid):
    lista = uid
    my_set = set(lista)
    return len(lista) == len(my_set)



print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
