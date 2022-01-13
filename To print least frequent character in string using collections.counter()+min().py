from collections import Counter

test_str = "mississippi"

print ("The original string is : " + test_str)

res = Counter(test_str)
res = min(res, key = res.get)

print ("The minimum of all characters in mississippi is : " + str(res))