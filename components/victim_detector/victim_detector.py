import sys
import time

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher

class VictimDetector:
  def __init__(self) -> None:
    print("VictimDetector init...")

if __name__ == "__main__":

  victimDetector = VictimDetector()

  # initialize eCAL API. The name of our Process will be "Python Hello World Publisher"
  ecal_core.initialize(sys.argv, "Python VictimDetector")

  # Create a String Publisher that publishes on the topic
  pub = StringPublisher("VictimDetector.Detected")
  
  # Create a counter, so something changes in our message
  detected = False
  
  # Infinite loop (using ecal_core.ok() will enable us to gracefully shutdown
  # the process from another application)
  while ecal_core.ok():
    # Create a message with a counter an publish it to the topic
    msg = f'{detected}'
    pub.send(msg)
    
    detected = not detected
    
    # Sleep 500 ms
    time.sleep(0.5)
    
  # finalize eCAL API
  ecal_core.finalize()