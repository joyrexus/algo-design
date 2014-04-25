import random
from match import Matcher


# the men and their list of ordered spousal preferences
M = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('men.txt')))

# the women and their list of ordered spousal preferences
W = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('women.txt')))

# for each man construct a random list of forbidden wives
forbidden = {}      # { 'dan': ['gay', 'eve', 'abi'], 'hal': ['eve'] }
for m, prefs in M.items():
    n = random.randint(0, len(prefs) - 1)
    forbidden[m] = random.sample(prefs, n)  # random sample of n wives

match = Matcher(M, W, forbidden)

# match men and women; returns a mapping of wives to husbands
wives = match()

assert match.is_stable(wives)           # should be a stable matching

# swap the husbands of two wives, which should make the matching unstable
a, b = random.sample(wives.keys(), 2)
wives[b], wives[a] = wives[a], wives[b]

match.is_stable(wives, verbose=True)

