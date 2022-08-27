def minimum_window(s, t):
    hash_s, hash_t = {}, {}
    res = []
    # counting the characters in s and t
    for char in s:
        hash_s.update({char: s.count(char)})
    for char in t:
        hash_t.update({char: t.count(char)})
    # returning null if they aren't sufficient characters
    for char, count in hash_t.items():
        if hash_s.get(char, 0) < count:
            return ""
    print(hash_s, hash_t)
    if hash_s == hash_t:
        return t
    # getting the indices of characters in t
    left_val = []
    for i in range(len(s)):
        if s[i] in hash_t:
            left_val.append(i)

    def checker(x, y):
        x, y = list(x), list(y)
        for char in x:
            if char not in y:
                return False
        return True
    # main algorithm
    i = 0
    while i < len(left_val):
        left = left_val[i]
        right = left
        while not checker("".join(hash_t), s[left:right]):
            right += 1
            if right >= len(s):
                break
        if checker("".join(hash_t), s[left:right]):
            res.append(s[left:right])
        i += 1
    # rendering the result
    hash_res = {}
    for potential_res in res:
        hash_res.update({potential_res: len(potential_res)})

    minimum = min(hash_res.values())
    for key, value in hash_res.items():
        if value == minimum:
            return key


# Testing
assert(minimum_window("adobecodebanc", "abc")) == "banc"
assert(minimum_window("a", "a")) == "a"
assert(minimum_window("a", "aa")) == ""
print(minimum_window("adobecodebanc", "abc"))
print(minimum_window("a", "a"))
print(minimum_window("aa", "aa"))
