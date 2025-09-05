import time

lst = range(10000)

minimum = None

# O(n^2) algorithm for smallest element
start = time.time()

for element in lst:
    is_min = True
    for other_element in lst:
        if element > other_element:
            is_min = False
    if is_min:
        minimum = element

end = time.time()

print(f"Smallest element is {minimum}. Time taken for O(n2) algorithm: {end - start} seconds")

minimum = lst[0]

# O(n) algorithm for smallest element
start = time.time()

for i in range(1, len(lst)):
    if minimum > lst[i]:
        minimum = lst[i]

end = time.time()

print(f"Smallest element is {minimum}. Time taken for O(n) algorithm: {end - start} seconds")