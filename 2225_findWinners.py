from collections import Counter


def findWinners(matches: list[list[int]]) -> list[list[int]]:
    win =[]
    lose = []

    no_lose = []
    one_lose = []

    for [w, l] in matches: #Creating a dicts with winners and losers
        win.append(w)
        lose.append(l)
    count_l = Counter(lose)
    count_w = Counter(win)
    for key, value in count_l.items(): #Finding players with 1ose and add them to list
        if value == 1:
            one_lose.append(key)
    for key in count_w:
        if key not in count_l.keys(): #Finding players with no loses and add then to list
            no_lose.append(key)
    no_lose.sort()
    one_lose.sort()
    return [no_lose, one_lose]

matches_1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
matches_2 = [[2,3],[1,3],[5,4],[6,4]]

print(findWinners(matches_1))
print(findWinners(matches_2))