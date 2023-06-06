"""
You can create a file called `.env` in the root of the repo, containing your local env vars.
"""
from dotenv import load_dotenv
from pydantic import BaseSettings

# Load environment variables
load_dotenv(verbose=True)


class Settings(BaseSettings):
    """.env variables have priority over following default values"""

    hf_auth_token: str

    class Config:
        """.env file location"""

        env_file = ".env"


settings = Settings()
