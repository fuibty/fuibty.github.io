
# To compile run
#   python setup.py build_ext --inplace


def find(list rule_init, int L):

    cdef list P
    cdef int new
    cdef int rule[4][24]
    for i in range(4):
        for j in range(24):
            rule[i][j] = rule_init[i][j]


    if L == 1:
        return [[0]]
    else:
        patterns = []
        prev_patterns = find(rule,L-1)
        for i in range(len(prev_patterns)):
            P = prev_patterns[i]
            for j in range(4):
                new = rule[j][P[-1]]
                if not (new in P):
                    patterns.append(P+[new])
        return patterns


