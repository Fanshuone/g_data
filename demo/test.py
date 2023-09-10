name = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David']
name_sorted = [n for i, n in enumerate(name) if n not in name[:i]]
print(name_sorted)
