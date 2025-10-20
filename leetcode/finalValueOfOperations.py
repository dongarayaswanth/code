class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        s = 0
        for op in operations:
            if op == 'X++' or op == '++X':
                s += 1
            elif op == 'X--' or op == '--X':
                s -= 1
            else:
                pass
        return s
        