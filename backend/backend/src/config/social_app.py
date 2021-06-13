from authlib.integrations.starlette_client import OAuth


social_auth = OAuth()

redirect_uri = "http://localhost:8000/api/auth/github_login"

social_auth.register(
    name="github",
    client_id="4154f2c545347d6e96b7",
    client_secret="ecd43355995b421152f5e3efb2716d033bb05503",
    access_token_url="https://github.com/login/oauth/access_token",
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "user:email"},
)
