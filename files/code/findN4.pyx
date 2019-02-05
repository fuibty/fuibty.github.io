#from libcpp.vector cimport vector


# To compile run
#   python setup.py build_ext --inplace


def find(list rule,list oneAway,int n):

    print('Looking for patterns ...')
    print('Counting to 1')


    cdef int s,choice,temp,new
    cdef bint broken
    cdef list patterns
    cdef list P
    cdef list r
    #cdef vector[int] P
    #cdef int[] P
    #cdef vector[list] patterns

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
                #if (new in oneAway):
                if P[-1] > 19:
                    patterns.append(P)
        print('%d/4' % (i+1))
    return patterns
