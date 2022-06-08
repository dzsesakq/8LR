#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    def getInput(): return(input('запрашиваю ввод: '))
    def testInput(n):
        try: n = int(n); return(True)
        except: return(False)
    def strToInt(n): return(int(n))
    def printInt(n): print(n)