
from helpers.file_loader import FileLoader

from helpers.file_loader import FileLoader
from helpers.yaml_loader import YamlLoader
from models.yaml_rule import YamlRule
from services.compose_checker import ComposeChecker

docker_compose = YamlLoader.load_yaml_from_str(
    FileLoader.load_file_to_str("docker-compose.yml"))

rules = [
    YamlRule("networks", should_contain="ksp-traefik"),
    YamlRule("networks.ksp-traefik.external", should_be=True),
    YamlRule("services.?.networks", should_contain="ksp-traefik"),
    YamlRule("services.*.deploy", should_contain="replicas"),
    YamlRule("services.?.deploy.labels", should_contain="traefik.enable=true"),
    YamlRule("services.?.deploy.labels",
             should_contain="traefik.docker.network=ksp-traefik")
]


ComposeChecker(docker_compose, rules).check()
