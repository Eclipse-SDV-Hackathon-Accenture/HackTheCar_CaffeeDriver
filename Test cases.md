# Test cases

Motivation...

| TC                                             | Component         | Stimulation                                                    | Expected result                |
|------------------------------------------------|-------------------|----------------------------------------------------------------|--------------------------------|
| Case 1: Valid Coordinates Inside Warning Area  | Offender Detector | x = 5, y = 10 (coordinates inside the warning area)            | True (Offender detected)       |
| Case 2: Valid Coordinates Outside Warning Area | Offender Detector | x = -3, y = 10 (coordinates outside the warning area)          | False  (Offender not detected) |
| Case 3: Invalid Coordinate data type           | Offender Detector | x = "hello", y = "world" (invalid string coordinates)          | Error message                  |
| Case 4: Borderline Coordinates                 | Offender Detector | x = 25, y = 50 (coordinates on the border of the warning area) | True (Offender detected)       |
