def f(arr):
    valid = []
    counter = 0
    for element in arr:
        if len(element) >= 4 and len(element) <= 12:
            for char in element:
                if char.isdigit() or char == "_":
                    valid.append(element)
            
    
    return len(set(valid))


print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))
