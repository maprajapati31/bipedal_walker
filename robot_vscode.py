import time
import pybullet as p

# Set up PyBullet
physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("simple_walker_08mar.urdf")

# Load the bipedal walker URDF
walkerStartPos = [0, 0, 1]
walkerStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
walkerId = p.loadURDF("simple_walker_08mar.urdf", walkerStartPos, walkerStartOrientation)

# Simulation loop
for _ in range(1000):
    p.stepSimulation()
    time.sleep(1./240.)  # control simulation speed

# Disconnect from PyBullet
p.disconnect()
