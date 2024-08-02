import json
from pathlib import Path

JSON_FILE_PATH = Path(__file__).resolve().parent / 'fornecedores.json'

def read_json():
    """Lê o conteúdo do arquivo JSON."""
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_json(data):
    """Escreve o conteúdo no arquivo JSON."""
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def get_fornecedores():
    """Retorna a lista de fornecedores do arquivo JSON."""
    return read_json()

def add_fornecedor(fornecedor):
    """Adiciona um novo fornecedor ao arquivo JSON."""
    data = read_json()
    data.append(fornecedor)
    write_json(data)
