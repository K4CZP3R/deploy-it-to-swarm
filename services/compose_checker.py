from typing import Any


from typing import Any

from models.yaml_rule import YamlRule
from typing import List


class ComposeChecker:
    def __init__(self, yaml_content: Any, rules: List[YamlRule]) -> None:
        self.yaml_content = yaml_content
        self.rules = rules

    def check(self) -> None:
        total_result = True
        for rule in self.rules:
            total_result if rule.check(self.yaml_content) else False
        return total_result
