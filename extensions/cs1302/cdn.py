import requests
import requests_cache

from abc import abstractmethod, ABC
from requests_cache import CachedSession


class NpmCdn(ABC):
    @classmethod
    @abstractmethod
    def get_url_format(cls) -> str:
        ...

    @classmethod
    def get_url(cls, package: str, version: str, path: str) -> str:
        url_format = cls.get_url_format()
        return url_format.format(
            package=package,
            version=version,
            path=path,
        )  # return

    @classmethod
    def get_cached_session(cls) -> CachedSession:
        return CachedSession(
            f"cs1302.cdn.{cls.__name__}",
            backend="filesystem",
            use_temp=True,
        )

    @classmethod
    def get(cls, package: str, version: str, path: str) -> str:
        url = cls.get_url(package, version, path)
        session = cls.get_cached_session()
        request = session.get(url)
        text = request.text.strip()
        return text


class JsDelivrCdn(NpmCdn):
    @classmethod
    def get_url_format(cls) -> str:
        return "https://cdn.jsdelivr.net/npm/{package}@{version}/{path}"
