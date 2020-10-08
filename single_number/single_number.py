'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    wrong_numbers = []
    # loop through the given array
    for i in range(len(arr)):
        for x in range(i + 1, len(arr)):
            if arr[i] == arr[x]:
                wrong_numbers.append(arr[i])
    return arr[i]

                


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")