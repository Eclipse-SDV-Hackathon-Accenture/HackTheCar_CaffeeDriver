import sys
import time

sys.path.insert(0, "..")

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

        self.pub_OffenderDetector = ProtoPublisher(
            "OffenderDetector", offender_detector_pb2.OfferDetector
        )

        self.sub_ROSTrafficParticipantList = ProtoSubscriber(
            "ROSTrafficParticipantListTransformed", MarkerArray.MarkerArray
        )
        self.sub_ROSTrafficParticipantList.set_callback(
            self.callback_ROSTrafficParticipantList
        )

    def run(self) -> None:
        while ecal_core.ok():
            msg_OfferDetector = offender_detector_pb2.OfferDetector()

            msg_OfferDetector.detected = self.detected
            self.pub_OffenderDetector.send(msg_OfferDetector)

            time.sleep(0.1)
        ecal_core.finalize()

    def callback_ROSTrafficParticipantList(
        self, topic_name, marker_array_proto_msg, time
    ) -> None:
        self.detected = self.check_marker(marker_array_proto_msg)

    def check_marker(self, ma) -> bool:
        if len(ma.markers) > 0:
            for marker in ma.markers:
                if marker.ns != "car":
                    continue

                if marker.pose.position.x > parameters.OFFENDER_DANGER_ZONE_LONG_NEAR:
                    continue

                if marker.pose.position.x < parameters.OFFENDER_DANGER_ZONE_LONG_FAR:
                    continue

                if marker.pose.position.y > parameters.OFFENDER_DANGER_ZONE_LAT_FAR:
                    continue

                if marker.pose.position.y < parameters.OFFENDER_DANGER_ZONE_LAT_NEAR:
                    continue

                print("Offender ", marker.id, "detected!")
                return True

        return False

def run():
    offenderDetector = OffenderDetector()
    offenderDetector.run()

if __name__ == "__main__":
    run()