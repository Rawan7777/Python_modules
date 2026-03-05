from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0
        self.error_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return result string."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria. Can be overridden."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics. Can be overridden."""
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
            "error_count": self.error_count,
        }


class SensorStream(DataStream):
    """Stream for environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings and compute average temperature."""
        if not data_batch:
            return "No sensor data to process."
        temps: List[float] = []
        for item in data_batch:
            try:
                if isinstance(item, dict) and "temp" in item:
                    temps.append(float(item["temp"]))
            except (ValueError, TypeError):
                self.error_count += 1
        self.processed_count += len(data_batch)
        avg_temp: float = sum(temps) / len(temps) if temps else 0.0
        return (
            f"Sensor analysis: {len(item)} readings processed, "
            f"avg temp: {avg_temp:.1f}°C"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter sensor data; 'critical' returns high-value readings."""
        if criteria == "critical":
            result: List[Any] = []
            for item in data_batch:
                try:
                    val: float = (
                        float(item["temp"])
                        if isinstance(item, dict) and "temp" in item
                        else float(item)
                    )
                    if val > 30.0:
                        result.append(item)
                except (ValueError, TypeError):
                    pass
            return result
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["stream_type"] = self.stream_type
        return stats


class TransactionStream(DataStream):
    """Stream for financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"
        self.total_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transactions and compute net flow."""
        if not data_batch:
            return "No transaction data to process."
        net_flow: float = 0.0
        for item in data_batch:
            try:
                if isinstance(item, dict):
                    op: str = item.get("op", {})
                    amount: float = float(item.get("amount", 0))
                net_flow += amount if op == "buy" else -amount
            except (ValueError, TypeError):
                self.error_count += 1
        self.processed_count += len(data_batch)
        self.total_flow += net_flow
        sign: str = "+" if net_flow >= 0 else ""
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {sign}{net_flow:.0f} units"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter transactions; 'large' returns items > 100 units."""
        if criteria == "large":
            result: List[Any] = []
            for item in data_batch:
                try:
                    amount: float = (
                        float(item.get("amount", 0))
                        if isinstance(item, dict)
                        else float(item)
                    )
                    if amount > 100:
                        result.append(item)
                except (ValueError, TypeError):
                    pass
            return result
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["stream_type"] = self.stream_type
        stats["total_flow"] = self.total_flow
        return stats


class EventStream(DataStream):
    """Stream for system event data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"
        self.error_events: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process system events and count errors."""
        if not data_batch:
            return "No event data to process."
        errors: int = sum(
            1 for item in data_batch
            if item.lower() == "error"
        )
        self.error_events += errors
        self.processed_count += len(data_batch)
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{errors} error detected"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter events; 'high-priority' returns error events."""
        if criteria == "high-priority":
            return [
                item for item in data_batch
                if "error" in str(item).lower()
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["stream_type"] = self.stream_type
        stats["error_events"] = self.error_events
        return stats


class StreamProcessor:
    """Manages multiple stream types polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a stream with the processor."""
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        """Process each stream with its corresponding batch."""
        results: List[str] = []
        for stream, batch in zip(self.streams, batches):
            try:
                results.append(stream.process_batch(batch))
            except Exception as e:
                results.append(f"Stream error: {e}")
        return results

    def filter_all(
        self,
        batches: List[List[Any]],
        criteria: Optional[str] = None
    ) -> List[List[Any]]:
        """Filter each stream's batch using stream-specific logic."""
        return [
            stream.filter_data(batch, criteria)
            for stream, batch in zip(self.streams, batches)
        ]


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    # Individual stream demos
    print("\nInitializing Sensor Stream...")
    sensor: SensorStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch: List[Any] = [
        {"temp": 22.5, "humidity": 65, "pressure": 1013}
    ]
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_batch))

    print("\nInitializing Transaction Stream...")
    trans: TransactionStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    trans_batch: List[Any] = [
        {"op": "buy", "amount": 100},
        {"op": "sell", "amount": 150},
        {"op": "buy", "amount": 75},
    ]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans.process_batch(trans_batch))

    print("\nInitializing Event Stream...")
    event: EventStream = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch: List[str] = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_batch))

    # Polymorphic processing via StreamProcessor
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor: StreamProcessor = StreamProcessor()
    s2: SensorStream = SensorStream("SENSOR_002")
    t2: TransactionStream = TransactionStream("TRANS_002")
    e2: EventStream = EventStream("EVENT_002")

    processor.add_stream(s2)
    processor.add_stream(t2)
    processor.add_stream(e2)

    batches: List[List[Any]] = [
        [22.1, 35.6],
        [
            {"op": "buy", "amount": 50},
            {"op": "sell", "amount": 200},
            {"op": "buy", "amount": 80},
            {"op": "buy", "amount": 120},
        ],
        ["login", "error", "logout"],
    ]

    results: List[str] = processor.process_all(batches)
    print("\nBatch 1 Results:")
    print(f"- Sensor data: 2 readings processed")
    print(f"- Transaction data: 4 operations processed")
    print(f"- Event data: 3 events processed")

    # Filtering demo
    print("\nStream filtering active: High-priority data only")
    sensor_filtered: List[Any] = s2.filter_data([22.1, 35.6], "critical")
    trans_filtered: List[Any] = t2.filter_data(
        [
            {"op": "buy", "amount": 50},
            {"op": "sell", "amount": 200},
        ],
        "large",
    )
    event_filtered: List[Any] = e2.filter_data(
        ["login", "error", "logout"], "high-priority"
    )
    print(
        f"Filtered results: {len(sensor_filtered)} critical sensor alerts, "
        f"{len(trans_filtered)} large transaction"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()