energyHave = getEnergyReading() #Reading is pulled live from the Raspberry Pi
energyNeed = getEnergyNeed() #Pre-determined number from the user

def blockHeight():
    global energyHave, energyNeed
    if energyNeed > energyHave:
        energyHave += dropWeight()
    else:
        energyHave -= liftWeight()
