import sys
import time

sys.path.insert(0, "..")

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber
from ecal.core.publisher import ProtoPublisher

import parameters
import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray
import datatypes.victim_detector_pb2 as victim_detector_pb2


class VictimDetector:
    def __init__(self) -> None:
        print("VictimDetector init...")

        self.detected = False

        ecal_core.initialize(sys.argv, "Python VictimDetector")

        self.pub_VictimDetector = ProtoPublisher(
            "VictimDetector", victim_detector_pb2.VictimDetector
        )
        self.sub_ROSTrafficParticipantList = ProtoSubscriber(
            "ROSTrafficParticipantListTransformed", MarkerArray.MarkerArray
        )

        self.sub_ROSTrafficParticipantList.set_callback(
            self.callback_ROSTrafficParticipantList
        )

    def run(self) -> None:
        while ecal_core.ok():
            msg_VictimDetector = victim_detector_pb2.VictimDetector()

            msg_VictimDetector.detected = self.detected
            self.pub_VictimDetector.send(msg_VictimDetector)

            time.sleep(0.1)

        ecal_core.finalize()

    def callback_ROSTrafficParticipantList(
        self, topic_name, marker_array_proto_msg, time):
        self.detected = self.check_marker(marker_array_proto_msg)

    def check_marker(self, ma) -> bool:
        if len(ma.markers) > 0:
            for marker in ma.markers:
                if marker.ns != "pedestrian":
                    continue

                if marker.pose.position.x < parameters.VICTIM_DANGER_ZONE_LONG_NEAR:
                    continue

                if marker.pose.position.x > parameters.VICTIM_DANGER_ZONE_LONG_FAR:
                    continue

                if marker.pose.position.y > parameters.VICTIM_DANGER_ZONE_LAT_FAR:
                    continue

                if marker.pose.position.y < parameters.VICTIM_DANGER_ZONE_LAT_NEAR:
                    continue
                
                return True

        return False


if __name__ == "__main__":
    victimDetector = VictimDetector()
    victimDetector.run()
