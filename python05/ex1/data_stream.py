from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Generator


class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return List[Any]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return Dict[str, Union[str, int, float]]


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.data_type: str = "Environmental Data"
        self.analysis_total: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:

        if not data_batch:
            return "No data is provided"

        temp: float = 0.0
        temp_total: int = 0

        for ele in data_batch:
            if isinstance(ele, dict):
                self.analysis_total += len(ele)
                temp_temp: Any = ele.get("temp", "no-reading")
                if not isinstance(temp_temp, str):
                    temp += temp_temp
                    temp_total += 1
            else:
                return "The data is not well structured (dict)"

        avg: float = temp / temp_total if temp_total else 0
        return (
            f"Sensor analysis: {self.analysis_total} readings processed, "
            f"avg temp: {avg}°C"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "processed_count": self.analysis_total,
        }

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:

        result: List[Any] = []

        if not data_batch:
            return result

        for ele in data_batch:
            if isinstance(ele, dict):
                result.extend(
                    value for value in ele.values()
                    if value > criteria
                )
            else:
                return result

        return result


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.data_type: str = "Financial Data"
        self.analysis_total: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:

        if not data_batch:
            return "No data is provided"

        net_flow: int = 0

        for ele in data_batch:
            if isinstance(ele, dict):
                operation: str = ele["operation"]
                amount: int = ele["amount"]
                net_flow += amount if operation == "buy" else -amount
            else:
                return "The data is not well structured (dict)"

        sign: str = "+" if net_flow > 0 else ""
        self.analysis_total = len(data_batch)

        return (
            f"Transaction analysis: {self.analysis_total} operations, "
            f"net flow: {sign}{net_flow} units"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "processed_count": self.analysis_total,
        }

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:

        if not data_batch:
            return []

        result: List[Any] = []

        for ele in data_batch:
            if isinstance(ele, dict):
                if ele["amount"] > criteria:
                    result.append(ele["amount"])
            else:
                return []

        return result


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.data_type: str = "System Events"
        self.analysis_total: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:

        if not data_batch:
            return "No data is provided"

        errors: int = 0

        for ele in data_batch:
            if isinstance(ele, list):
                self.analysis_total += len(ele)
                for event in ele:
                    errors += 1 if event.lower() == "error" else 0
            else:
                return "The data is not well structured (list)"

        return (
            f"Event analysis: {self.analysis_total} events, "
            f"{errors} error detected"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "processed_count": self.analysis_total,
        }

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:

        if not data_batch:
            return []

        result: List[Any] = []

        for ele in data_batch:
            if isinstance(ele, list):
                result.extend(value for value in ele if value == criteria)
            else:
                return []

        return result


class StreamProcessor:

    stream_objects: List[DataStream] = []

    def process_all(self, batches: List[dict]) -> None:

        for ele in batches:
            stream: DataStream = ele["stream"]
            data: List[Any] = ele["data"]

            StreamProcessor.stream_objects.append(stream)
            stream.process_batch(data)

    def get_stats_all(self) -> Generator[Dict[str, Union[str, int, float]],
                                         None, None]:

        for stream in StreamProcessor.stream_objects:
            yield stream.get_stats()

    def filter_all(self, batches_all: List[dict]) -> None:

        result: Dict[DataStream, List[Any]] = {}

        for ele in batches_all:
            stream: DataStream = ele["stream"]
            data: List[Any] = ele["data"]
            criteria: Any = ele["criteria"]

            result[stream] = stream.filter_data(data, criteria)

        sensor_alerts: List[Any]
        large_transaction: List[Any]
        sensor_alerts, large_transaction = result.values()

        print(
            f"Filtered results: {len(sensor_alerts)} critical , "
            f"{len(large_transaction)} large transaction"
        )


if __name__ == "__main__":

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    try:
        print("Initializing Sensor Stream...")
        sensor_01: SensorStream = SensorStream("SENSOR_001")
        print(f"Stream ID: {sensor_01.stream_id}, Type: {sensor_01.data_type}")
        print("Processing sensor batch: "
              "[temp:22.5, humidity:65, pressure:1013]")
        sensor_batch: List[Dict[str, Union[float, int]]] = [
                {
                    "temp": 22.5,
                    "humidity": 65,
                    "pressure": 1013
                }
            ]
        print(sensor_01.process_batch(sensor_batch))
    except Exception as error:
        print(f"Error occured: {error}")

    try:
        print("\nInitializing Transaction Stream...")
        trans_01: TransactionStream = TransactionStream("TRANS_001")
        print(f"Stream ID: {trans_01.stream_id}, Type: {trans_01.data_type}")
        print("Processing transaction batch: [buy:100, sell:150, buy:75]")
        trans_batch: List[Dict[str, Union[str, int]]] = [
            {"operation": "buy", "amount": 100},
            {"operation": "sell", "amount": 150},
            {"operation": "buy", "amount": 75},
        ]
        print(trans_01.process_batch(trans_batch))
    except Exception as error:
        print(f"Error occured: {error}")

    try:
        print("\nInitializing Event Stream...")
        event_01: EventStream = EventStream("EVENT_001")
        print(f"Stream ID: {event_01.stream_id}, Type: {event_01.data_type}")
        print("Processing event batch: [login, error, logout]")
        event_batch: List[List[str]] = [["login", "error", "logout"]]
        print(event_01.process_batch(event_batch))

        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
    except Exception as error:
        print(f"Error occured: {error}")

    sensor_02: SensorStream = SensorStream("SENSOR_002")
    trans_02: TransactionStream = TransactionStream("TRANS_002")
    event_02: EventStream = EventStream("EVENT_002")

    processor: StreamProcessor = StreamProcessor()

    batches: List[dict] = [
        {"stream": sensor_02, "data": [{"temp": 22.5}, {"temp": 29.5}]},
        {
            "stream": trans_02,
            "data": [
                {"operation": "buy", "amount": 50},
                {"operation": "sell", "amount": 200},
                {"operation": "buy", "amount": 80},
                {"operation": "buy", "amount": 120},
            ],
        },
        {"stream": event_02, "data": [["login", "error", "logout"]]},
    ]

    processor.process_all(batches)
    gen: Generator[Dict[str, Union[str, int, float]], None, None]
    gen = processor.get_stats_all()

    print("Batch 1 Results:")
    curr: Dict[str, Union[str, int, float]] = next(gen)
    print(f"- Sensor data: {curr['processed_count']} readings processed")
    curr = next(gen)
    print(f"- Transaction data: {curr['processed_count']} \
          operations processed")
    curr = next(gen)
    print(f"- Event data: {curr['processed_count']} events processed")

    print("\nStream filtering active: High-priority data only")

    batches_all: List[dict] = [
        {
            "stream": sensor_02,
            "data": [{"temp": 50.5}, {"temp": 69.5}],
            "criteria": 40
        },
        {
            "stream": trans_02,
            "data": [
                {"operation": "buy", "amount": 50},
                {"operation": "sell", "amount": 200},
                {"operation": "buy", "amount": 80},
                {"operation": "buy", "amount": 120},
            ],
            "criteria": 150,
        },
    ]

    processor.filter_all(batches_all)
