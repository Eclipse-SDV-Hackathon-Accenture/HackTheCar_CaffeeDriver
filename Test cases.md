# Test cases

Motivation...

| TC  | Component | Stimulation   | Expected result  |
|----------------|-------------------|----------------------------------------------------------------|----------------------------|
| Case 1: Valid Coordinates Inside Warning Area  | Offender Detector | x = 5, y = 10 (coordinates inside the warning area)            | Offender detected|
| Case 2: Valid Coordinates Outside Warning Area | Offender Detector | x = -3, y = 10 (coordinates outside the warning area)          | Offender not detected|
| Case 3: Invalid Coordinate data type           | Offender Detector | x = "hello", y = "world" (invalid string coordinates)          | Error message |
| Case 4: Borderline Coordinates                 | Offender Detector | x = 25, y = 50 (coordinates on the border of the warning area) | Offender detected|
| Case 5: Borderline Coordinates                 | Offender Detector | x = 25, y = 50 (coordinates on the border of the warning area) | Offender detected|
| Case 6: Indicator Light Test | Guardian Angel |offenderDetector = True, victimDetector  = True |indicator_request should send True and the ego vehicle's indicator light should turn on|
| Case 7: Indicator Light Test | Guardian Angel |offenderDetector = False, victimDetector = False |indicator_request should send False and the ego vehicle's indicator light should remain off|
| Case 8: Warning Signal Test | Guardian Angel |offenderDetector = True, victimDetector = True |guardianAngel.warning should send True and The warning light on the Foxglove tool should turn on|
| Case 9: Warning Signal Test | Guardian Angel |offenderDetector = False, victimDetector = "Str" |Error message and The warning light on the Foxglove tool should remain off|
