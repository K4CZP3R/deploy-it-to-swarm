from typing import Any


from typing import Any

from models.yaml_rule import YamlRule
from typing import List


class ComposeChecker:
    def __init__(self, yaml_content: Any, rules: List[YamlRule]) -> None:
        self.yaml_content = yaml_content
        self.rules = rules

    def check(self) -> None:
        for rule in self.rules:
            result = rule.check(self.yaml_content)
            print(f"{rule}: {result}")
