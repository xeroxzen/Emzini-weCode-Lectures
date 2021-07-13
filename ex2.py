# Go Bears

def oski(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk + 1, berk - 1]

        def berk(ley): return berk - ley
        return [berk, cal(berk)]
    return cal(2)


# oski(abs)
