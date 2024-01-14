# test_cases.py
# Definition of individual API test cases

from test_config import endpoints
from test_config import endpoints, base_url


tests = [

    ## Task endpoint tests for 'ignite' project without format=md
    # 1. Tasks in JSON Format 0-2
    {"name": "Get All Tasks in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite", "method": "GET", "overview": "Testing retrieval of all tasks in 'ignite' project in JSON format."},
    {"name": "Get Specific Task in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite/1", "method": "GET", "overview": "Testing retrieval of a specific task in 'ignite' project in JSON format."},
    {"name": "Get Specific Subtask in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite/1.1", "method": "GET", "overview": "Testing retrieval of a specific subtask in 'ignite' project in JSON format."},
    
    ## Task endpoint tests for 'ignite' project with format=md
    # 2. Tasks in Markdown Format 3-5
    {"name": "Get All Tasks in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of all tasks in 'ignite' project in Markdown format."},
    {"name": "Get Specific Task in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite/1?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of a specific task in 'ignite' project in Markdown format."},
    {"name": "Get Specific Subtask in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite/1.1?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of a specific subtask in 'ignite' project in Markdown format."},

    # 3. Update Tasks 6-9
    {"name": "Update Task 1 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/1", "method": "PUT", "data": {"status": True}, "overview": "Testing update of task 1 status to true in 'ignite' project."},
    {"name": "Update Task 2 Status and Description in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/2", "method": "PUT", "data": {"status": False, "description": "Updated description for task 2"}, "overview": "Testing update of task 2 status and description in 'ignite' project."},
    {"name": "Update Subtask 1.1 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/1.1", "method": "PUT", "data": {"status": True}, "overview": "Testing update of subtask 1.1 status to true in 'ignite' project."},
    {"name": "Update Subtask 2.2 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/2.2", "method": "PUT", "data": {"status": False}, "overview": "Testing update of subtask 2.2 status to false in 'ignite' project."},
   
   
    # 4. Note Tests 10-12
    {"name": "Update a Note", "endpoint": f"{base_url}/api/notes/update/{note_id}", "method": "PUT", "overview": "Testing updating an existing note.", "data": {"identifier": "src/main.py>MyClass>my_method", "updates": {"content": "Updated content"}}},
    {"name": "Delete a Note", "endpoint": f"{base_url}/api/notes/delete/{note_id}", "method": "DELETE", "overview": "Testing deletion of a note.", "data": {"identifier": "src/main.py>MyClass>my_method"}},
    {"name": "Get Notes by Identifier", "endpoint": f"{base_url}/api/notes/src/main.py>MyClass", "method": "GET", "overview": "Testing retrieval of notes by identifier."},
    
    # 4.5. Testing prompt retrieval of a markdown prompt 13-18
    {"name": "Get Prompt", "endpoint": f"{base_url}/prompts/ignite", "method": "GET", "overview": "Testing retrieval of a markdown prompt."},
    {"name": "Get Prompt", "endpoint": endpoints["get_prompt"], "method": "GET", "overview": "Testing retrieval of a markdown prompt."},
    {"name": "Get Tasks", "endpoint": endpoints["get_tasks"], "method": "GET", "overview": "Testing retrieval of tasks in Markdown format."},
    {"name": "Get Specific Task", "endpoint": endpoints["get_specific_task"], "method": "GET", "overview": "Testing retrieval of a specific task in Markdown format."},
    {"name": "Get Specific Subtask", "endpoint": endpoints["get_specific_subtask"], "method": "GET", "overview": "Testing retrieval of a specific subtask in Markdown format."},
    {"name": "Invalid Task Retrieval", "endpoint": f"{base_url}/tasks/nonexistent_project", "method": "GET", "expected_status": 404, "overview": "Expected to fail due to a non-existent project name."},
]
