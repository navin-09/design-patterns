# Design Patterns — Senior Backend (Python / FastAPI)

Patterns every senior backend dev should know, grouped by category.
Three tiers: GoF patterns that survive, enterprise patterns, and
resilience / distributed-systems patterns.

## Categories & patterns

### 1. Creational (GoF)
- Factory Method : A factory is code whose JOB is to CREATE objects, so the caller doesn't have to new/instantiate them directly.
- Singleton : Ensures a class has ONLY ONE instance and gives everyone a single shared point of access to it.
- Builder : Lets you construct a complex object STEP BY STEP instead of passing a giant constructor with many parameters.

### 2. Structural (GoF)
- Adapter : A wrapper that translates one interface into another so two incompatible pieces of code can talk to each other.
- Decorator : Wraps an object to ADD behavior/responsibilities dynamically without changing its original class.

### 3. Behavioral (GoF)
- Strategy : Defines a family of interchangeable algorithms and lets you SWAP the behavior at runtime without changing the caller.
- Observer / Pub-Sub : An object (subject) notifies a list of subscribers automatically when its state changes — publish without knowing who listens.
- Command : Wraps a request (action + its data) into an object so you can queue it, undo it, or delay it.
- State : Lets an object CHANGE its behavior when its internal state changes, as if it switched to a different class.
- Template Method : Defines the SKELETON of an algorithm in a base class, letting subclasses fill in the specific steps.
- Specification : Encapsulates a business rule as a composable object you can combine with AND/OR/NOT to test if something satisfies it.

### 4. Enterprise / Architectural
- Repository : A single collection-style layer that hides WHERE and HOW data is stored, so the rest of the app talks to objects, not SQL.
- Unit of Work : Tracks all changes (inserts/updates/deletes) in one place and COMMITS them together as a single transaction.
- Dependency Injection : Passes an object's dependencies in from the outside instead of letting it create them, so it's easy to swap and test.
- Service Layer : A thin layer that holds the app's USE-CASE logic so controllers/handlers stay dumb and business rules live in one place.

### 5. Resilience / Distributed Systems
- Circuit Breaker : Watches for failing calls and TRIPS open to fail fast / recover gracefully instead of hammering a broken dependency.
- Retry + Exponential Backoff : Automatically re-attempts a failed call, waiting progressively longer between tries to avoid overwhelming the system.
- Rate Limiting : Caps how many requests a client can make in a window to protect the system from abuse and overload.
- CQRS : Splits the write model from the read model so each can scale and evolve independently (Command vs Query).
- Saga / Orchestration : Coordinates a multi-step distributed transaction by chaining local steps with compensating actions to undo on failure.
- Event Sourcing / Outbox : Stores state as an APPEND-ONLY log of events (with an Outbox pattern to publish them reliably without losing writes).
- Cache-Aside : App checks the cache first, loads from the DB on a miss, and populates the cache — keeping hot data close to the caller.
- Message Queue / Async : Decouples producers from consumers by passing work through a queue so tasks run asynchronously and survive spikes.

## Folder structure

```
design-patterns/
├── README.md
└── patterns/
    ├── creational/ -> (fsb)
    │   ├── factory/
    │   ├── singleton/
    │   └── builder/
    ├── structural/ -> (ad)
    │   ├── adapter/
    │   └── decorator/
    ├── behavioral/ -> (socstp)
    │   ├── strategy/
    │   ├── observer/
    │   ├── command/
    │   ├── state/
    │   ├── template_method/
    │   └── specification/
    ├── enterprise/ -> (ruds)
    │   ├── repository/
    │   ├── unit_of_work/
    │   ├── dependency_injection/
    │   └── service_layer/
    └── resilience/ -> (crr)
        ├── circuit_breaker/
        ├── retry_backoff/
        ├── rate_limiting/
        ├── cqrs/
        ├── saga/
        ├── event_sourcing/
        ├── cache_aside/
        └── message_queue/
```
