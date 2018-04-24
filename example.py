"""
>>> from passwordstrength.entropy import Entropy
>>> import math
>>> entropy = Entropy()
>>> math.log2(entropy.entropy_non_word('asdhaskj'))
39.603517745128734
>>> math.log2(entropy.entropy_word_list(['hello', 'World']))
27.575424759098897
>>> math.log2(entropy.entropy_non_word('@sdhaskj'))
41.54693421676237
>>> math.log2(entropy.entropy_non_word('@sQsA$!j'))
48.43376716002963
"""