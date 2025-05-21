from abc import ABC, abstractmethod

from models.entities import ExtractedEntity

class EntityExtractorEngine(ABC):
    
    def __init__(self):
        self._config = self._init_extractor_configuration()
    
    @abstractmethod
    def extract_entities(self, text_content: str) -> list[ExtractedEntity]:
        pass
    
    @abstractmethod
    def _init_extractor_configuration(self) -> dict[str, any]:
        pass