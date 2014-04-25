from match import match, forbidden, M, W

# check if a mapping of wives to husbands is stable
def is_stable(wives, verbose=False):
    for w, m in wives.items():
        i = M[m].index(w)
        preferred = M[m][:i]
        for p in preferred:
            if p in forbidden.get(m, []):   # no need to worry about 
                continue                    #    forbidden marriages!
            h = wives[p]
            if W[p].index(m) < W[p].index(h):  
                msg = "{}'s marriage to {} is unstable: " + \
                      "{} prefers {} over {} and {} prefers " + \
                      "{} over her current husband {}"
                if verbose:
                    print msg.format(m, w, m, p, w, p, m, h) 
                return False
    return True

# a mapping from men to their top preferences
top = dict((m, rank[0]) for m, rank in M.items()) 

# match men and women; returns a mapping of wives to husbands
wives = match(M.keys(), top)

assert is_stable(wives)             # should be a stable matching

# swap the husbands of two wives, which should make the matching unstable
wives['fay'], wives['gay'] = wives['gay'], wives['fay']

assert is_stable(wives) is False    # should not be a stable matching

# with the perturbed matching we find that gav's marriage to fay is unstable: 
#
#   * gav prefers gay over fay 
#   * gay prefers gav over her current husband dan
