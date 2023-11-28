import sys
import time

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher
from ecal.core.subscriber import StringSubscriber

class Coordinator:
  def __init__(self) -> None:
    print("Coordinator init...")

offenderDetector_Detected = False
victimDetector_Detected = False

def callback_OffenderDetector_Detected(topic_name, msg, time):
  # print("Received: {}".format(msg))
  global offenderDetector_Detected
  offenderDetector_Detected = (msg == "True")

def callback_VictimDetector_Detected(topic_name, msg, time):
  # print("Received: {}".format(msg))
  global victimDetector_Detected
  victimDetector_Detected = (msg == "True")

if __name__ == "__main__":

  coordinator = Coordinator()

  # initialize eCAL API. The name of our Process will be "Python Hello World Publisher"
  ecal_core.initialize(sys.argv, "Python Coordinator")

  # Create a String Publisher that publishes on the topic
  pub = StringPublisher("Coordinator.Warning")

  
  sub_OffenderDetector_Detected = StringSubscriber("OffenderDetector.Detected")
  sub_VictimDetector_Detected = StringSubscriber("VictimDetector.Detected")
  
  sub_OffenderDetector_Detected.set_callback(callback_OffenderDetector_Detected)
  sub_VictimDetector_Detected.set_callback(callback_VictimDetector_Detected)
  
  # Just don't exit
  while ecal_core.ok():
    time.sleep(0.5)
    print(f'offenderDetector_Detected: {offenderDetector_Detected}')
    print(f'victimDetector_Detected: {victimDetector_Detected}')
    print()
  # finalize eCAL API
  ecal_core.finalize()