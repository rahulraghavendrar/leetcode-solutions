class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        result = []

        for i in range(len(strs)):
            a = len(strs[i])
            sizes.append(a)

        for i in sizes:
            result.append(str(i))
            result.append(",")

        result.append("#")
        result.extend(strs)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes = []
        k = 0
        num = ""

        while s[k] != '#':
            if s[k] == ',':
                sizes.append(int(num))
                num = ""
            else:
                num += s[k]

            k += 1

        count = k + 1
        result = []

        for length in sizes:
            result.append(s[count : count + length])
            count += length

        return result