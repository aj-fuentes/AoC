import sys


def read_nums(line, s=" "):
    return list(map(int, line.strip().replace(s + s, s).split(s)))


def read_boards(info):
    for k in range((len(info) - 2) // 6):
        board = [read_nums(info[2 + k * 6 + i]) for i in range(5)]
        yield board


def get_res(nums, rinfos, cinfos):
    wons = set()
    for n in nums:
        for k, xinfos in enumerate(zip(rinfos, cinfos)):
            if k in wons:
                continue
            for xinfo in xinfos:
                for i in range(5):
                    if n in xinfo[i]["vals"]:
                        xinfo[i]["vals"].remove(n)
                        if not xinfo[i]["vals"]:
                            wons.add(k)
                            yield sum(b for a in xinfo for b in a["vals"]) * n


info = open(sys.argv[1], "rt").read().split("\n")
nums = read_nums(info[0], ",")
boards = list(read_boards(info))
rinfos = [[{"won": False, "vals": set(r)} for r in b] for b in boards]
cinfos = [[{"won": False, "vals": {r[i] for r in b}} for i in range(5)] for b in boards]

sols = list(get_res(nums, rinfos, cinfos))

print(sols[0])
print(sols[-1])
