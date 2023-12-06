# Write a python program to
# - Find the sum and average of given numbers using lists
# - Display elements of list in reverse order
# - Find the minimum and maximum elements in the lists

inp = input("Enter numbers separated by space: ").split(" ")
nums = list(map(lambda x: int(x), inp))

print(f"- Sum: {sum(nums)}")
print(f"- Average: {sum(nums) / len(nums)}")

print("- Reversed:", end=" ")
for i in range(len(nums) - 1, -1, -1):
    print(nums[i], end=" ")
print()

print(f"- Minimum: {min(nums)}")
print(f"- Maximum: {max(nums)}")
