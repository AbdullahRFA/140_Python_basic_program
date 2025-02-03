# Enter distance in kilometers: 100
# 100.0 kilometers is equal to 62.137100000000004 miles
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")
