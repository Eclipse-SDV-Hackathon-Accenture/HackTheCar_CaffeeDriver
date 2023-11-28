import sys
import time

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher

class OffenderDetector:
  def __init__(self) -> None:
    print("OffenderDetector init...")

if __name__ == "__main__":

  offenderDetector = OffenderDetector()

  # initialize eCAL API. The name of our Process will be "Python Hello World Publisher"
  ecal_core.initialize(sys.argv, "Python OffenderDetector")

  # Create a String Publisher that publishes on the topic
  pub = StringPublisher("OffenderDetector.Detected")
  
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