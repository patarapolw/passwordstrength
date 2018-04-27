# PasswordStrength

[![Build Status](https://travis-ci.org/patarapolw/passwordstrength.svg?branch=master)](https://travis-ci.org/patarapolw/passwordstrength)
[![Latest Version](https://pypip.in/version/passwordstrength/badge.svg)](https://pypi.python.org/pypi/passwordstrength/)
[![PyPI license](https://img.shields.io/pypi/l/passwordstrength.svg)](https://pypi.python.org/pypi/passwordstrength/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/passwordstrength.svg)](https://pypi.python.org/pypi/passwordstrength/)


Editable password strength calculator for Python.

Update: Add entropy module!

## Entropy

This calculates the ability to tolerate dictionary attack. Probably, an entropy of [2\*\*70](https://pthree.org/2018/04/19/use-a-good-password-generator/) is eventually needed.

```pycon
>>> from passwordstrength.entropy import Entropy
>>> import math
>>> entropy = Entropy()
>>> math.log2(entropy.entropy('asdhaskj'))
39.603517745128734
>>> math.log2(entropy.entropy('hello'))
11.240195053979924
>>> math.log2(entropy.entropy('helloworld'))
49.00439718141092
>>> math.log2(entropy.entropy('@sdhaskj'))
41.54693421676237
>>> math.log2(entropy.entropy('@sQsA$!j'))
48.43376716002963
```

## Password Meter

This is based on http://www.passwordmeter.com

### Usage

```pycon
>>> from passwordstrength.passwordmeter import PasswordStrength
>>> strength = PasswordStrength('password')
>>> strength.strength()
9
>>> strength.rule_scores()
{'Additions': {'nAlphaLCBonus': 0,
  'nAlphaUCBonus': 0,
  'nLengthBonus': 32,
  'nMidCharBonus': 0,
  'nNumberBonus': 0,
  'nSymbolBonus': 0},
 'Deductions': {'nAlphasOnlyBonus': 8,
  'nConsecAlphaLCBonus': 14,
  'nConsecAlphaUCBonus': 0,
  'nConsecNumberBonus': 0,
  'nNumbersOnlyBonus': 0,
  'nRepCharBonus': 1,
  'nSeqAlphaBonus': 0,
  'nSeqNumberBonus': 0,
  'nSeqSymbolBonus': 0}}
```
