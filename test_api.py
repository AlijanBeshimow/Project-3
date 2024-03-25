import requests


TEST_URL = 'http://127.0.0.1:5000/api/tasks'


# TESTING VIEW ALL TASKS
def test_get_tasks():
    response = requests.get(TEST_URL)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data['tasks'], list)


# TESTING GET TASK BY ID
def test_get_task_by_id():
    response = requests.get(f'{TEST_URL}/1')
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        data = response.json()
        assert 'title' in data
        assert 'description' in data
        assert 'category' in data


# TESTING CREATE
def test_create_task():
    task_data = {'title': 'New Task'}
    response = requests.post(TEST_URL, json=task_data)
    assert response.status_code == 201
    assert 'message' in response.json()
    assert response.json()['message'] == 'Task added successfully'


# TESTING UPDATE
def test_update_task():
    task_id = 1
    updated_task_data = {'title': 'Updated Task Title',
                         'description': 'Updated Task Description', 'category': 'Updated Category'}
    response = requests.put(f'{TEST_URL}/{task_id}', json=updated_task_data)
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()['message'] == 'Task updated successfully'


# TESTING DELETE
def test_delete_task():
    task_id = 1
    response = requests.delete(f'{TEST_URL}/{task_id}')
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert response.json()['message'] == 'Task deleted successfully'
