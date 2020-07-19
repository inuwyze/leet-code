class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        try:
            return math.log2(n).is_integer()
        except:
            return False