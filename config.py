from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    llm_model_path: str
    grammar_file_path: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
