from typing import List
from models.yaml_rule import YamlRule


class YamlRulesCollections:
    @staticmethod
    def get_flame_rules() -> List[YamlRule]:
        return [
            YamlRule("services.?.deploy.labels",
                     should_contain="flame\.type=.+"),
            YamlRule("services.?.deploy.labels",
                     should_contain="flame\.name=.+"),
            YamlRule("services.?.deploy.labels",
                     should_contain="flame\.url=.+")
        ]

    @staticmethod
    def get_traefik_rules() -> List[YamlRule]:
        return [
            YamlRule("services.?.deploy.labels",
                     should_contain="traefik.enable=true"),
            YamlRule("services.?.deploy.labels",
                     should_contain="traefik.docker.network=ksp-traefik"),
            YamlRule("services.?.deploy.labels",
                     should_contain="traefik\.http\.routers\..+\.rule=Host\(`.+\`\)"),
            YamlRule("services.?.deploy.labels",
                     should_contain="traefik\.http\.routers\..+\.entrypoints=.+"),
            YamlRule("services.?.deploy.labels",
                     should_contain="traefik\.http\.services\..+\.loadbalancer\.server\.port=\d+")

        ]

    @staticmethod
    def get_network_rules(network_name: str) -> List[YamlRule]:
        return [
            YamlRule("networks", should_contain=network_name),
            YamlRule(f"networks.{network_name}.external", regex="True"),
            YamlRule("services.?.networks", should_contain=network_name),
        ]

    @staticmethod
    def get_swarm_rules() -> List[YamlRule]:
        return [
            YamlRule("services.*.deploy", should_contain="replicas")
        ]

    @staticmethod
    def get_version_rules() -> List[YamlRule]:
        return [
            YamlRule("version", regex="\d+\.[3,8]")
        ]
