import json
import os

class JSON:
    @staticmethod
    def save_json(filename, data):
        with open(f'{filename}.json', 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)