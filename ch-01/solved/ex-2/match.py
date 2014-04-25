import random

# the men and their list of ordered spousal preferences
M = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('men.txt')))

# the women and their list of ordered spousal preferences
W = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('women.txt')))

# for each man construct a random list of forbidden wives
forbidden = {}      # { 'dan': ['gay', 'eve', 'abi'], 'hal': ['eve'] }
for m, prefs in M.items():
    randrange = range(random.randint(0, len(prefs) - 1))
    forbidden[m] = [random.choice(prefs) for i in randrange]

# test whether w prefers m over h
def prefers(w, m, h):
    return W[w].index(m) < W[w].index(h)

# return the woman favored by m after w
def after(m, w):
    prefs = M[m]                    # m's ordered list of preferences
    i = prefs.index(w) + 1          # index of woman following w in list of prefs
    if i >= len(prefs):
        return ''                   # no more women left!
    w = prefs[i]                    # woman following w in list of prefs
    if w in forbidden.get(m, []):   # get next woman if (m, w) is forbidden
        return after(m, w)
    return w

# try to match all men with their next preferred spouse
def match(men, next={}, wives={}):
    if not len(men): return wives
    m, men = men[0], men[1:]
    w = next[m]                     # next woman for m to propose to
    if not w:                       # continue if no woman to propose to
        return match(men, next, wives)
    next[m] = after(m, w)           # woman after w in m's list of prefs
    if w in wives:
        h = wives[w]                # current husband
        if prefers(w, m, h):
            men.append(h)           # husband becomes available again
            wives[w] = m            # w becomes wife of m
        else:
            men.append(m)           # m remains unmarried
    else:
        wives[w] = m                # w becomes wife of m
    return match(men, next, wives)
