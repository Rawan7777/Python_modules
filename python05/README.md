# 🔌 Code Nexus — Module 05

> **Polymorphic Data Streams in the Digital Matrix**  
> *42 Network — Python Cursus*

---

## 📖 About

**Code Nexus** is the sixth module of the 42 Python cursus, set in the year 2087 where the sprawling digital metropolis of Neo-Tokyo runs on data streams processed in perfect harmony. This module focuses on **method overriding, subtype polymorphism, abstract base classes, and Protocol-based duck typing** — the skills that elevate a programmer into a true Stream Engineer.

Building on file I/O (Module 04), you now learn to design flexible, extensible class hierarchies: defining abstract interfaces, overriding methods in specialized subclasses, and building systems where a single unified interface handles completely different data types through polymorphic dispatch.

> 🗺️ You are a Stream Engineer Initiate in the Code Nexus. Three phases stand between you and full certification as a Senior Stream Engineer.

---

## 🗂️ Project Structure

```
module05/
├── ex0/
│   └── stream_processor.py
├── ex1/
│   └── data_stream.py
└── ex2/
    └── nexus_pipeline.py
```

---

## 📋 Exercises Overview

| Phase | Exercise | File | Core Concept |
|-------|----------|------|--------------|
| **Alpha** | Data Processor Foundation | `stream_processor.py` | ABC + `@abstractmethod` + method overriding |
| **Beta** | Polymorphic Streams | `data_stream.py` | Subtype polymorphism + batch processing |
| **Gamma** | Nexus Integration | `nexus_pipeline.py` | Pipeline architecture + Protocol (duck typing) |

---

## 🔧 Technical Requirements

- **Language:** Python 3.10+
- **Authorized imports:** `abc`, `typing`, `collections` (Ex02 only), `isinstance()`
- **Mandatory pattern:** All base classes must use `ABC` and `@abstractmethod`
- **Type annotations:** All parameters, return types, and class attributes must be fully typed using the `typing` module (`Any`, `List`, `Dict`, `Union`, `Optional`, `Protocol`)
- **Style:** flake8 compliant — clean, readable, well-structured code
- **Error handling:** All processing must fail gracefully — no unhandled crashes

---

## 📝 Exercise Details

### Phase Alpha — Data Processor Foundation

Learn the most fundamental OOP pattern: **abstract base classes and method overriding**.

Build a `DataProcessor` ABC that defines a common interface, then create three specialized subclasses — `NumericProcessor`, `TextProcessor`, and `LogProcessor` — each overriding `process()` and `validate()` to handle its specific data type.

**Key behavior:**
- `process()` and `validate()` are abstract — subclasses *must* implement them
- `format_output()` has a default implementation that subclasses *may* override
- A polymorphic demo processes different data types through the same `List[DataProcessor]` interface

```
$> python3 stream_processor.py
=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===

Initializing Numeric Processor...
Processing data: [1, 2, 3, 4, 5]
Validation: Numeric data verified
Output: Processed 5 numeric values, sum=15, avg=3.0

Initializing Text Processor...
Processing data: "Hello Nexus World"
Validation: Text data verified
Output: Processed text: 17 characters, 3 words

Initializing Log Processor...
Processing data: "ERROR: Connection timeout"
Validation: Log entry verified
Output: [ERROR] ERROR level detected: Connection timeout

=== Polymorphic Processing Demo ===
Processing multiple data types through same interface...
Result 1: Processed 3 numeric values, sum=6, avg=2.0
Result 2: Processed text: 12 characters, 2 words
Result 3: [INFO] INFO level detected: System ready

Foundation systems online. Nexus ready for advanced streams.
```

> 💡 Think about what it means for a method to be *abstract*. Why can you not instantiate `DataProcessor` directly? What guarantee does `@abstractmethod` give you about every concrete subclass?

Authorized: `ABC`, `abstractmethod`, `isinstance()`, `print()`, `typing` module

---

### Phase Beta — Polymorphic Streams

Take polymorphism further with **stream classes that carry state and process batches**.

Build a `DataStream` ABC and three specialized streams — `SensorStream`, `TransactionStream`, `EventStream` — each with its own batch format and processing logic. Then build a `StreamProcessor` manager that handles any stream type through a single unified interface, including a generator-based stats pipeline.

**Key behavior:**
- `process_batch()` is abstract; `filter_data()` and `get_stats()` have overridable defaults
- Each stream class holds its own `stream_id`, `data_type`, and running counters
- `StreamProcessor.get_stats_all()` is a **generator** — it yields stats one stream at a time
- Filtering is criteria-driven and type-specific per stream class

```
$> python3 data_stream.py
=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

Initializing Sensor Stream...
Stream ID: SENSOR_001, Type: Environmental Data
Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
Sensor analysis: 3 readings processed, avg temp: 22.5°C

Initializing Transaction Stream...
Stream ID: TRANS_001, Type: Financial Data
Processing transaction batch: [buy:100, sell:150, buy:75]
Transaction analysis: 3 operations, net flow: +25 units

Initializing Event Stream...
Stream ID: EVENT_001, Type: System Events
Processing event batch: [login, error, logout]
Event analysis: 3 events, 1 error detected

=== Polymorphic Stream Processing ===
Processing mixed stream types through unified interface...

Batch 1 Results:
- Sensor data: 2 readings processed
- Transaction data: 4 operations processed
- Event data: 3 events processed

Stream filtering active: High-priority data only
Filtered results: 2 critical sensor alerts, 1 large transaction
```

> ⚠️ **Generator protocol:** `get_stats_all()` uses `yield` — each call to `next()` resumes execution at the next `yield`. Know the difference between a generator function and a regular function that returns a list. You will be asked about this during evaluation.

Authorized: `ABC`, `abstractmethod`, `isinstance()`, `print()`, `typing` module

---

### Phase Gamma — Nexus Integration *(Capstone)*

The ultimate challenge: combine everything — ABCs, Protocol-based duck typing, pipeline composition, and error recovery — into an **enterprise-grade data processing pipeline**.

Build `ProcessingStage` as a `Protocol` (duck typing — no inheritance required), implement three concrete stages (`InputStage`, `TransformStage`, `OutputStage`), then build three pipeline adapters (`JSONAdapter`, `CSVAdapter`, `StreamAdapter`) that inherit from `ProcessingPipeline` and run data through the stage chain. Orchestrate everything with a `NexusManager`.

**Key behavior:**
- `ProcessingStage` is a `Protocol` — any class with `process()` qualifies, no inheritance needed
- `ProcessingPipeline` is an ABC — adapters inherit from it and override `process()`
- Each adapter iterates through its `stages` list, passing data from one stage to the next
- `NexusManager` handles multiple pipeline types polymorphically via `isinstance()` dispatch
- Error recovery is demonstrated: a bad input triggers `ValueError`, which is caught and handled

```
$> python3 nexus_pipeline.py
=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===

Initializing Nexus Manager...
Pipeline capacity: 1000 streams/second

Creating Data Processing Pipeline...
Stage 1: Input validation and parsing
Stage 2: Data transformation and enrichment
Stage 3: Output formatting and delivery

=== Multi-Format Data Processing ===

Processing JSON data through pipeline...
Input: {'sensor': 'temperature', 'value': 23.5, 'unit': 'C'}
Transform: Enriched with metadata and validation
Output: Processed temperature reading: 23.5°C (Normal range)

Processing CSV data through same pipeline...
Input: "user,action,timestamp"
Transform: Parsed and structured data
Output: user activity logged: 1 actions processed

Processing Stream data through same pipeline...
Input: Real-time sensor stream
Transform: Aggregated and filtered
Output: Stream summary: 5 readings, avg: 21.58°C

=== Pipeline Chaining Demo ===
Pipeline A -> Pipeline B -> Pipeline C
Data flow: Raw -> Processed -> Analyzed -> Stored

Chain result: 3 records processed through 3-stage pipeline
Performance: 95% efficiency, 0.2s total processing time

=== Error Recovery Test ===
Simulating pipeline failure...
Error detected in Stage 2: Invalid data format
Recovery initiated: Switching to backup processor
Recovery successful: Pipeline restored, processing resumed

Nexus Integration complete. All systems operational.
```

> 💡 **Protocol vs ABC:** An ABC enforces inheritance — subclasses *must* opt in by inheriting. A `Protocol` enforces structure — any class with the right method signatures qualifies automatically, regardless of its inheritance chain. This is Python's form of **structural subtyping** (duck typing formalized). Know when to use each.

Authorized: `ABC`, `abstractmethod`, `Protocol`, `isinstance()`, `print()`, `collections`, `typing` module

---

## 🧠 Concepts Introduced

| Concept | First seen | Python mechanism |
|---------|-----------|-----------------|
| Abstract Base Class | Ex00 | `from abc import ABC` |
| Abstract methods | Ex00 | `@abstractmethod` decorator |
| Method overriding | Ex00 | Redefining parent methods in subclass |
| `super()` | Ex00/Ex02 | Delegating to parent `__init__` |
| Subtype polymorphism | Ex01 | Processing `List[DataStream]` uniformly |
| Generator functions | Ex01 | `yield` + `next()` protocol |
| Batch processing | Ex01 | `process_batch()` / `filter_data()` |
| Protocol (duck typing) | Ex02 | `from typing import Protocol` |
| Pipeline composition | Ex02 | Stages stored in `List[Any]`, chained sequentially |
| Error recovery | Ex02 | `try/except` inside pipeline `process()` |

---

## 🔗 ABC vs Protocol Reference

| Feature | `ABC` + `@abstractmethod` | `Protocol` |
|---------|--------------------------|------------|
| Inheritance required | ✅ Yes | ❌ No |
| Enforcement | At instantiation time | At type-check time (mypy) |
| Use case | Shared base behavior + forced interface | Pure structural typing / duck typing |
| Example | `DataProcessor`, `ProcessingPipeline` | `ProcessingStage` |

```python
# ABC — must inherit to qualify
class MyProcessor(DataProcessor):
    def process(self, data: Any) -> str: ...
    def validate(self, data: Any) -> bool: ...

# Protocol — just having the right method is enough
class AnyStage:            # no inheritance!
    def process(self, data: Any) -> Any: ...
```

---

## 🔗 Polymorphism Patterns Reference

| Pattern | Description | Example in project |
|---------|-------------|-------------------|
| Method overriding | Subclass replaces parent method | `NumericProcessor.process()` |
| Subtype polymorphism | Parent type variable holds subclass instance | `List[DataProcessor]` |
| Duck typing (Protocol) | Structural match, no inheritance | `ProcessingStage` protocol |
| Generator protocol | `yield`-based lazy iteration | `StreamProcessor.get_stats_all()` |
| Pipeline composition | Stages chained inside an adapter | `JSONAdapter` running three stages |

---

## 🚀 Running the Exercises

```bash
# Run each exercise independently
cd ex0/ && python3 stream_processor.py
cd ex1/ && python3 data_stream.py
cd ex2/ && python3 nexus_pipeline.py
```

No external data files are required — all test data is defined inline in each `__main__` block.

---

## ⚠️ Important Rules

- **Always use `ABC` and `@abstractmethod`** for base classes — bare classes without the abstract machinery will be flagged during evaluation
- **Never import anything outside the authorized list** — no `dataclasses`, `functools`, or third-party libraries
- Programs must **never crash** — all processing errors must be caught and handled gracefully
- **Type annotations are mandatory everywhere** — unannotated parameters or return types will be flagged
- Overridden methods must maintain the **same signature** as their parent (interface consistency)
- You may adjust flavor text and data samples as long as the core class structure and behavior are preserved

---

## 🤖 AI Usage Policy

AI tools are **permitted** with the following rules:

- ✅ Use AI to explore the difference between `ABC` and `Protocol`, understand `super()` behavior in multi-level hierarchies, and clarify generator semantics
- ✅ Only submit code you **fully understand** and can explain line by line
- ❌ During peer evaluation you'll be asked to explain why `process()` is abstract, what happens when you call `next()` on an exhausted generator, and how `Protocol` differs from `ABC` — "I got it from AI" is not an answer
- ❌ Do not copy-paste solutions you cannot trace through manually

---

## 📦 Submission

Submit all files via your **Git repository**. Only files tracked in the repo will be evaluated.

Files to submit:
- `ex0/stream_processor.py`
- `ex1/data_stream.py`
- `ex2/nexus_pipeline.py`

> Do **not** submit generated files, scratch notebooks, or any extra `.py` files — only the three listed above.

---

*"Same interface, different behavior — this is the Nexus principle. Master it, and any data stream becomes yours to command."*
