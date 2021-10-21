energyHave = 1000
energyNeed = 2000


def blockHeight():
    global energyHave, energyNeed
    if energyHave > energyNeed:
        return 1 #drop weights
    else:
        energyHave += 1000 #lift weights
        blockHeight() #recursion until drop weights


blockHeight()
