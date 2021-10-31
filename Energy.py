energyHave = getEnergyReading() #Reading is pulled live from the Raspberry Pi
energyNeed = getEnergyNeed() #Pre-determined number from the user

def blockHeight():
    global energyHave, energyNeed
    if energyNeed > energyHave:
        return 1 #drop weights
    else:
        energyHave += liftWeight() #lift weights
        blockHeight() #recursion until drop weights


blockHeight()
