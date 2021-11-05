from typing import Any
import yaml


class YamlLoader:
    @staticmethod
    def load_yaml_from_str(str: str) -> Any:
        """
        Loads a yaml file from a string.
        """
        return yaml.load(str, Loader=yaml.FullLoader)
