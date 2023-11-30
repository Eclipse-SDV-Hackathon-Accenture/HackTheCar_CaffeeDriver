import sys
import time
import json
import threading
import paho.mqtt.client as mqtt
from flask import Flask, request, jsonify
from flask_sock import Sock
from flask import send_from_directory
from flask import render_template

class RemoteVehicle:
    def __init__(self) -> None:
        print("RemoteVehicle init...")
        self.topic_guardian_angel_warning = "eclipse_sdv_hackathon/car2car/guardian_angel/warning"
        self.waring = False
        self.sock_clients = []
        self.signals = {
             'warning': False
            }

        self.mqtt = mqtt.Client()
        self.mqtt.on_connect  = self.mqtt_on_connect 
        self.mqtt.on_message = self.mqtt_on_message
        self.mqtt.connect("localhost", 1883)
        self.mqtt.loop_start()
        self.app = Flask('RemoteVehicle')
        self.sock = Sock(self.app)

        @self.app.route('/')
        def __index():
            return send_from_directory('webapp', 'index.htm')

        @self.app.route('/<path:path>')
        def send_file(path):
            return send_from_directory('webapp', path)

        @self.app.route('/hello')
        def __hello():
            return 'hello'
        @self.sock.route('/')
        def __echo(ws):
            print("New Websocket Connection")
            self.sock_clients.append({
                'ws': ws,
                'open': True,
                'index': len(self.sock_clients)
            })
            self.sendSignals(self.signals)
            while True:
                msg = json.loads(ws.receive())

    def ws_send_msg(self, msg):
        for client in self.sock_clients:
            if client['ws'].connected:
                client['ws'].send(json.dumps(msg))

    def sendSignals(self, signals):
        self.ws_send_msg({
              'event': 'Signals',
              'data': signals
          })

    def run(self) -> None:
        threading.Thread(target=self.runWebserver).start()
        while True:
            print(f'warning: {self.warning}')
            time.sleep(0.1)

    def runWebserver(self):
        self.app.run(host='0.0.0.0', port=8080)

    def mqtt_on_connect(self, client, userdata, flags, rc):  
        print("Connected with result code "+str(rc))
        self.mqtt.subscribe(self.topic_guardian_angel_warning)

    def mqtt_on_message(self, client, userdata, msg):
        if msg.topic == self.topic_guardian_angel_warning:
            self.warning = msg.payload.decode() == 'True'
            self.signals['warning'] = self.warning
            self.sendSignals(self.signals)

if __name__ == "__main__":
    remoteVehicle = RemoteVehicle()
    remoteVehicle.run()