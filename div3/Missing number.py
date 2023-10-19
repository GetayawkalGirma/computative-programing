def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage:
my_list = [0, 1]
missing = find_missing_number(my_list)

if missing is not None:
    print(f"The missing number in the list is {missing}")
else:
    print("No missing numbers found in the list.")
