class Solution:
    def getLastDigit(self, a: str, b: str) -> int:
        if b == "0":
            return 1

        last = int(a[-1])

        # last digit cycles
        cycle = [
            [0],
            [1],
            [2, 4, 8, 6],
            [3, 9, 7, 1],
            [4, 6],
            [5],
            [6],
            [7, 9, 3, 1],
            [8, 4, 2, 6],
            [9, 1]
        ]

        c = cycle[last]
        n = 0
        for ch in b:
            n = (n * 10 + int(ch)) % len(c)

        return c[n - 1] if n != 0 else c[-1]