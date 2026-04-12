class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""
        n = max(len(a), len(b))

        a = a[::-1]
        b = b[::-1]
        for i in range(n):
            da = (ord(a[i]) - ord('0')) if i < len(a) else 0
            db = (ord(b[i]) - ord('0')) if i < len(b) else 0

            total = da + db + carry
            res = str(total % 2) + res
            carry = total // 2

        res = "1" + res if carry else res
        return res
