from abc import ABC, abstractmethod

class OAuth2Provider(ABC):
    @abstractmethod
    def authenticate(self, token: str) -> dict:
        pass

    @abstractmethod
    def authorize(self, user_id: str) -> dict:
        pass
