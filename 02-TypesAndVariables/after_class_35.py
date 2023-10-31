# 35.	A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the circumference of the tree entered from the keyboard, 
# calculates and displays the value True if the tree can be cut down, or display the value False otherwise. Sample result:
# Enter tree circumference: …
# Tree can be cut down: …

# circumference = int(input("Enter cincumference: "))
# r = circumference / (2 * 3.14)
# diameter = 2 * r
# print(f"Tree can be cut down: {diameter>=50}")

def cut_the_tree(circumference):
    # circumference = 2 * 3,14 * r
    r = circumference / (2 * 3.14)
    diameter = 2 * r
    return(diameter>=50)

print(cut_the_tree(25))