#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


THE_GREAT_QUESTION = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '
                      'Creators of the great works? Both? You be the judge!')

STATEMENTS = THE_GREAT_QUESTION.split('. ')

print STATEMENTS

ARTISTS = STATEMENTS[:4]

print ARTISTS

NUM_ARTISTS = len(ARTISTS)

print NUM_ARTISTS

CHARACTERS = len(THE_GREAT_QUESTION)

print CHARACTERS
