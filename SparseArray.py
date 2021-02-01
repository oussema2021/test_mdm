
import math
from collections import Counter

class SparseArray:
  def __init__(self,strings):
    self.strings = strings

  def matchingStrings(self,queries):
    s = Counter(self.strings)
    result = dict()

    for q in queries:
      result.update({q:s[q]})
    return result
