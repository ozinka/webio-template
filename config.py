import json
import os
import hashlib
import random
import string
from dataclasses import dataclass, field


@dataclass
class Config:
    _instance = None  # Class-level variable for the singleton instance

    # Define file paths as class variables with default values
    users_file_path: str = field(default='data/users.json', init=False)
    config_file_path: str = field(default='data/config.json', init=False)
    users: dict = field(init=False, default_factory=dict)
    config: dict = field(init=False, default_factory=dict)

    def __post_init__(self):
        # Ensure the data directory exists
        os.makedirs('data', exist_ok=True)

        # Load or create users.json
        self.users = self.load_or_create_users()

        # Load or create config.json
        self.config = self.load_or_create_config()

    def load_or_create_users(self) -> dict:
        """Load users from file or create default users if file doesn't exist."""
        default_users = {
            "admin": {
                "password": hashlib.sha256("admin".encode()).hexdigest(),
                "role": "admin"
            }
        }

        if not os.path.exists(self.users_file_path):
            with open(self.users_file_path, 'w') as file:
                json.dump(default_users, file, indent=4)
                print(f"File '{self.users_file_path}' created with default users.")

        with open(self.users_file_path, 'r') as file:
            return json.load(file)

    def load_or_create_config(self) -> dict:
        """Load configuration from file or create default config if file doesn't exist."""
        default_config = {
            "secret_key": self.generate_random_string(32),
              "web_prod_link": "",
              "web_dev_link": "",
              "db_prod_host": "",
              "db_dev_host": "",
              "db_prod_user": "",
              "db_prod_password": ""
        }

        if not os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'w') as file:
                json.dump(default_config, file, indent=4)
                print(f"File '{self.config_file_path}' created with default config.")

        with open(self.config_file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def generate_random_string(length: int) -> str:
        """Generate a random string of the given length."""
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of Config."""
        if cls._instance is None:
            cls._instance = cls()  # Create the instance if it doesn't exist
        return cls._instance


# Usage in the project
config = Config()
print("Users loaded:", config.users)
