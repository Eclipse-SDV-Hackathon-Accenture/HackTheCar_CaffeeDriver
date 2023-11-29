import sys
import time

sys.path.insert(0, '..')

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher
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

        # Create a String Publisher that publishes on the topic
        # self.pub_VictimDetector_Detected = StringPublisher("VictimDetector.Detected")
        self.pub_VictimDetector = ProtoPublisher("VictimDetector", victim_detector_pb2.VictimDetector)
        self.sub_ROSTrafficParticipantList = ProtoSubscriber("ROSTrafficParticipantList", MarkerArray.MarkerArray)

        self.sub_ROSTrafficParticipantList.set_callback(self.callback_ROSTrafficParticipantList)

    def run(self) -> None:

        while ecal_core.ok():
            # self.pub_VictimDetector_Detected.send(str(self.detected))

            msg_VictimDetector = victim_detector_pb2.VictimDetector()

            msg_VictimDetector.detected = self.detected
            self.pub_VictimDetector.send(msg_VictimDetector)
            self.detected = not self.detected

            time.sleep(0.12)

        # finalize eCAL API
        ecal_core.finalize()

    def callback_ROSTrafficParticipantList(self, topic_name, marker_array_proto_msg, time):
        ma = marker_array_proto_msg
        if len(ma.markers) > 0:

            # marker loop
            for marker in ma.markers:
                self.detected = False

                # type filter
                if marker.ns != "pedestrian":
                    print("not pedestrian -> drop")
                    continue

                # coordinates filter
                # victim
                if marker.pose.position.x > parameters.VICTIM_DANGER_ZONE_LONG_NEAR:
                    print(marker.pose.position.x, " > ", parameters.VICTIM_DANGER_ZONE_LONG_NEAR)
                    continue

                if marker.pose.position.x < parameters.VICTIM_DANGER_ZONE_LONG_FAR:
                    print(marker.pose.position.x, " < ", parameters.VICTIM_DANGER_ZONE_LONG_FAR)
                    continue

                if marker.pose.position.y > parameters.VICTIM_DANGER_ZONE_LAT_FAR:
                    print(marker.pose.position.y, " > ", parameters.VICTIM_DANGER_ZONE_LAT_FAR)
                    continue

                if marker.pose.position.y < parameters.VICTIM_DANGER_ZONE_LAT_NEAR:
                    print(marker.pose.position.y, " < ", parameters.VICTIM_DANGER_ZONE_LAT_NEAR)
                    continue

                self.detected = True
                return


if __name__ == "__main__":
    victimDetector = VictimDetector()
    victimDetector.run()
