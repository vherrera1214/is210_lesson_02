#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Numeric data tpyes """

FLOATVAR = float(0.1)

import decimal
DECIMALVAR = decimal.Decimal(0.1)

from fractions import Fraction
FRACTIONVAR = Fraction(1, 10)

print (FLOATVAR)

print (DECIMALVAR)

print (FRACTIONVAR)