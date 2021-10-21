energyHave = 1000
energyNeed = 2000


def blockHeight():
    global energyHave, energyNeed
    if energyHave > energyNeed:
        return 1
    else:
        energyHave += 1000
        blockHeight()


blockHeight()
