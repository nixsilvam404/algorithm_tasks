def uniqueOccurrences(arr: list[int]) -> bool:
    hash_map = {}
    for i in arr:
        hash_map[i] = hash_map.get(i, 0) + 1
    return len(hash_map.values()) == len(set(hash_map.values()))


print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1, 2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))