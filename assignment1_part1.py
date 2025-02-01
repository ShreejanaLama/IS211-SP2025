# assignment1_part1.py

# Custom exception class
class ListDivideException(Exception):
    pass

# Function to count numbers divisible by 'divide'
def list_divide(numbers, divide=2):
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1
    return count

# Function to test list_divide
def test_list_divide():
    # Test case 1
    result = list_divide([1, 2, 3, 4, 5])
    if result != 2:
        raise ListDivideException("Test 1 Failed")
    
    # Test case 2
    result = list_divide([2, 4, 6, 8, 10])
    if result != 5:
        raise ListDivideException("Test 2 Failed")
    
    # Test case 3
    result = list_divide([30, 54, 63, 98, 100], divide=10)
    if result != 2:
        raise ListDivideException("Test 3 Failed")
    
    # Test case 4
    result = list_divide([])
    if result != 0:
        raise ListDivideException("Test 4 Failed")
    
    # Test case 5
    result = list_divide([1, 2, 3, 4, 5], 1)
    if result != 5:
        raise ListDivideException("Test 5 Failed")

# Running the test
try:
    test_list_divide()
    print("All tests passed successfully.")
except ListDivideException as e:
    print(f"An error occurred: {e}")
