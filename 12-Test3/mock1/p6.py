# (p6.py) Assume that a valid variable name in a computer program consists of one to five characters. 
# The first character of a variable name must be a lowercase or uppercase letter or an underscore. 
# The remaining characters in the variable name can be uppercase or lowercase letters, digits or the underscore character. 
# Create a function f(vname) that returns true if the variable name vname is valid. Otherwise, the function returns false. 
# Example:
# f("abc") -> True
# f("Abc") -> True
# f("aBC") -> True
# f("_ab_c") -> True
# f("abcdef") -> False

def f(vname):
    counter = 0
    if len(vname) >= 1 and len(vname) <= 5:
        for char in vname:
            if char.isalpha() or char.isnumeric() or char == "_":
                continue
            else:
                counter += 1
        if counter >= 1:
            return False
        if vname[0].isalpha() or vname[0] == "_":
            return True
        else:
            return False
    else:
        return False

    


print(f("abc"))
print(f("Abc"))
print(f("aBc"))
print(f("_ab_c"))
print(f("abcdef"))
print(f("8abc"))
print(f("_aB8_"))
print(f("_4x"))
print(f("as!"))