# Hack the Car by Coffee Driver (IAV)

## Idea for Our Tool: Warning Traffic Participants of Danger Situations using Car2X Communication

The idea for our tool comes from recognizing the need to improve communication between vehicles on the road. Specifically, we aim to address the issue of potential danger situations arising when interacting with other road users.To achieve this, we have developed a tool that uses Car2X communication to warn traffic participants if a danger situation can arise.  
By providing clear and timely communication to other road users, we believe we can increase safety and reduce the number of accidents on the road. We recognize the importance of efficient and effective communication and strive to contribute to the development of a safer transportation system.
We have chosen to focus on one specific scenario for the SDV Hackathon 2023 challenge due to the limited timeframe.



## Covered scenario

The scenario we have chosen to focus on for the SDV Hackathon 2023 challenge involves a pedestrian about to cross the street in front of or behind the Ego vehicle while another vehicle (Offender) is passing through. In this situation, there is a risk of an accident occurring if both the Offender and the pedestrian are not aware of each other's presence.
To prevent this from happening and increase road safety, our tool is designed to activate the indicator lights in the Ego vehicle as a warning signal. This warning signal will alert both the Offender and the pedestrian of the potential danger and allow them to take appropriate actions to avoid an accident.
Our tool uses Car2X communication to detect the presence of the Offender and the pedestrian and determine their positions relative to the Ego vehicle. If both are present at the same time, the tool triggers the indicator lights in the Ego vehicle. This feature is designed to provide a clear and timely warning to all parties involved and reduce the risk of accidents.


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
- Car2X communication to the Offender to warn over its HMI and possibly prepare or execute a braking
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

subgraph Danger detection
transformer[Coordinates
            System
Transformer]
offender[Offender
Detector]
victim[Victim
Detector]
angel[Guardian
Angel]
        end

subgraph Warning rising
car_out[Car]:::given
Car2X
end

Car & Trace & Stub --Markers --> transformer

transformer -- Transformed
marker--> offender & victim

offender -- offender
detected --> angel

victim -- victim
detected--> angel

angel -- Light on --> car_out

angel -- Data --> Car2X

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

Transfer of the data from and to the components is realized with
eCAL messages containing objects in protobuf-format.
All components subscribe to certain message topics,
which gives the possibility to visualize the inter-component communication
and to inject synthetic messages for testing purposes.
A stub is developed to provide the message generation with wished values.

### Testing

The behavior of every component and the whole system should be tested
to ensure the correct

The system is developed in a modular architecture with defined data containers (messages).
So can every component be tested isolated, but as a part of a (sub-)system.

````mermaid
    flowchart LR
  Stub -- Stimulation --> Component -- Result --> Evaluation

````

````mermaid
    flowchart LR
  Stub -- Stimulation --> Component1 --> Component2 -- Result --> Evaluation

````

### Rising of the warning

### Visualization

