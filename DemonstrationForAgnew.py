import time


def testBattery():
    print("Beginning Testing...")
    # Cut power from wall outlet by deactivating relay
    time.sleep(1)
    print("Power from wall outlet is now deactivated")
    # Activate relays for gravity battery
    time.sleep(1)
    print("Power is now redirected to come from gravity battery")
    print("Testing is now concluded")


def liftWeights():
    print("Now lifting weights...")
    # Activate relays and PWM to run motor to lift weights
    time.sleep(5)
    print("Weights now lifted")
    print("Redirecting power to come from wall outlet...")
    # Activate relays to reroute power to come from wall outlet
    time.sleep(3)


print("Initializing...")
# Initialize all ports and activate relays to provide power from wall outlet
time.sleep(3)
print("Initialized")
print("Relays ... are activated; power is coming from wall")
input("Press ENTER to begin testing battery")
testBattery()
input("Press ENTER to lift weights back up")
liftWeights()
