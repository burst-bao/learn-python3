#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])

# -*- coding: utf-8 -*-
def trim(s):
    l=len(s)
    while(True):      #先清除掉后面的，再递归，在清除掉前面的
        if s[-1:]!=' ':
            s=s[:]
            break
        elif s[-1:]==' ':
            s=s[:l-1]
            return trim(s)
    while(True):
        if s[:1]!=' ':
            s=s[:]
            break
        elif s[:1]==' ':
            s=s[-l+1:]
            return trim(s)
return s
