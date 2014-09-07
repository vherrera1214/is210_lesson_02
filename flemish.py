#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FISHY = inquisition.SPANISH.replace('surprise', 'haddock')

RE = 'Spanish'

FLEMISH = FISHY[: FISHY.index(RE)] + 'Flemish' + FISHY[FISHY.index(RE) + len(RE):]

print FLEMISH
