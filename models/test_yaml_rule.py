import pytest

from models.yaml_rule import YamlRule


def test_regex_rules_str_comparasion():
    to_test_yaml = {
        "test": {
            "a": {
                "b": {
                    "c": "testValid!"
                }
            }
        }
    }

    assert YamlRule('test.a.b.c', regex="testValid!").check(to_test_yaml)


def test_regex_rules_to_str_comparasion():
    to_test_yaml = {
        "test": {
            "a": {
                "b": {
                    "c": 12345
                }
            }
        }
    }

    assert YamlRule("test.a.b.c", regex="12345").check(to_test_yaml)


def test_regex_rules_str_comparasion_fail():
    to_test_yaml = {
        "test": {
            "a": {
                "b": {
                    "c": "testValid!"
                }
            }
        }
    }

    assert not YamlRule('test.a.b.c', regex="testInvalid!").check(to_test_yaml)


def test_should_contain_str():
    to_test_yaml = {
        "test": ["yeah", "boi"]
    }

    assert YamlRule('test', should_contain="yeah").check(to_test_yaml)


def test_should_contain_str_fail():
    to_test_yaml = {
        "test": ["yeah", "boi"]
    }

    assert not YamlRule('test', should_contain="pfff").check(to_test_yaml)


def test_should_contain_regex():
    to_test_yaml = {
        "test": ["this.test", "something else"]
    }

    assert YamlRule("test", should_contain=r"this\..+").check(to_test_yaml)


def test_regex_all_dict():
    to_test_yaml = {
        "test": {
            "arr": {
                "yeah": {
                    "name": "boi"
                },
                "foo": {
                    "name": "boi"
                }
            }
        }
    }

    assert YamlRule("test.arr.*.name", regex="boi").check(to_test_yaml)


def test_regex_all_array():
    to_test_yaml = {
        "test": {
            "arr": [
                {
                    "yeah": {
                        "name": "boi",
                        "subname": "test"
                    }
                },
                {
                    "foo": {
                        "name": "boi",
                        "subname": "rest"
                    }
                }
            ]
        }
    }

    assert YamlRule("test.arr.*.name", regex="boi").check(to_test_yaml)
    assert not YamlRule("test.arr.*.subname", regex="test").check(to_test_yaml)


def test_regex_any_array():
    to_test_yaml = {
        "test": {
            "arr": [
                {
                    "yeah": {
                        "name": "boi",
                        "subname": "test"
                    }
                },
                {
                    "foo": {
                        "name": "rboi",
                        "subname": "rest"
                    }
                }
            ]
        }
    }

    assert YamlRule("test.arr.?.name", regex="boi").check(to_test_yaml)
    assert YamlRule("test.arr.?.subname", regex="test").check(to_test_yaml)


def test_regex_any_dict():
    to_test_yaml = {
        "test": {
            "arr": {
                "yeah": {
                    "name": "boi"
                },
                "foo": {
                    "name": "boir"
                }
            }
        }
    }

    assert YamlRule("test.arr.?.name", regex="boi").check(to_test_yaml)
