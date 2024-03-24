import requests


TEST_URL = 'http://127.0.0.1:5000/api/tasks'


def test_get_tasks():
    response = requests.get(TEST_URL)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_task_by_id():
    response = requests.get(f'{TEST_URL}/1')
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        data = response.json()
        assert 'title' in data


def test_create_task():
    task_data = {'title': 'New Task'}
    response = requests.post(TEST_URL, json=task_data)
    assert response.status_code == 201
    assert 'title' in response.json()
    assert response.json()['title'] == task_data['title']
