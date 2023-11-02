import requests
import logging
import pytest

logging.basicConfig(level=logging.INFO, filename='tests.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

def log_request_response(request, response):
    logging.info(f"Request method: {request.method}")
    logging.info(f"Request URL: {request.url}")
    logging.info(f"Request headers: {request.headers}")
    logging.info(f"Request body: {request.body}")
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response headers: {response.headers}")
    logging.info(f"Response body: {response.text}")

def test_create_post(base_url, post_data):
    logging.info("Starting test: test_create_post")
    url = f"{base_url}/posts"
    response = requests.post(url, json=post_data)
    log_request_response(response.request, response)
    
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    response_data = response.json()
    for key, value in post_data.items():
        assert response_data[key] == value, f"Expected {key} to be {value}, but got {response_data[key]}"
    logging.info("Test test_create_post passed.")

def test_get_posts(base_url):
    logging.info("Starting test: test_get_posts")
    url = f"{base_url}/posts"
    response = requests.get(url)
    log_request_response(response.request, response)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    logging.info("Test test_get_posts passed.")

def test_filter_posts(base_url, user_id):
    logging.info("Starting test: test_filter_posts")
    url = f"{base_url}/posts"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    log_request_response(response.request, response)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    response_data = response.json()
    for post in response_data:
        assert post["userId"] == user_id, f"Expected userId to be {user_id}, but got {post['userId']}"
    logging.info("Test test_filter_posts passed.")  