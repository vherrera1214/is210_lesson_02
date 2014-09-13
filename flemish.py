#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FISHY = inquisition.SPANISH.replace('surprise', 'haddock')

R = 'Spanish'

FLEMISH = FISHY[: FISHY.index(R)] + 'Flemish' + FISHY[FISHY.index(R) + len(R):]

print FLEMISH
