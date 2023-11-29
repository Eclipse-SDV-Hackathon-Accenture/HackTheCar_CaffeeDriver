import sys
import time

sys.path.insert(0, '..')

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher
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

        self.sub_ROSTrafficParticipantList = ProtoSubscriber("ROSTrafficParticipantList", MarkerArray.MarkerArray)
        self.sub_ROSTrafficParticipantList.set_callback(self.callback_ROSTrafficParticipantList)

    def run(self) -> None:

        while ecal_core.ok():
            # self.pub_OffenderDetector_Detected.send(str(self.detected))

            msg_OfferDetector = offender_detector_pb2.OfferDetector()

            msg_OfferDetector.detected = self.detected
            self.pub_OffenderDetector.send(msg_OfferDetector)
            self.detected = not self.detected

            time.sleep(0.11)

        # finalize eCAL API
        ecal_core.finalize()

    def callback_ROSTrafficParticipantList(self, topic_name, marker_array_proto_msg, time) -> None:
        ma = marker_array_proto_msg
        self.detected = False

        if len(ma.markers) > 0:

            # marker loop
            for marker in ma.markers:
                # type filter
                if marker.ns != "car":
                    continue

                # print("x=", marker.pose.position.x, " y=", marker.pose.position.y)
                x_list.append(marker.pose.position.x)
                y_list.append(marker.pose.position.y)

                # coordinates filter
                # offender
                if marker.pose.position.x > parameters.OFFENDER_DANGER_ZONE_LONG_NEAR:
                    continue

                if marker.pose.position.x < parameters.OFFENDER_DANGER_ZONE_LONG_FAR:
                    continue

                if marker.pose.position.y > parameters.OFFENDER_DANGER_ZONE_LAT_FAR:
                    continue

                if marker.pose.position.y < parameters.OFFENDER_DANGER_ZONE_LAT_NEAR:
                    continue

                print("Offender detected!")
                self.detected = True
                return

        print("x_min=", min(x_list), "x_max=", max(x_list), "y_min=", min(y_list), "y_min=", min(y_list))


if __name__ == "__main__":
    offenderDetector = OffenderDetector()
    offenderDetector.run()
