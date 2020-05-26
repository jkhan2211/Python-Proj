'''
  1. Calculate XOR of A and B.
        a_xor_b = A ^ B
  2. Count the set bits in the above
     calculated XOR result.
        countSetBits(a_xor_b)

        For exe"
        A = 146 = (1 0 0 *1 *0 0 *1 *0)
        B = 137 = (1 0 0 *0 *1 0 *0 *1)

        Answer = 4
'''


# Count number of bits to be flipped
# to convert A into B

# Function that count set bits
def countSetBits( n ):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count


# Function that return count of
# flipped number
def FlippedCount(a , b):
    # Return count of set bits in
    # a XOR b
    return countSetBits(a^b)


# Driver code
a = 10
b = 20
print(FlippedCount(a, b))

