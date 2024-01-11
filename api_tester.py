# api_tester.py
import requests
import json

# API Base URL
base_url = "https://api.ignite.webally.co.za"

# API Endpoints to test
endpoints = {
    "get_notes": f"{base_url}/notes/ignite?format=md",
    "add_note": f"{base_url}/notes/ignite/add",
    "update_note": f"{base_url}/notes/ignite/update",
    "delete_note": f"{base_url}/notes/ignite/delete",
    "get_prompt": f"{base_url}/prompts/ignite?format=md",
    "get_tasks": f"{base_url}/tasks/ignite?format=md",
    "get_specific_task": f"{base_url}/tasks/ignite/1?format=md",
    "get_specific_subtask": f"{base_url}/tasks/ignite/1/1?format=md"
}

# API Key
api_key = "_mu0WygMRETwooV39aj0PQ"

# Markdown Log File
log_file = "api_test_log.md"

def test_endpoint(name, url, method, data=None, params=None, overview="", expected_status=200):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    response = None

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, json=data, headers=headers)

        if response and response.status_code == expected_status:
            log_response(name, url, response, overview)
        else:
            log_error(name, url, response, expected_status, overview)
    except Exception as e:
        log_exception(name, url, e, overview)

def log_response(name, url, response, overview):
    with open(log_file, "a") as file:
        file.write(f"# {name}\n\n")
        file.write(f"## Overview\n{overview}\n\n")
        file.write(f"### Endpoint: {url}\n")
        file.write("```json\n")
        file.write(json.dumps(response.json(), indent=2) if response else "No response")
        file.write("\n```\n\n")

def log_error(name, url, response, expected_status, overview):
    with open(log_file, "a") as file:
        file.write(f"# Error: {name}\n\n")
        file.write(f"## Overview\n{overview}\n\n")
        file.write(f"### Endpoint: {url}\n")
        file.write(f"### Expected Status: {expected_status}\n")
        file.write(f"### Actual Status: {response.status_code if response else 'No Response'}\n")
        file.write("```json\n")
        file.write(json.dumps(response.json(), indent=2) if response else "No response")
        file.write("\n```\n\n")

def log_exception(name, url, exception, overview):
    with open(log_file, "a") as file:
        file.write(f"# Exception: {name}\n\n")
        file.write(f"## Overview\n{overview}\n\n")
        file.write(f"### Endpoint: {url}\n")
        file.write(f"### Exception: {str(exception)}\n\n")

# Test each endpoint
test_endpoint("Get Notes", endpoints["get_notes"], "GET", overview="Testing retrieval of notes in Markdown format.")

# Test each endpoint
test_endpoint("Add Note", endpoints["add_note"], "POST", {"content": "Example note", "level": "project"}, overview="Testing addition of a new note.")

# Test each endpoint
test_endpoint("Update Note", endpoints["update_note"], "PUT", {"note_id": "1", "content": "Updated note content", "level": "project"}, overview="Testing update of an existing note.")

# Test each endpoint
test_endpoint("Delete Note", endpoints["delete_note"], "DELETE", {"note_id": "1", "level": "project"}, overview="Testing deletion of a note.")

# Test each endpoint
test_endpoint("Get Prompt", endpoints["get_prompt"], "GET", overview="Testing retrieval of a markdown prompt.")

# Test each endpoint
test_endpoint("Get Tasks", endpoints["get_tasks"], "GET", overview="Testing retrieval of tasks in Markdown format.")

# Test each endpoint
test_endpoint("Get Specific Task", endpoints["get_specific_task"], "GET", overview="Testing retrieval of a specific task in Markdown format.")

# Test each endpoint
test_endpoint("Get Specific Subtask", endpoints["get_specific_subtask"], "GET", overview="Testing retrieval of a specific subtask in Markdown format.")

# Testing retrieval of notes in Markdown format.
test_endpoint("Get Notes", endpoints["get_notes"], "GET", overview="Testing retrieval of notes in Markdown format.")

# Testing addition of a new note.
test_endpoint("Add Note", endpoints["add_note"], "POST", {"content": "Example note", "level": "project"}, overview="Testing addition of a new note.")

# Testing update of an existing note.
test_endpoint("Update Note", endpoints["update_note"], "PUT", {"note_id": "1", "content": "Updated note content", "level": "project"}, overview="Testing update of an existing note.")

# Testing deletion of a note.
test_endpoint("Delete Note", endpoints["delete_note"], "DELETE", {"note_id": "1", "level": "project"}, overview="Testing deletion of a note.")

# Testing retrieval of a markdown prompt.
test_endpoint("Get Prompt", endpoints["get_prompt"], "GET", overview="Testing retrieval of a markdown prompt.")

# Testing retrieval of tasks in Markdown format.
test_endpoint("Get Tasks", endpoints["get_tasks"], "GET", overview="Testing retrieval of tasks in Markdown format.")

# Testing retrieval of a specific task in Markdown format.
test_endpoint("Get Specific Task", endpoints["get_specific_task"], "GET", overview="Testing retrieval of a specific task in Markdown format.")

# Testing retrieval of a specific subtask in Markdown format.
test_endpoint("Get Specific Subtask", endpoints["get_specific_subtask"], "GET", overview="Testing retrieval of a specific subtask in Markdown format.")

# Testing retrieval of a task from a non-existent project - expected to fail.
test_endpoint("Invalid Task Retrieval", f"{base_url}/tasks/nonexistent_project", "GET", expected_status=404, overview="Expected to fail due to a non-existent project name.")

# Testing addition of a note to a non-existent project - expected to fail.
test_endpoint("Invalid Note Addition", f"{base_url}/notes/nonexistent_project/add", "POST", {"content": "Invalid note", "level": "project"}, expected_status=404, overview="Expected to fail as the project doesn't exist.")

# Testing update of a note with missing or invalid note ID - expected to fail.
test_endpoint("Invalid Note Update", f"{base_url}/notes/ignite/update", "PUT", {"content": "Updated note content", "level": "project"}, expected_status=400, overview="Fails due to missing or invalid note ID.")

# Testing deletion of a note with missing or invalid note ID - expected to fail.
test_endpoint("Invalid Note Deletion", f"{base_url}/notes/ignite/delete", "DELETE", expected_status=400, overview="Fails due to missing or invalid note ID.")

# Testing retrieval of a prompt from a non-existent project - expected to fail.
test_endpoint("Invalid Prompt Retrieval", f"{base_url}/prompts/nonexistent_project", "GET", expected_status=404, overview="Expected to fail due to a non-existent project name.")

# Testing retrieval of a task with a non-existent task number - expected to fail.
test_endpoint("Invalid Task Retrieval with Incorrect Task Number", f"{base_url}/tasks/ignite/nonexistent_task", "GET", expected_status=404, overview="Fails due to non-existent task number.")

# Testing retrieval of a subtask with a non-existent subtask number - expected to fail.
test_endpoint("Invalid Subtask Retrieval with Incorrect Subtask Number", f"{base_url}/tasks/ignite/1/nonexistent_subtask", "GET", expected_status=404, overview="Fails due to non-existent subtask number.")