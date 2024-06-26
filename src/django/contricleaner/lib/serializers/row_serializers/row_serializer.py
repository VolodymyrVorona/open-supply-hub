from abc import ABC, abstractmethod


class RowSerializer(ABC):

    @abstractmethod
    def validate(self, row: dict) -> dict:
        pass
