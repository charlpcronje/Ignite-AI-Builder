# test_cases.py
# Definition of individual API test cases

from test_config import endpoints
from test_config import endpoints, base_url

tests = [
    ## Task endpoint tests for 'ignite' project without format=md
    # 1. Tasks in JSON Format
    # 1.1. Get All Tasks in 'ignite' - JSON Format
    {"name": "Get All Tasks in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite", "method": "GET", "overview": "Testing retrieval of all tasks in 'ignite' project in JSON format."},
    # 1.2. Get Specific Task in 'ignite' - JSON Format
    {"name": "Get Specific Task in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite/1", "method": "GET", "overview": "Testing retrieval of a specific task in 'ignite' project in JSON format."},
    # 1.3 Get Specific Subtask in 'ignite' - JSON Format
    {"name": "Get Specific Subtask in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite/1.1", "method": "GET", "overview": "Testing retrieval of a specific subtask in 'ignite' project in JSON format."},
    
    ## Task endpoint tests for 'ignite' project with format=md
    # 2. Tasks in Markdown Format
    # 2.1. Get All Tasks in 'ignite' - Markdown Format
    {"name": "Get All Tasks in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of all tasks in 'ignite' project in Markdown format."},
    # 2.2. "Get Specific Task in 'ignite' - Markdown Format
    {"name": "Get Specific Task in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite/1?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of a specific task in 'ignite' project in Markdown format."},
    # 2.3. Get Specific Subtask in 'ignite' - Markdown Format
    {"name": "Get Specific Subtask in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite/1.1?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of a specific subtask in 'ignite' project in Markdown format."},

    # 3 Update Tasks
    # 3.1. Testing update of task 1 status to true in 'ignite' project.
    {"name": "Update Task 1 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/1", "method": "PUT", "data": {"status": True}, "overview": "Testing update of task 1 status to true in 'ignite' project."},
    # 3.2. Testing update of task 1 status to true in 'ignite' project.   
    {"name": "Update Task 2 Status and Description in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/2", "method": "PUT", "data": {"status": False, "description": "Updated description for task 2"}, "overview": "Testing update of task 2 status and description in 'ignite' project."},
    # 3.3. Testing update of subtask 1.1 status to true in 'ignite' project.
    {"name": "Update Subtask 1.1 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/1.1", "method": "PUT", "data": {"status": True}, "overview": "Testing update of subtask 1.1 status to true in 'ignite' project."},
    # 3.4. Testing update of subtask 2.2 status to false in 'ignite' project.
    {"name": "Update Subtask 2.2 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/2.2", "method": "PUT", "data": {"status": False}, "overview": "Testing update of subtask 2.2 status to false in 'ignite' project."},

    # 4. Notes
    # 4.1. Testing retrieval of notes in Markdown format.
    {"name": "Get Notes", "endpoint": endpoints["get_notes"], "method": "GET", "overview": "Testing retrieval of notes in Markdown format."},
    # 4.2. Testing addition of a new note.
    {"name": "Add Note", "endpoint": endpoints["add_note"], "method": "POST", "data": {"content": "Example note", "level": "project"}, "overview": "Testing addition of a new note."},
    # 4.3. Testing update of an existing note.
    {"name": "Update Note", "endpoint": endpoints["update_note"], "method": "PUT", "data": {"note_id": "1", "content": "Updated note content", "level": "project"}, "overview": "Testing update of an existing note."},
    # 4.4. Testing deletion of a note.
    {"name": "Delete Note", "endpoint": endpoints["delete_note"], "method": "DELETE", "data": {"note_id": "1", "level": "project"}, "overview": "Testing deletion of a note."},
    
    # 4.5. Testing prompt retrieval of a markdown prompt
    {"name": "Get Prompt", "endpoint": f"{base_url}/prompts/ignite", "method": "GET", "overview": "Testing retrieval of a markdown prompt."},
    {"name": "Get Prompt", "endpoint": endpoints["get_prompt"], "method": "GET", "overview": "Testing retrieval of a markdown prompt."},
    {"name": "Get Tasks", "endpoint": endpoints["get_tasks"], "method": "GET", "overview": "Testing retrieval of tasks in Markdown format."},
    {"name": "Get Specific Task", "endpoint": endpoints["get_specific_task"], "method": "GET", "overview": "Testing retrieval of a specific task in Markdown format."},
    {"name": "Get Specific Subtask", "endpoint": endpoints["get_specific_subtask"], "method": "GET", "overview": "Testing retrieval of a specific subtask in Markdown format."},
    {"name": "Invalid Task Retrieval", "endpoint": f"{base_url}/tasks/nonexistent_project", "method": "GET", "expected_status": 404, "overview": "Expected to fail due to a non-existent project name."},

    {"name": "Invalid Note Addition", "endpoint": f"{base_url}/notes/nonexistent_project/add", "method": "POST", "data": {"content": "Invalid note", "level": "project"}, "expected_status": 404, "overview": "Expected to fail as the project doesn't exist."},
    {"name": "Invalid Note Update", "endpoint": f"{base_url}/notes/ignite/update", "method": "PUT", "data": {"content": "Updated note content", "level": "project"}, "expected_status": 400, "overview": "Fails due to missing or invalid note ID."},
    {"name": "Invalid Note Deletion", "endpoint": f"{base_url}/notes/ignite/delete", "method": "DELETE", "expected_status": 400, "overview": "Fails due to missing or invalid note ID."},

    {"name": "Invalid Prompt Retrieval", "endpoint": f"{base_url}/prompts/nonexistent_project", "method": "GET", "expected_status": 404, "overview": "Expected to fail due to a non-existent project name."},
    {"name": "Invalid Task Retrieval with Incorrect Task Number", "endpoint": f"{base_url}/tasks/ignite/nonexistent_task", "method": "GET", "expected_status": 404, "overview": "Fails due to non-existent task number."},
    {"name": "Invalid Subtask Retrieval with Incorrect Subtask Number", "endpoint": f"{base_url}/tasks/ignite/1/nonexistent_subtask", "method": "GET", "expected_status": 404, "overview": "Fails due to non-existent subtask number."}
]
