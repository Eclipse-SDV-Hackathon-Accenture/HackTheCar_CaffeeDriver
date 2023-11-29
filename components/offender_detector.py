import sys
import time

sys.path.insert(0, '..')

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber
from ecal.core.publisher import ProtoPublisher

import parameters
import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray
import datatypes.offender_detector_pb2 as offender_detector_pb2

x_list = []
y_list = []


class OffenderDetector:
    def __init__(self) -> None:

        print("OffenderDetector init...")

        self.detected = False

        ecal_core.initialize(sys.argv, "Python OffenderDetector")

        # Create a String Publisher that publishes on the topic
        # self.pub_OffenderDetector_Detected = StringPublisher("OffenderDetector.Detected")

        self.pub_OffenderDetector = ProtoPublisher("OffenderDetector", offender_detector_pb2.OfferDetector)

        self.sub_ROSTrafficParticipantList = ProtoSubscriber("ROSTrafficParticipantListTransformed",
                                                             MarkerArray.MarkerArray)
        self.sub_ROSTrafficParticipantList.set_callback(self.callback_ROSTrafficParticipantList)

    def run(self) -> None:

        while ecal_core.ok():
            # self.pub_OffenderDetector_Detected.send(str(self.detected))

            msg_OfferDetector = offender_detector_pb2.OfferDetector()

            msg_OfferDetector.detected = self.detected
            self.pub_OffenderDetector.send(msg_OfferDetector)
            # self.detected = not self.detected

            time.sleep(0.11)

        # finalize eCAL API
        ecal_core.finalize()

    def callback_ROSTrafficParticipantList(self, topic_name, marker_array_proto_msg, time) -> None:
        ma = marker_array_proto_msg
        self.detected = False

        if self.check_marker(ma):
            self.detected = True

    def check_marker(self, ma) -> bool:
        # detected = False
        if len(ma.markers) > 0:

            # marker loop
            for marker in ma.markers:
                # type filter
                if marker.ns != "car":
                    continue

                # coordinates filter
                # print(marker.pose.position.x, marker.pose.position.y)
                # offender
                if marker.pose.position.x > parameters.OFFENDER_DANGER_ZONE_LAT_NEAR:
                    # print("LAT NEAR", marker.pose.position.x, ">", parameters.OFFENDER_DANGER_ZONE_LAT_NEAR)
                    continue

                if marker.pose.position.x < parameters.OFFENDER_DANGER_ZONE_LAT_FAR:
                    # print("LAT FAR", marker.pose.position.x, "<", parameters.OFFENDER_DANGER_ZONE_LAT_FAR)
                    continue

                if marker.pose.position.y > parameters.OFFENDER_DANGER_ZONE_LONG_FAR:
                    # print("LONG FAR", marker.pose.position.y, ">", parameters.OFFENDER_DANGER_ZONE_LONG_FAR)
                    continue

                if marker.pose.position.y < parameters.OFFENDER_DANGER_ZONE_LONG_NEAR:
                    # print("LONG NEAR", marker.pose.position.y, "<", parameters.OFFENDER_DANGER_ZONE_LONG_NEAR)
                    continue

                print("Offender ", marker.id, "detected!")
                # detected = True
                return True

        return False


if __name__ == "__main__":
    offenderDetector = OffenderDetector()
    offenderDetector.run()
