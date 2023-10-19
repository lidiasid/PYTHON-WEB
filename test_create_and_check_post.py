import pytest
import requests
import yaml

# Создание нового поста и проверка его наличия
def test_create_and_check_post(auth_token, config_data):
    create_post_url = f"{config_data['base_url']}/api/posts"
    headers = {'Authorization': f'Bearer {auth_token}'}
    
    post_data = {
        "title": "New Post Title",
        "description": "New Post Description",
        "content": "New Post Content"
    }
    
    # Создание нового поста
    response = requests.post(create_post_url, json=post_data, headers=headers)
    assert response.status_code == 201
    
    post_id = response.json().get("id")
    
    # Получение списка всех постов для проверки наличия созданного
    all_posts_url = f"{config_data['base_url']}/api/posts"
    response = requests.get(all_posts_url, headers=headers)
    assert response.status_code == 200
    
    posts = response.json()
    
    # Поиск созданного поста по его описанию
    assert any(post for post in posts if post.get("id") == post_id and post.get("description") == "New Post Description")
