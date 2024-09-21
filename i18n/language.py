import json
import os
from config.settings import settings
from logs.log_config import logger


class Language:
    def __init__(self, language="en"):
        self.supported_languages = self.load_supported_languages()
        self.language = language
        self.translations = self.load_translations()

    def load_supported_languages(self):
        try:
            file_path = os.path.join("i18n", "languages.json")
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Language file {file_path} does not exist.")

            with open(file_path, "r", encoding="utf-8") as f:
                logger.info(f"Languages loaded: {file_path}")
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading languages file: {e}")
            return {}

    def load_translations(self):
        try:
            file_path = os.path.join("i18n", "translations", f"{self.language}.json")
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Language file {file_path} does not exist.")

            with open(file_path, "r", encoding="utf-8") as f:
                logger.info(f"Language loaded: {file_path}")
                return json.load(f)

        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading language file: {e}")
            return {}

    def set_language(self, language):
        self.language = language
        self.translations = self.load_translations()
        logger.info(f"Language switched to {language}")

    def get(self, key):
        value = self.translations.get(key)
        if value is None:
            logger.warning(
                f"Translation key '{key}' not found for language '{self.language}'"
            )
            return key
        return value


language = Language(settings.config["language"])
print(language.supported_languages)
