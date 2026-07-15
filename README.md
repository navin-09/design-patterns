# Design Patterns — Senior Backend (Python / FastAPI)

Patterns every senior backend dev should know, grouped by category.
Three tiers: GoF patterns that survive, enterprise patterns, and
resilience / distributed-systems patterns.

## Categories & patterns

### 1. Creational (GoF)
- Factory Method
- Singleton  *(know critically — interview favorite, production anti-pattern)*
- Builder

### 2. Structural (GoF)
- Adapter
- Decorator

### 3. Behavioral (GoF)
- Strategy
- Observer / Pub-Sub
- Command
- State
- Template Method
- Specification

### 4. Enterprise / Architectural
- Repository
- Unit of Work
- Dependency Injection
- Service Layer

### 5. Resilience / Distributed Systems
- Circuit Breaker
- Retry + Exponential Backoff
- Rate Limiting
- CQRS
- Saga / Orchestration
- Event Sourcing / Outbox
- Cache-Aside
- Message Queue / Async

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
