
from helpers.file_loader import FileLoader

from helpers.file_loader import FileLoader
from helpers.yaml_loader import YamlLoader
from helpers.yaml_rules_collections import YamlRulesCollections
from models.yaml_rule import YamlRule
from services.compose_checker import ComposeChecker

docker_compose = YamlLoader.load_yaml_from_str(
    FileLoader.load_file_to_str("docker-compose.yml"))

rules = [*YamlRulesCollections.get_traefik_rules(), *YamlRulesCollections.get_swarm_rules(),
         *YamlRulesCollections.get_network_rules("ksp-traefik"), *YamlRulesCollections.get_flame_rules(), *YamlRulesCollections.get_version_rules()]

ComposeChecker(docker_compose, rules).check()
