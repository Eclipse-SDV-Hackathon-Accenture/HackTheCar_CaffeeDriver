# Hack the Car by Coffee Driver (IAV)

## Idea

We want to warn the traffic participants, if a danger situation can arise. 
For purposes of SDV Hackathon 2023 challenge we cover only one scenario.

## Covered scenario

Assumed the target car (Ego car) is parked on the street shoulder, we want to detect, 
if, at the same time, a pedestrian is about to walk across the street for or behind the Ego car
and a car (Offender) passes the Ego car.
In this case can the pedestrian be harmed by the passed car.
To prevent it both traffic participants should be warned by the Ego car,
which make the Ego car incarnate a Guardian Angel (in the meaning of protecting the pedestrian).

```
=======================================



---   ---   ---   ---   ---   ---   ---
  ----------
  |Offender|-------->   !
  ----------
                        ^
    -------   --------- | -------
    |     |   |Ego car| | |     |
    -------   --------- | -------
========================|==============
                        O
```

## Approach

We use the Ego car sensor array to detect the both defined traffic participants:
the Offender and the Victim.
The detection includes the selecting the relevant objects and their intention.
The development of this detection algorythm is separated into two complexity stages:

- Stage 1 with simple static check, if any of both object types (car, pedestrian) is in the defined danger zone
- Stage 2 with movement vector building to recognise the situation in dynamic sense

If a potential danger situation is recognized, a warning should be fired.
The available Ego car is capable to activate the turn signal lights.
For the hackathon challenge we make use of only this feature.
Further warning channels and visualization are imaginable:

- Car lights to side select warning
- Car lights to spot the pedestrian to improve the visibility
- Car2car communication to the Offender to warn over its HMI and possibly prepare or execute a braking
- The build-in music system to tell the pedestrian about the danger and its direction
- Anonymized post into the (city traffic) cloud to train the AI and detect potential danger spots

## Realization

The focus of the realization is to implement the logic of detection of the relevant objects and to fire a warning.

```mermaid
    flowchart LR
        data_source[Sensor data] --> angel[Guardian Angel] --> warning[Warning system]
```

Both the sensor data and the warning system are provided by the given car over a high-level abstraction layer.

### Data flow

```mermaid
    flowchart LR
        classDef given stroke:#777, fill:#777
        subgraph Sensor data 
            Car:::given
            Trace:::given
            Stub
        end
        subgraph Guardian Angel 
            offender[Offender Detector]
            victim[Victim Detector]
            state[Car State Check]
        end
        Car & Trace & Stub --Markers--> offender & victim
        offender -- offender detected--> warning[Warning System]:::given
        victim -- victim detected--> warning
        Car & Trace --Signals--> state --Car state --> warning
```

### Sensor data feeding

For purposes of the development we used both the trace recorded while simulating of a set of sub-scenarios
and an implemented stub to feed objects in the Ego car environment.

Our covered scenario contains detection of two traffic participants.
For understanding of world representation with provided sensor data
two isolated traces was recorded in addition to complete one:

- Movement of the passing car (Offender)
- Movement of the Pedestrian (Victim)
  - inclusive a movement around the Ego car to determine its dimensions
- Simultaneous movement of both the Offender and the Victim

### Coordinate system transformation

Provided trace data contains coordinates in a system placed in the world.
The axes of the world-related coordinate system can,
but not have to be parallel to same axes of the car-related coordinate system.

To detect the parallelism of the Offender trajectory
a coordinate system transformation is necessary.
The offset and the angles of rotation for all three coordinates are
provided by the car abstraction layer.

### Integration of the Guardian Angel components

Transfer of the data from and to the components is

eCAL messages

protobuf-format

Visualization
