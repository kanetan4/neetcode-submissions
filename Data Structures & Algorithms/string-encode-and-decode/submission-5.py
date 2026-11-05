class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        length, i = len(s), 0
        num = 0
        while i < length:
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                if s[i+1] == "#":
                    i += 2
                    decoded.append(s[i:i+num])
                    i += num
                    num = 0
                    continue
            i += 1
        return decoded
