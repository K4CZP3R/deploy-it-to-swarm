from typing import Any, List
import re


class YamlRule:
    def __init__(self, path: str, should_contain: str = None,  regex: str = None) -> None:
        self.path = path
        self.should_contain = should_contain
        self.regex = regex

    def check(self, yaml_content: Any) -> bool:
        path_splitted = self.path.split(".")
        return self.__deep_search(yaml_content, path_splitted)

    def __verify_node(self, result):
        # if self.should_contain is not None and self.should_contain in result:
        if self.should_contain is not None:
            for r in result:
                if re.match(self.should_contain, str(r)):
                    return True

        if self.regex is not None and re.search(self.regex, str(result)):
            return True
        return False

    def __deep_search(self, current_content: Any, search_through: List[str], current=0) -> bool:
        if current < len(search_through) and search_through[current] in current_content:
            return self.__deep_search(current_content[search_through[current]], search_through, current + 1)
        elif current < len(search_through) and search_through[current] == "*":
            all_true = True
            for sub in current_content:
                sub_check = self.__deep_search(
                    current_content[sub], search_through, current + 1)
                if not sub_check:
                    all_true = False
            return all_true
        elif current < len(search_through) and search_through[current] == "?":
            any_true = False
            for sub in current_content:
                sub_check = self.__deep_search(
                    current_content[sub], search_through, current + 1)
                if sub_check is True:
                    any_true = True

            return any_true
        return self.__verify_node(current_content)

    def __str__(self) -> str:
        return f"{self.path} should '{'regex' if self.regex is not None else 'contain regex'}' '{self.regex if self.regex is not None else self.should_contain}'"
