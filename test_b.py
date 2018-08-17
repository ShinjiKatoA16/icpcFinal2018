#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

program = 'prob_b.py'
testdir = 'icpc2018data/B-comma/'
files = os.listdir(testdir)

for f in files:
    if f[-3:] == '.in':
        print('testing', f)
        os.system('python3 '+program+' < '+testdir+f+'>xxx')
        os.system('diff xxx '+testdir+f[:-2]+'ans')
