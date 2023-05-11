from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(path: str, type: str) -> str:
        raise NotImplementedError('abstact function not implemented')
