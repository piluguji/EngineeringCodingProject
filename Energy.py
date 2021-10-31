energyHave = getEnergyReading() #Reading is pulled live from the Raspberry Pi
energyNeed = getEnergyNeed() #Pre-determined number from the user

def blockHeight():
    global energyHave, energyNeed
    if energyNeed > energyHave:
        energyHave += dropWeight()
    else:
        energyHave -= liftWeight()

def dropWeight():
    global energyHave, energyNeed
    drop(energyNeed-energyHave) #sends a signal to drop the weights to get needed energy
    return energyNeed - energyHave #returns the value to update energyHave 
    
def liftWeight():
    global energyHave, energyNeed
    lift(energyHave - energyNeed) #sends a signal to lift the weights to store excess energy
    return energyHave - energyNeed #returns the value to update energyHave
    
