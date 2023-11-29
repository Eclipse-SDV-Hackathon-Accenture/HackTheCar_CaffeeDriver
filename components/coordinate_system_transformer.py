import sys
import time
import math
import numpy as np
sys.path.insert(0, '..')
import ecal.core.core as ecal_core
from scipy.spatial.transform import Rotation as R
from ecal.core.subscriber import ProtoSubscriber
from ecal.core.publisher import ProtoPublisher
import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray
import datatypes.ros.tf2_msgs.TFMessage_pb2 as TFMessage


class CoordinateTransformer:
    def __init__(self) -> None:

        print("CoordinateTransformer init...")

        self.transformationX = 0.0
        self.transformationY = 0.0
        self.transformationZ = 0.0
        self.lidarYaw = 0.0
        self.vehicleYaw = 0.0

        ecal_core.initialize(sys.argv, "Coordinate Transformer")

        self.sub_ROSTrafficParticipantList = ProtoSubscriber("ROSTrafficParticipantList", MarkerArray.MarkerArray)
        self.sub_ROSVehiclePoseTransforms = ProtoSubscriber("ROSVehiclePoseTransforms", TFMessage.TFMessage)
        self.sub_ROSVLS128CenterCenterRoofTransform = ProtoSubscriber("ROSVLS128CenterCenterRoofTransform", TFMessage.TFMessage)

        self.pub_ROSTrafficParticipantListTransformt = ProtoPublisher("ROSTrafficParticipantListTransformed", MarkerArray.MarkerArray)

        self.sub_ROSTrafficParticipantList.set_callback(self.callback_ROSTrafficParticipantList)
        self.sub_ROSVehiclePoseTransforms.set_callback(self.callback_ROSVehiclePoseTransforms)
        self.sub_ROSVLS128CenterCenterRoofTransform.set_callback(self.callback_ROSVLS128CenterCenterRoofTransform)

    def callback_ROSVehiclePoseTransforms(self, topic_name, tfmessage_array_proto_msg, time):
        if(len(tfmessage_array_proto_msg.transforms) > 0):
            for transform in tfmessage_array_proto_msg.transforms:
                if(transform.child_frame_id == "vehicle_rear-axle_hub-height"):
                    vehicleYaw = self.euler_from_quaternion(
                        transform.transform.rotation.x,
                        transform.transform.rotation.y,
                        transform.transform.rotation.z,
                        transform.transform.rotation.w)[2]
                    if(self.vehicleYaw != vehicleYaw):
                        self.vehicleYaw = vehicleYaw
                        
                    
                    self.transformationX = transform.transform.translation.x
                    self.transformationY = transform.transform.translation.y
                    self.transformationZ = transform.transform.translation.z
    
    def callback_ROSVLS128CenterCenterRoofTransform(self, topic_name, tfmessage_array_proto_msg, time):
        if(len(tfmessage_array_proto_msg.transforms) > 0):
            for transform in tfmessage_array_proto_msg.transforms:
                if(transform.child_frame_id == "lidar_velodyne_vls128_center"):
                    LidarYaw = self.euler_from_quaternion(
                        transform.transform.rotation.x,
                        transform.transform.rotation.y,
                        transform.transform.rotation.z,
                        transform.transform.rotation.w)[2]
                    if(self.lidarYaw != LidarYaw):
                        self.lidarYaw = LidarYaw
                    
  # Callback for receiving messages
    def callback_ROSTrafficParticipantList(self, topic_name, marker_array_proto_msg, time):
        vcar = [ self.transformationX ,  self.transformationY,  self.transformationZ]
        r = R.from_euler('z', math.degrees(-self.vehicleYaw), degrees=True)
        vcar = r.apply(vcar)
        if(len(marker_array_proto_msg.markers) > 0):
            for marker in marker_array_proto_msg.markers:
                v = [ marker.pose.position.x ,  marker.pose.position.y,  marker.pose.position.z]
                v = r.apply(v)
                marker.pose.position.x = v[0] - vcar[0]
                marker.pose.position.y = v[1] - vcar[1]
                marker.pose.position.z = v[2] - vcar[2]

            self.pub_ROSTrafficParticipantListTransformt.send(marker_array_proto_msg)

    def run(self) -> None:

        # Just don't exit
        while ecal_core.ok():
            time.sleep(0.5)
    
      # finalize eCAL API
    ecal_core.finalize()

    def euler_from_quaternion(self, x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians

if __name__ == "__main__":

    coordinateTransformer = CoordinateTransformer()
    coordinateTransformer.run()
