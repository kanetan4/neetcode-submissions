class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for x in strs:
            string += (x + "?")
        # print(string)
        return string

    def decode(self, s: str) -> List[str]:
        output = s.split("?")
        output.pop()
        return output