import sys
import time

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher
from ecal.core.subscriber import ProtoSubscriber

import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray


class VictimDetector:
  def __init__(self) -> None:
    print("VictimDetector init...")
      
    ecal_core.initialize(sys.argv, "Python VictimDetector")

    self.detected = False

    self.pub_VictimDetector_Detected = StringPublisher("VictimDetector.Detected")
  
    
  def run(self) -> None:

    while ecal_core.ok():
      self.pub_VictimDetector_Detected.send(str(self.detected))
      self.detected = not self.detected
      time.sleep(0.5)
      
    ecal_core.finalize()

if __name__ == "__main__":

  victimDetector = VictimDetector()
  victimDetector.run()