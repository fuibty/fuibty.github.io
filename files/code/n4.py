# coding=utf-8
from math import factorial as fct
import time
import sys

# comment if you don't want to use cython
#from findN4 import find

# modified aliasN4.py ++++ {{{

def permutations(s):
    """Permutations of a string"""
    p = []
    if len(s) > 1:
        e = s[0]
        r = s[1:]
        var = permutations(r)
        for i in range(len(var)):
            for j in range(len(var[i])):
                p.append(var[i][0:j]+e+var[i][j:])
            p.append(var[i]+e)
        return p
    else:
        return [s]

def rule0(s):
    return s[1] + s[0] + s[2:]
def rule1(s):
    return s[0] + s[2] + s[1] + s[3]
def rule2(s):
    return s[:2] + s[3] + s[2]
def rule3(s):
    return s[1] + s[0] + s[3] + s[2]

#permList = permutations('1234')

# Triks {{{
# 0:'1234'
# ...
# ...
# 20:'2134'
# 21:'1324'
# 22:'1243'
# 23:'2143'
#
#if new > 19:
#   patterns.append(P)
#
permList =\
    [
    '1234'
    ,'1423'
    ,'4123'
    ,'1432'
    ,'4132'
    ,'4312'
    ,'3421'
    ,'3241'
    ,'2314'
    ,'3214'
    ,'2341'
    ,'2431'
    ,'4213'
    ,'2413'
    ,'4231'
    ,'4321'
    ,'3412'
    ,'3142'
    ,'1342'
    ,'3124'
    ,'1324'
    ,'2134'
    ,'2143'
    ,'1243'
    ]
# }}}

toStr = {}
toNum = {}
for i in range(len(permList)):
    toStr[i]=permList[i]
    toNum[permList[i]] = i

rule_S = {
         0:rule0
        ,1:rule1
        ,2:rule2
        ,3:rule3
        }

#rule = [
#         [0 for i in range(24)]
#        ,[0 for i in range(24)]
#        ,[0 for i in range(24)]
#        ,[0 for i in range(24)]
#       ]

# which yields the same as
rule = []
for i in range(4):
    rule.append([0 for j in range(24)])


for i in range(4):
    for j in range(24):
        rule[i][j] = toNum[rule_S[i](toStr[j])]

#print(rule[0]) #print(rule[1])
#print(rule[2])
#print(rule[3])
#sys.exit()


#oneAway =
#    [
#     rule[0][0]
#    ,rule[1][0]
#    ,rule[2][0]
#    ,rule[3][0]
#    ]

# which yields the same as
oneAway = []
for i in range(4):
    oneAway.append(rule[i][0])

# }}}
def timeStr(t): # {{{
    secs = t%60
    t = t//60
    mins = t%60
    t = t//60
    hours = t%24
    days = t//24
    ddd = ' '
    hhh = ' '
    mmm = ' '
    sss = ' '
    if days >= 2:
        ddd = 's'
    if hours >= 2:
        hhh = 's'
    if mins >= 2:
        mmm = 's'
    if secs >= 2:
        sss = 's'
    D = '%3d day%s' % (days,ddd)
    H = '%2d hour%s' % (hours,hhh)
    M = '%2d minute%s' % (mins,mmm)
    S = '%5.2f second%s' % (secs,sss)
    return '%s  %s  %s  %s' % (D,H,M,S)

def printResult(t,nr):
    CR = '%d change ringing patterns' % nr
    print('We found %s in\n\n%s' % (CR,timeStr(t)))
# }}}


n = int(sys.argv[1])


# uncomment if you don't want to use cython

#def find(L):
#    if L == 1:
#        return [[0]]
#    else:
#        patterns = []
#        prev_patterns = find(L-1)
#        for i in range(len(prev_patterns)):
#            P = prev_patterns[i]
#            for j in range(4):
#                new = rule[j][P[-1]]
#                if not (new in P):
#                    patterns.append(P+[new])
#        return patterns


t0 = time.process_time()

partial_patterns = find(rule,n)
#partial_patterns = find(n)

t1 = time.process_time()

patterns = []
m = len(partial_patterns)
for i in range(m):
    if partial_patterns[i][-1] > 19:
        patterns.append(partial_patterns[i])

t2 = time.process_time()

t = t1-t0

print('DONE.\n')
count = len(patterns)
printResult(t,count)

f = open('change4_%d.txt' % n,'w')
f.write('Number of patterns = ' + str(count) + '\n\n')

for pattern in patterns:
    for nr in pattern:
        f.write(toStr[nr]+'\n')
    f.write('1234\n')
    f.write('\n')
f.close()


