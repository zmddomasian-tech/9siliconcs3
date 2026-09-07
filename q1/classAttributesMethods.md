## Design Revision
Changes from my previous design:
- added a UID property as a private attribute
- minutes changed to duration in seconds


| Attribute       | Data Type | Visibility | Why Public/Private?                                             |

| Title           | String    | Public     | People should be able to know the song's title for them to find |
| Artist          | String    | Public     | People should be able to recognize the song's artist            |
| Explicit rating | Boolean   | Public     | People should be warned of the song's contents                  |
| Duration        | Int       | Public     | To display the duration of the song (in seconds)                |
| UID             | String    | Private    | The UID must be private for clean dsiplay and prevent tampering |


##Updated Class Diagram:
+--------------------------------------------+
|                    Song                    |
+--------------------------------------------+
| + Title           : String                 |
| + Artist          : String                 |
| + Explicit rating : Boolean                |
| + Duration        : Int                    |
| - UID             : String                 |
+--------------------------------------------+
| + play(self)                               |
| + playback(self, seconds)                  |
| + pause(self)                              |
| + repeat(self)                             |                
+--------------------------------------------+

##Python implementation
![Python source](q1/classimplementation1.py)

##Test run
[Test run]()

##Object Diagram
[Object diagram]()

##Analysis

### Why did you make your chosen attribute private?
- My chosen orivate attribute was the UID. Users must not see the UID so it would display a clean interface and prevent accidental tampering
### Which method changes the state of your object?
- methods play, playback, pause, and repeat all change the state of the object.
### How did your two objects demonstrate that instances are independent?
- By the two objects state's changing idependently of eachother. Object 1 was played and paused and Object 2 was played and continues to play/
### What is the difference between your class diagram and your object diagram?
- The class diagram represents the blueprint of the system while the object diagram is a snapshot of the actual objects and their current data values.
