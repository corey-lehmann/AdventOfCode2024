import numpy as np
data = np.array(np.loadtxt(r'AdventOfCode2024/Day1Input.txt'))
list1 = np.sort(data[:, 0])
list2 = np.sort(data[:, 1])
diff_list = np.abs(list1-list2)
total_diff = np.sum(diff_list)
print(f'Part 1 solution: {total_diff:.0f}')

total_similarity = 0
for i in list1:
    total_counts = np.sum(list2==i)
    similarity_score = i*total_counts
    total_similarity += similarity_score
print(f'Part 2 solution: {total_similarity:.0f}')


