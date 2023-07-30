class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total, new = str(int(a) + int(b)), []
        for v in total:
            # if current letter not 2 then just append
            if v != "2":
                new.append(v)
            else:
                # if 0 is not in new, eg. 1111, will turn to 10000
                if "0" not in new:
                    new = list(map(lambda x: x.replace('1', '0'), new))
                    new.append("0")
                    new.insert(0, "1")
                else:
                    # else search for 0 to turn into 1, eg. 1012 will turn to 1100
                    for i in range(len(new) - 1, -1, -1):
                        if new[i] == "0":
                            new[i] = "1"
                            break
                        else:
                            new[i] = "0"
                    new.append("0")
        # return as string
        return "".join(new)