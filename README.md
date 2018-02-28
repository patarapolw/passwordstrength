# PasswordStrength
Editable password strength calculator for Python

## Installation

    pip install passwordstrength

## Password Meter

This is based on http://www.passwordmeter.com

### Usage

```python
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
