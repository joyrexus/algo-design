from match import Matcher

# the men and their list of ordered spousal preferences
M = {
  'm1': ["w1", "w2", "w3"],
  'm2': ["w1", "w3", "w2"],
  'm3': ["w2", "w1", "w3"]
}

# the women and their list of ordered spousal preferences
W = {
  'w1': ["m3", "m2", "m1"],
  'w2': ["m2", "m1", "m3"],
  'w3': ["m2", "m1", "m3"]
}

# check if a mapping of wives to husbands is stable
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

# initialize Matcher with preference lists for both men and women
match = Matcher(M, W)

# match men and women; returns a mapping of wives to husbands
wives = match()
assert match.is_stable()            # should be a stable matching
assert wives['w1'] is 'm3'          # `w1` is married to `m3`

# now change prefs of woman `w1` and rematch
W['w1'] = ["m3", "m1", "m2"]

# re-initialize Matcher with revised preference lists
match = Matcher(M, W)
wives = match()
assert match.is_stable()            # should be a stable matching
assert wives['w1'] is 'm1'          # but `w1` is now married to `m1`
