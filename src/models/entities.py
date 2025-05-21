from dataclasses import dataclass

@dataclass
class ExtractedEntity:
    inferred_type: str
    value: any
