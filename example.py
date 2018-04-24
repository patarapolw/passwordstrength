"""
>>> from passwordstrength.entropy import Entropy
>>> import math
>>> entropy = Entropy()
>>> math.log2(entropy.entropy_non_word('asdhaskj'))
39.603517745128734
>>> math.log2(entropy.entropy_word_list(['hello', 'World']))
39.78991097025491
>>> math.log2(entropy.entropy_non_word('@sdhaskj'))
41.54693421676237
"""