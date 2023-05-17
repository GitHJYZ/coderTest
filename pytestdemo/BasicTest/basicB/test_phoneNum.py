class Solution:
    def letterCombinations(self, digits: str)-> list[str]:
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index:int):
            if index == len(digits):
                result.append("".join(tmp))
            else:
                digit = digits[index]
                for i in phoneMap[digit]:
                    tmp.append(i)
                    backtrack(index+1)
                    tmp.pop()

        tmp = list()
        result = list()
        backtrack(0)
        return result

def test_num():
    digits = '2'
    s = Solution()
    res = s.letterCombinations(digits)
    print(res)
