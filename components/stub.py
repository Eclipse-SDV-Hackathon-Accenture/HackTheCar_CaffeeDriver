import sys
import time

sys.path.insert(0, "..")

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher
from ecal.core.subscriber import ProtoSubscriber
from ecal.core.publisher import ProtoPublisher

import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray
import datatypes.ros.visualization_msgs.Marker_pb2 as Marker


class Stub:
    def __init__(self) -> None:
        print("Stub init...")

        ecal_core.initialize(sys.argv, "Python Stub")

        self.pub_ROSTrafficParticipantList = ProtoPublisher(
            "ROSTrafficParticipantList", MarkerArray.MarkerArray
        )

    def run(self) -> None:
        while ecal_core.ok():
            markerArray = MarkerArray.MarkerArray()

            marker = Marker.Marker()
            marker.ns = "car"

            marker2 = Marker.Marker()
            marker2.ns = "car2"

            markerArray.markers.extend([marker, marker2])

            self.pub_ROSTrafficParticipantList.send(markerArray)

            time.sleep(0.5)

        ecal_core.finalize()


if __name__ == "__main__":
    stub = Stub()
    stub.run()
