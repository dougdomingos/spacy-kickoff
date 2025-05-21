import importlib
import spacy
import spacy.cli

from config import consts
from core.extractors.base import EntityExtractorEngine
from models.entities import ExtractedEntity

class SpacyExtractor(EntityExtractorEngine):

    def __init__(self):
        super().__init__()
    
    def extract_entities(self, text_content: str):
        entities = []

        processor = self._config.get("processor")
        processed_text = processor(text_content)

        for entity in processed_text.ents:
            entities.append(ExtractedEntity(entity.label_, entity.text))
        
        return entities

    def _init_extractor_configuration(self):
        return {
            "model": consts.SPACY_LANG_MODEL,
            "processor": self._load_spacy_model(consts.SPACY_LANG_MODEL)
        }
    
    def _load_spacy_model(self, model_id: str) -> spacy.Language:
        try:
            importlib.import_module(model_id)
        except ImportError:
            print(f'Model "{model_id}" not found. Downloading...')
            spacy.cli.download(model_id)
        
        return spacy.load(model_id)
