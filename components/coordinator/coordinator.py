import sys
import time

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher
from ecal.core.subscriber import StringSubscriber

class Coordinator:

  def __init__(self) -> None:
    print("Coordinator init...")

    ecal_core.initialize(sys.argv, "Python Coordinator")

    self.offenderDetector_Detected = False
    self.victimDetector_Detected = False
    
    self.pub_Coordinator_Warning = StringPublisher("Coordinator.Warning")

    
    sub_OffenderDetector_Detected = StringSubscriber("OffenderDetector.Detected")
    sub_VictimDetector_Detected = StringSubscriber("VictimDetector.Detected")
    
    sub_OffenderDetector_Detected.set_callback(self.callback_OffenderDetector_Detected)
    sub_VictimDetector_Detected.set_callback(self.callback_VictimDetector_Detected)
    

  def run(self):
    while ecal_core.ok():

      print(f'offenderDetector_Detected: {self.offenderDetector_Detected}')
      print(f'victimDetector_Detected: {self.victimDetector_Detected}')
      print()

      warning = self.offenderDetector_Detected and self.victimDetector_Detected
      self.pub_Coordinator_Warning.send(str(warning))

      
      time.sleep(0.5)
    
    # finalize eCAL API
    ecal_core.finalize()
    
  def callback_OffenderDetector_Detected(self, topic_name, msg, time):
    # print("Debug eCAL callback_OffenderDetector_Detected: {}".format(msg))
    self.offenderDetector_Detected = (msg == "True")

  def callback_VictimDetector_Detected(self, topic_name, msg, time):
    # print("Debug eCAL callback_VictimDetector_Detected: {}".format(msg))
    self.victimDetector_Detected = (msg == "True")


if __name__ == "__main__":

  coordinator = Coordinator()
  coordinator.run()