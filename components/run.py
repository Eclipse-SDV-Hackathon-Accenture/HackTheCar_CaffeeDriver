import sys
import time
import threading

import offender_detector
import victim_detector
import guardian_angel
import coordinate_system_transformer
import RemoteVehicle


# python.exe .\ecal_foxglove_bridge.py
# python.exe .\coordinate_system_transformer.py
# python.exe .\offender_detector.py
# python.exe .\victim_detector.py
# python.exe .\guardian_angel.py
# python.exe .\guardian_angel.py

thread_coordinate_system_transformer = threading.Thread(target=coordinate_system_transformer.run)
thraed_offender_detector = threading.Thread(target=offender_detector.run)
thraed_victim_detector = threading.Thread(target=victim_detector.run)
thraed_guardian_angel = threading.Thread(target=guardian_angel.run)
thraed_RemoteVehicle = threading.Thread(target=RemoteVehicle.run)

thread_coordinate_system_transformer.start()
thraed_offender_detector.start()
thraed_victim_detector.start()
thraed_guardian_angel.start()
thraed_RemoteVehicle.start()

print('Running...')

while True:
    print('Loop')
    time.sleep(1)

print('Exit!')