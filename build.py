def solution(dic):
    newdict = dict(sorted(dic.items()))
    return newdict.keys()

print solution({1: 10, 4: 40, 2: 20, 3: 30})
