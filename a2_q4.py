def a2_q4(values):
    sorted_values = sorted(values) 
    n = len(sorted_values)
    target_sum = sum(sorted_values) / 2  

    group1 = []
    group2 = []

    for val in sorted_values:
        if sum(group1) < target_sum:
            group1.append(val)
        else:
            group2.append(val)

    diff = abs(sum(group1) - sum(group2))

    return {"group1": group1, "group2": group2, "diff": diff}

print(a2_q4([1, 2, 3, 4, 5, 6, 7, 8]))