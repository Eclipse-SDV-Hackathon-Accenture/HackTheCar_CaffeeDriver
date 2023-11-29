import sys
import time
import math

sys.path.insert(0, '..')

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber
from ecal.core.publisher import ProtoPublisher

# Import the "datatypes.ros.visualization_msgs.MarkerArray_pb2.py" file that we have just generated from the
# datatypes directory 
import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray


class CoordinateTransformer:
  def __init__(self) -> None:

    print("CoordinateTransformer init...")

    self.transformationX = -48.097
    self.transformationY = 32.456
    self.transformationZ = -5.548
    self.rotationx = math.radians(-0.5)
    self.rotationy = math.radians(1.0)
    self.rotationz = math.radians(68,4)


    ecal_core.initialize(sys.argv, "Python Protobuf Subscriber")

    self.sub_ROSTrafficParticipantList = ProtoSubscriber("ROSTrafficParticipantList", MarkerArray.MarkerArray)
    self.sub_ROSTrafficParticipantList.set_callback(self.callback_ROSTrafficParticipantList)

    self.pub_ROSTrafficParticipantListTransformt = ProtoPublisher("ROSTrafficParticipantListTransformt", MarkerArray.MarkerArray)
  
  # Callback for receiving messages
  def callback_ROSTrafficParticipantList(self,topic_name, marker_array_proto_msg, time):

    if(len(marker_array_proto_msg.markers) > 0):
      for marker in marker_array_proto_msg.markers:
        marker.pose.position.x = marker.pose.position.x - self.transformationX
        marker.pose.position.y = marker.pose.position.y - self.transformationY
        marker.pose.position.z = marker.pose.position.z - self.transformationZ  
      self.pub_ROSTrafficParticipantListTransformt.send(marker_array_proto_msg)
    

  def run(self) -> None:
    
    # Just don't exit
    while ecal_core.ok():
      time.sleep(0.5)
  
  # finalize eCAL API
  ecal_core.finalize()

if __name__ == "__main__":
  
  coordinateTransformer = CoordinateTransformer()
  coordinateTransformer.run()