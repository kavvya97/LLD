## REQUIREMENTS
- multiple floors
- multiple elevators
- Add/Remove Elevators
- TWO TYPES OF REQUESTS
  - person on floor pressing up/down to call the elevator
  - person in the lift pressing the buttons to go to the selected floor

### OBJECTS
- ElevatorSystem
- ElevatorCar
- ElevatorController
- Floor
- Button- InternalButton, ExternalButton
- Direction- UP, DOWN, NONE
- Display
- Door
- Dispatcher- InternalDispatcher, ExternalDispatcher
- ElevatorSelectionStrategy- OddEvenStrategy, ZoneStrategy
- ElevatorControlStrategy- FirstComeFirstServe, ShortestSeekTime, ScanAlgorithm, LookAlgorithm