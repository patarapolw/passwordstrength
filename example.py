"""
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
"""
