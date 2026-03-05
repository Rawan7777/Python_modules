from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Default output formatting (can be overridden)."""
        return f"Output: {result}\n"


class NumericProcessor(DataProcessor):
    """Processor for numeric list data."""

    def validate(self, data: Any) -> bool:
        try:
            return bool(data) and all(isinstance(x, (int, float)) for x in data)
        except TypeError:
            return False

    def process(self, data: Any) -> str:

        count = len(data)
        total = sum(data)
        avg = total / count

        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:

        char_count = len(data)
        word_count = len(data.split())

        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    """Processor for log entry strings."""

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return ":" in data

    def process(self, data: Any) -> str:

        level, message = data.split(":", 1)
        message = message.strip()

        return f"[{level}] {level} level detected: {message}"


def main() -> None:

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric_processor = NumericProcessor()
    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    try:
        if numeric_processor.validate(numeric_data):
            print("Validation: Numeric data verified")
            result = numeric_processor.process(numeric_data)
            print(numeric_processor.format_output(result))
        else:
            print("Validation: Numeric data not verified")
    except Exception as error:
        print(f"Error: {error}")

    print("Initializing Text Processor...")
    text_processor = TextProcessor()
    text_data = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    try:
        if text_processor.validate(text_data):
            print("Validation: Text data verified")
            result = text_processor.process(text_data)
            print(text_processor.format_output(result))
        else:
            print("Validation: Text data not verified")
    except Exception as error:
        print(f"Error: {error}")

    print("Initializing Log Processor...")
    log_processor = LogProcessor()
    log_data = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    try:
        if log_processor.validate(log_data):
            print("Validation: Log entry verified")
            result = log_processor.process(log_data)
            print(log_processor.format_output(result))
        else:
            print("Validation: Log entry not verified")
    except Exception as error:
        print(f"Error: {error}")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    data_samples = [
    [1, 2, 3],
    "Hello sweety",
    "INFO: System ready",
]

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    for i in range(len(processors)):
        processor = processors[i]
        data = data_samples[i]

        try:
            result = processor.process(data)
            print("Result", i + 1, ":", result)
        except Exception as error:
            print("Result", i + 1, ": Error -", error)

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()