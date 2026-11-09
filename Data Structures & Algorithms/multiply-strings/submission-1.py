class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return "0"
        total = len(num1) + len(num2)
        carry = 0
        ans = ""
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(total - 1):
            digit = carry
            n, m = 0, i
            while n < len(num1) and m >= 0:
                if m < len(num2): 
                    digit += int(num1[n]) * int(num2[m])
                n += 1
                m -= 1
            carry = digit // 10
            ans += str(digit % 10)
        if carry != 0: ans += str(carry)
        return ans[::-1]
