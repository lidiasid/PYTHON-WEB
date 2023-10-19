import pytest
import requests
import yaml

@pytest.fixture(scope="session")
def auth_token():
    with open("config.yaml", 'r') as f:
        config = yaml.safe_load(f)

    login_url = f"{config['base_url']}/gateway/login"
    login_data = {
        "username": config['username'],
        "password": config['password']
    }

    response = requests.post(login_url, json=login_data)

    if response.status_code != 200:
        print(f"Не удалось войти, код состояния: {response.status_code}, сообщение: {response.text}")
        raise Exception("Failed to get auth token")

    token = response.json().get('token')

    if not token:
        raise Exception("Failed to get auth token")

    return token
