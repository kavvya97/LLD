# LLD
Repository for storing common Low-level design problem with architecture diagrams and listing design patters used in the problem.

##  Core components
- Classes and Objects (key classes, responsibilities, data, methods)
- Interfaces and abstractions (functions exposed to outside world vs hidden functiions, part of s/m likely to change)
- Relations between classes(Association('uses-a'), composition(strong 'has-a'), aggregation(weak 'has-a'), inheritance('is-a'))
- methods(public/private, input/output response)
- Design patterns 
  - Singleton: useful when you need exactly one instance of a class across your system.
  - Factory: useful when you want to delegate object creation without exposing the instantiation details to the client.
  - Strategy: useful when you need to switch between multiple algorithms or behaviors at runtime.
  - Observer: useful for event-driven systems where you need to establish a publisher–subscriber relationship between objects.
  - Decorator: useful when you want to add new behavior to objects without altering existing code.
  - Adapter: useful when you need to bridge incompatible interfaces to work together.
  - Facade: useful when you want to provide a simplified interface to a complex subsystem.

  