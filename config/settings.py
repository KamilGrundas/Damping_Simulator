import json
import os


class Settings:
    def __init__(self, config_file="config/config.json"):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            # Ustawienia domyślne, jeśli plik nie istnieje
            return {"language": "en"}

    def save_config(self):
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def get(self, key, default=None):
        return self.config.get(key, default)


# Użycie
settings = Settings()
