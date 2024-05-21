from abc import ABC, abstractmethod
from provider.oauth2_provider import OAuth2Provider

class OAuth2Factory(ABC):
    @abstractmethod
    def create_provider(self) -> OAuth2Provider:
        pass
