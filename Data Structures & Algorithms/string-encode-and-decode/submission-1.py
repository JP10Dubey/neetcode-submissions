class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "wrenm,cbt"
        return "xvt1267vhyvgyt".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "wrenm,cbt":
            return []
        return s.split("xvt1267vhyvgyt")