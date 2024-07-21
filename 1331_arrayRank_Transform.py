def arrayRankTransform(arr: list[int]) -> list[int]:
    sorted_arr = sorted(arr)
    rank = {}

    for i in sorted_arr:
        rank.setdefault(i, len(rank) + 1)

    return list(map(rank.get, arr))


arr1 = [40,10,20,30]
arr2 = [100,100,100]
arr3 = [37,12,28,9,100,56,80,5,12]
print(arrayRankTransform(arr2))
        