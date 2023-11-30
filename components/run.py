import sys
import time
import threading

import offender_detector
import victim_detector
import guardian_angel
import coordinate_system_transformer


thraed_guardian_angel = threading.Thread(target=guardian_angel.run)

thraed_offender_detector = threading.Thread(target=offender_detector.run)

thraed_victim_detector = threading.Thread(target=victim_detector.run)

thraed_guardian_angel = threading.Thread(target=guardian_angel.run)

thraed_coordinate_system_transformer = threading.Thread(target=guardian_angel.run)


thraed_guardian_angel.start()
thraed_offender_detector.start()
thraed_victim_detector.start()
thread_guardian_angel.start()
thread_coordinate_system_transformer.start()


running = True
while running:
    time.sleep(0.1)
