def find_smallest_greater_number(num):
    # Convert the number to a list of digits
    digits = list(str(num))
   
    # Find the first digit from the right that is smaller than its right neighbor
    pivot_index = -1
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i+1]:
            pivot_index = i
            break
   
    # If no such digit is found, return -1 indicating it's not possible
    if pivot_index == -1:
        return -1
   
    # Find the smallest digit to the right of the pivot index that is greater than the pivot
    smallest_greater_index = pivot_index + 1
    for i in range(pivot_index + 1, len(digits)):
        if digits[i] > digits[pivot_index] and digits[i] < digits[smallest_greater_index]:
            smallest_greater_index = i
   
    # Swap the pivot with the smallest greater digit
    digits[pivot_index], digits[smallest_greater_index] = digits[smallest_greater_index], digits[pivot_index]
   
    # Sort the digits to the right of the pivot in ascending order
    digits[pivot_index + 1:] = sorted(digits[pivot_index + 1:])
   
    # Convert the list of digits back to a number
    result = int("".join(digits))
    return result

# Example usage
given_number = 155
smallest_greater_number = find_smallest_greater_number(given_number)

if smallest_greater_number == -1:
    print("No greater number with the same set of digits found.")
else:
    print(f"The smallest number greater than {given_number} with the same set of digits is {smallest_greater_number}.")
