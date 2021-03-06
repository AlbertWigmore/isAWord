import enchant
import itertools

d = enchant.Dict("en_GB")
_check = d.check


def my_check(s):
    if len(s) == 1:
        return s in {"a", "A", "I"}
    return _check(s)
d.check = my_check


def word_sieve(s):
    k = 0
    s += "$"
    solns = [[s]]
    for _, soln in enumerate(solns):
        for j in range(1, 1 + len(soln[-1])):  # Plus 1 fix if for soln[0:j]
            k += 1
            if d.check(soln[-1][0:j]):
                solns.append(soln[:-1] + [soln[-1][0:j], soln[-1][j:]])
    return [x[:-1] for x in solns if x[-1] == "$"]


def brute_force(s):
    words = []
    for i, j in itertools.combinations(xrange(len(s) + 1), 2):
        if d.check(s[i:j]):
            words.append((s[i:j], i, j))
    print words
    tmp_solns = [[x] for x in words if x[:][1] == 0]

    for i, j in enumerate(tmp_solns):
        tmp = [x for x in words if x[:][1] == j[-1][2]]
        for k in tmp:
            tmp_solns.append(j + [k])

    solns = []
    for x in tmp_solns:
        if x[-1][2] == len(s):
            solns.append(x)

    return solns


if __name__ == "__main__":
    string = open("data.txt").read().replace(" ", "").replace("\n", "")
    original = open("data.txt").read().replace("\n", "")

    brute_force(string)  # Method 1: Brute force method checks all substrings
    word_sieve(string)  # Method 2: Checks all prefixes of the string for words
