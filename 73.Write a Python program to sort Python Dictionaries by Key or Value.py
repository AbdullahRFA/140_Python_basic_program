# Sorting a dictionary by key and value

# Sample dictionary
data = {
    'banana': 3,
    'apple': 5,
    'cherry': 1,
    'mango': 4
}

# ✅ Sorting by Key (Alphabetically)
sorted_by_key = dict(sorted(data.items()))

# ✅ Sorting by Value (Ascending)
sorted_by_value = dict(sorted(data.items(), key=lambda item: item[1]))

# ✅ Sorting by Value (Descending)
sorted_by_value_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

# Printing Results
print("Original Dictionary:", data)
print("Sorted by Key:", sorted_by_key)
print("Sorted by Value (Ascending):", sorted_by_value)
print("Sorted by Value (Descending):", sorted_by_value_desc)