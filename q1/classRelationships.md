# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Song
Description: Represents a playable song with an artist and title.
## New Related Class
Class: Playlist
Description: A playable collection of songs.
## Association
Relationship: Playlist contains songs.
Explanation: A playlist is a collection of added songs.
## Multiplicity
Multiplicity: Zero or more
Explanation: A playliat can be empty amd hold an infinite amount of songs.
## UML Class Relationship Diagram
![Class Relationship Diagram](classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes? 
  The class playlist can contain the class songs.
### What multiplicity did you choose and why?
 Zero or more, because a playlist should be able to contain an infinite amount of songs or be empty.
### How did you implement the relationship in Python?
  
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
