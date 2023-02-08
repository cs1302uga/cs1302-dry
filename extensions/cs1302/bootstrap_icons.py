import requests

from cs1302.cdn import NpmCdn, JsDelivrCdn

BOOTSTRAP_ICONS_VERSION = "1.10.3"


class BootstrapIcons:
    def __init__(
        self, version: str = BOOTSTRAP_ICONS_VERSION, cdn: NpmCdn = JsDelivrCdn
    ) -> None:
        self.cdn = cdn
        self.version = version

    def get_path(self, name: str) -> str:
        return f"icons/{name}.svg"

    def get_url(self, name: str) -> str:
        return JsDelivrCdn.get_url(
            "bootstrap-icons",
            self.version,
            self.get_path(name),
        )  # return

    def get(self, name: str) -> str:
        return JsDelivrCdn.get(
            "bootstrap-icons",
            self.version,
            self.get_path(name),
        )  # return
