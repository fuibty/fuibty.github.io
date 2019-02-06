#from libcpp.vector cimport vector


# To compile run
#   python setup.py build_ext --inplace


def find(list rule_init,int n):

    print('Looking for patterns ...')
    print('Counting to 1')


    cdef int s
    cdef int choice
    cdef int temp
    cdef int new
    cdef bint broken
    cdef list P
    cdef int r[4][3]
    cdef int rule[4][24]

    for i in range(4):
        for j in range(24):
            rule[i][j] = rule_init[i][j]

    s = 0

    patterns = []

    r =\
        [
         [1,2,3]
        ,[0,2,3]
        ,[0,1,3]
        ,[0,1,2]
        ]

    for i in range(4):
        for j in range(3**(n-2)):
            P = [s,rule[i][s]]
            choice = i
            broken = False
            for k in range(n-2):
                temp = choice
                choice = j%3
                j = j//3
                new = rule[r[temp][choice]][P[-1]]
                if new in P:
                    broken = True
                    break
                P.append(new)
            if not broken:
                if P[-1] > 19:
                    patterns.append(P)
        print('%d/4' % (i+1))
    return patterns

