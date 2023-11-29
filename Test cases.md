# Test cases

Motivation...

| TC                                             | Component         | Stimulation                                                    | Expected result                |
|------------------------------------------------|-------------------|----------------------------------------------------------------|----------------------------|
| Case 1: Valid Coordinates Inside Warning Area  | Offender Detector | x = 5, y = 10 (coordinates inside the warning area)            | Offender detected|
| Case 2: Valid Coordinates Outside Warning Area | Offender Detector | x = -3, y = 10 (coordinates outside the warning area)          | Offender not detected|
| Case 3: Invalid Coordinate data type           | Offender Detector | x = "hello", y = "world" (invalid string coordinates)          | Error message |
| Case 4: Borderline Coordinates                 | Offender Detector | x = 25, y = 50 (coordinates on the border of the warning area) | Offender detected|
| Case 5: Borderline Coordinates                 | Offender Detector | x = 25, y = 50 (coordinates on the border of the warning area) | Offender detected|
| Case 6: Indicator Light Test | guardian_angel |offenderDetector_Detected = True, victimDetector_Detected  = True |msg_guardianAngel.warning should send True|
| Case 6: Indicator Light Test | guardian_angel |offenderDetector_Detected = False, victimDetector_Detected  = False |msg_guardianAngel.warning should send False|

