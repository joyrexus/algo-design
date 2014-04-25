class Matcher:

    def __init__(self, men, women):
        '''
        Constructs a Matcher instance.

        Takes a dict of men's spousal preferences, `men`,
        and a dict of women's spousal preferences, `women`.

        '''
        self.M = men
        self.W = women
        self.wives = {}
        self.pairs = []

    def __call__(self):
        return self.match()

    def prefers(self, w, m, h):
        'Test whether w prefers m over h.'
        return self.W[w].index(m) < self.W[w].index(h)

    def after(self, m, w):
        'Return the woman favored by m after w.'
        prefs = self.M[m]           # m's ordered list of preferences
        i = prefs.index(w) + 1      # woman following w in list of prefs
        return prefs[i]

    def match(self, men=None, next=None, wives=None):
        'Try to match all men with their next preferred spouse.'
        if men is None: 
            men = self.M.keys()         # get the complete list of men
        if next is None: 
            # if not defined, map each man to their first preference
            next = dict((m, rank[0]) for m, rank in self.M.items()) 
        if wives is None: 
            wives = {}                  # mapping from women to current spouse
        if not len(men): 
            self.pairs = [(h, w) for w, h in wives.items()]
            self.wives = wives
            return wives
        m, men = men[0], men[1:]
        w = next[m]                     # next woman for m to propose to
        next[m] = self.after(m, w)      # woman after w in m's list of prefs
        if w in wives:
            h = wives[w]                # current husband
            if self.prefers(w, m, h):
                men.append(h)           # husband becomes available again
                wives[w] = m            # w becomes wife of m
            else:
                men.append(m)           # m remains unmarried
        else:
            wives[w] = m                # w becomes wife of m
        return self.match(men, next, wives)

    def is_stable(self, wives=None, verbose=False):
        if wives is None:
            wives = self.wives
        for w, m in wives.items():
            i = self.M[m].index(w)
            preferred = self.M[m][:i]
            for p in preferred:
                h = wives[p]
                if self.W[p].index(m) < self.W[p].index(h):  
                    msg = "{}'s marriage to {} is unstable: " + \
                        "{} prefers {} over {} and {} prefers " + \
                        "{} over her current husband {}"
                    if verbose:
                        print msg.format(m, w, m, p, w, p, m, h) 
                    return False
        return True
