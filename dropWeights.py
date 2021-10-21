# Get energy values

# These are sample values
energyHave = 1500
energyNeeded = 2000


def dropWeights():
    global energyHave
    energyHave += 1000
    # Also mechanically drop weights


def liftWeights():
    global energyHave
    energyHave -= 1000
    # Also mechanically lift weights


if energyNeeded > energyHave:
    dropWeights()
if energyHave > energyNeeded + 1000:
    liftWeights()
