from match import Matcher


# the men and their list of ordered spousal preferences
M = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('men.txt')))

# the women and their list of ordered spousal preferences
W = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('women.txt')))


# initialize Matcher with preference lists for both men and women
match = Matcher(M, W)

# check if the mapping of wives to husbands is stable
def is_stable(wives, verbose=False):
    for w, m in wives.items():
        i = M[m].index(w)
        preferred = M[m][:i]
        for p in preferred:
            h = wives[p]
            if W[p].index(m) < W[p].index(h):  
                msg = "{}'s marriage to {} is unstable: " + \
                      "{} prefers {} over {} and {} prefers " + \
                      "{} over her current husband {}"
                if verbose:
                    print msg.format(m, w, m, p, w, p, m, h) 
                return False
    return True

# match men and women; returns a mapping of wives to husbands
wives = match()
assert is_stable(wives)             # should be a stable matching
assert match.is_stable()            # should be a stable matching

# swap the husbands of two wives, which should make the matching unstable
wives['fay'], wives['gay'] = wives['gay'], wives['fay']

assert is_stable(wives) is False    # should not be a stable matching

# with the perturbed matching we find that gav's marriage to fay is unstable: 
#
#   * gav prefers gay over fay 
#   * gay prefers gav over her current husband dan
