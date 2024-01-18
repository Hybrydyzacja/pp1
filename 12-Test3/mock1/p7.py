# (p7.py) Create a function f(arr2D) that returns true when the sum of the values in at least two columns is the same.
# Otherwise, the function returns false.
# Example:
# arr = [[3,4,2],[2,2,2,0],[5,0,0,5],[4,7,0,2],[0,2,0,0]]
# f([[3,4,2],[5,1,6]]) -> True
# f([[3,4,2],[5,1,7]]) -> False
# f([[3,4],[5,1],[4,7]]) -> True
# f([[3,4],[5,9],[4,7]]) -> False


def f(arr2D):
    sumy = []
    for i in range(len(arr2D)):
        suma = sum(arr2D[i])
        sumy.append(suma)
    return sumy

 

print(f([[3, 4, 2], [5, 1, 6]]))
print(f([[3, 4, 2], [5, 1, 7]]))
print(f([[3, 4], [5, 1], [4, 7]]))
print(f([[3, 4], [5, 9], [4, 7]]))
