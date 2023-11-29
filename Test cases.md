# Test cases

Motivation...

| TC ID | Component         | Stimulation                                              | Expected result       |
|-------|-------------------|----------------------------------------------------------|-----------------------|
| 1     | Offender Detector | Marker transformed<br>y > OFFENDER_DANGER_ZONE_LONG_FAR  | Offender not detected |
| 2     | Offender Detector | Marker transformed<br>y < OFFENDER_DANGER_ZONE_LONG_NEAR | Offender not detected |