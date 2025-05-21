from core.extractors.base import EntityExtractorEngine


class EntityExtractor:
    
    def __init__(self, engine: EntityExtractorEngine):
        self._extractor = engine
    
    def extract_entities_from_text(self, text: str) -> None:
        for entity in self._extractor.extract_entities(text):
            print(entity.__dict__)