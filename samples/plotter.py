import sys
import time
sys.path.insert(0, '..')
import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber
import matplotlib.pyplot as plt

# Import the "datatypes.ros.visualization_msgs.MarkerArray_pb2.py" file that we have just generated from the
# datatypes directory 
import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray

class Plot:
    def __init__(self) -> None:
        self.x_values = []
        self.y_values = []
        self.var_ids = []
        self.MarkerValues = {}

        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('x_value')
        self.ax.set_ylabel('y_value')
        self.ax.set_xlim(left=-10, right=10)
        self.ax.set_ylim(bottom=-10, top=10)

        plt.ion()

        ecal_core.initialize(sys.argv, "Plotter")

        self.sub = ProtoSubscriber("ROSTrafficParticipantListTransformed"
                      , MarkerArray.MarkerArray)
        self.sub.set_callback(self.callback)

    def update_plot(self):
        for id in self.MarkerValues:
            x_data = self.MarkerValues[id]["x_values"]
            y_data = self.MarkerValues[id]["y_values"]
            t_data = self.MarkerValues[id]["timestamp"]
            line_1 = self.ax.plot(x_data, y_data, 'bo')

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

# Callback for receiving messages
    def callback(self, topic_name, marker_array_proto_msg, time):
        ma = marker_array_proto_msg
        if(len(ma.markers) > 0):
            for var in ma.markers:
                if(var.ns == "pedestrian"): #pedestrian
                    if var.id in self.MarkerValues:
                        self.MarkerValues[var.id]["timestamp"].append(var.header.stamp.sec + (var.header.stamp.nsec*(10**(-9))))
                        self.MarkerValues[var.id]["x_values"].append(var.pose.position.x)
                        self.MarkerValues[var.id]["y_values"].append(var.pose.position.y)
                    else:
                        self.MarkerValues[var.id] = {}
                        self.MarkerValues[var.id]["timestamp"] = [var.header.stamp.sec + (var.header.stamp.nsec*(10**(-9)))]
                        self.MarkerValues[var.id]["x_values"] = [var.pose.position.x]
                        self.MarkerValues[var.id]["y_values"] = [var.pose.position.y]
                    if var.id not in self.var_ids:
                        self.var_ids.append(var.id)

    def doSomething(self) -> None:
        time.sleep(0.1)

    def run(self) -> None:
        plt.show(block=False)
        while ecal_core.ok():
            self.update_plot()
            time.sleep(0.2)

        print("first finish")
        ecal_core.finalize()
      
if __name__ == "__main__":
    plot = Plot()
    plot.run()