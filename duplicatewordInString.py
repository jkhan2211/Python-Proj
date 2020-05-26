'''
Algorithm
-Use collection and the Counter method to minimize code
'''

from collections import Counter


def find_duplicates(s):
    elements = Counter(s)
    return [k for k, v in elements.items() if v > 1]

print(find_duplicates("Hippojjdkfjsa"))