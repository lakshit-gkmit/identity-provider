from factories.oauth2_factory import OAuth2Factory
from provider.google_oauth_provider import GoogleOAuthProvider

class GoogleOAuthFactory(OAuth2Factory):
    def create_provider(self) -> GoogleOAuthProvider:
        return GoogleOAuthProvider()
