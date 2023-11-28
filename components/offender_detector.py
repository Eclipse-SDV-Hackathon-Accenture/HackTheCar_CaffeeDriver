import sys
import time

sys.path.insert(0, '..')

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher
from ecal.core.subscriber import ProtoSubscriber

import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray

class OffenderDetector:
  def __init__(self) -> None:

    print("OffenderDetector init...")
    
    self.detected = False

    ecal_core.initialize(sys.argv, "Python OffenderDetector")

    # Create a String Publisher that publishes on the topic
    self.pub_OffenderDetector_Detected = StringPublisher("OffenderDetector.Detected")
    
    self.sub_ROSTrafficParticipantList = ProtoSubscriber("ROSTrafficParticipantList", MarkerArray.MarkerArray)

    self.sub_ROSTrafficParticipantList.set_callback(self.callback_ROSTrafficParticipantList)

  def run(self) -> None:
    
    while ecal_core.ok():
      
      self.pub_OffenderDetector_Detected.send(str(self.detected))
      
      time.sleep(0.1)
      
    # finalize eCAL API
    ecal_core.finalize()
  
  def callback_ROSTrafficParticipantList(self, topic_name, marker_array_proto_msg, time):
    ma = marker_array_proto_msg
    if(len(ma.markers) > 0):
      for var in ma.markers:
        # if(var.ns == "pedestrian"):
          # print("pedestrian")
        detected = False
        if(var.ns == "car"):
          if var.pose.position.x < 40 and var.pose.position.x > 45:
            if var.pose.position.y < 12 and var.pose.position.y > 0:
              detected = True
        
        self.detected = False
          
if __name__ == "__main__":

  offenderDetector = OffenderDetector()
  offenderDetector.run()