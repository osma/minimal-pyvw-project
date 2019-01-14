#!/usr/bin/env python

# Minimal example script that uses the Vowpal Wabbit Python bindings
# Adapted from https://pypi.org/project/vowpalwabbit/

from vowpalwabbit import pyvw

vw = pyvw.vw(quiet=True)
ex = vw.example('1 | a b c')
vw.learn(ex)
print(vw.predict(ex))
