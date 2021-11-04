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
        if current >= len(search_through):
            return self.__verify_node(current_content)

        if search_through[current] in current_content:
            return self.__deep_search(current_content[search_through[current]], search_through, current + 1)
        elif search_through[current] == "*":
            all_true = True
            for sub_content in current_content:
                all_true = all_true if self.__deep_search(
                    current_content[sub_content], search_through, current + 1) else False
            return all_true
        elif search_through[current] == "?":
            any_true = False
            for sub_content in current_content:
                any_true = True if self.__deep_search(
                    current_content[sub_content], search_through, current + 1) else any_true
            return any_true
        else:
            return self.__verify_node(current_content)

    def __str__(self) -> str:
        return f"{self.path} should '{'regex' if self.regex is not None else 'contain regex'}' '{self.regex if self.regex is not None else self.should_contain}'"
