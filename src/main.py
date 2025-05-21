from core.entity_extractor import EntityExtractor
from core.extractors.spacy import SpacyExtractor
from utils.input_parser import parse_args
from utils.persistence import load_text_from_file

if __name__ == "__main__":
    args = parse_args()
    text = load_text_from_file(args.file)

    extractor = EntityExtractor(SpacyExtractor())
    extractor.extract_entities_from_text(text)