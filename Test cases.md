# Test cases

The purpose of this Test Cases.md file is to ensure that our code works correctly and produces accurate results. By testing various input scenarios and output cases,
we can verify the reliability and effectiveness of our code. Furthermore, documenting these tests allows us to easily reproduce them in the future and catch any potential regressions or issues that may arise. 
Conducting thorough testing increases confidence in the performance of our code and helps identify and address any bugs or errors early on. This, in turn, improves the overall quality and usability of the Code.
Therefore, we have compiled a set of test cases in the following table. Each test case outlines the components, the expected output, and the steps necessary to validate the results. These tests will help us ensure that our code performs as expected in different scenarios and conditions.
<br><br><br>


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
