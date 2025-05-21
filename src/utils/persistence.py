import os

def load_text_from_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f'File "{path}" does not exists')
    
    contents = None
    with open(path, 'r') as file:
        contents = file.read()
    
    return contents