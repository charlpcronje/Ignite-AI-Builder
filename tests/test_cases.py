# test_cases.py
# Definition of individual API test cases

from test_config import endpoints
from test_config import endpoints, base_url


tests = [

    # Task Manager
    ## 1. Tasks in JSON Format 0-2
    
    ### 1.1 Get All Tasks in 'ignite' - JSON Format
    {"name": "Get All Tasks in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite", "method": "GET", "overview": "Testing retrieval of all tasks in 'ignite' project in JSON format."},
    
    ### 1.2 Get Specific Task in 'ignite' - JSON Format
    {"name": "Get Specific Task in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite/1", "method": "GET", "overview": "Testing retrieval of a specific task in 'ignite' project in JSON format."},
    
    ### 1.3 Get Specific Subtask in 'ignite' - JSON Format
    {"name": "Get Specific Subtask in 'ignite' - JSON Format", "endpoint": f"{base_url}/tasks/ignite/1.1", "method": "GET", "overview": "Testing retrieval of a specific subtask in 'ignite' project in JSON format."},
    
    ## 2. Tasks in Markdown, format=mdt 3-5
    
    ### 2.1 Get All Tasks in 'ignite' - Markdown Format
    {"name": "Get All Tasks in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of all tasks in 'ignite' project in Markdown format."},
    
    ### 2.2 Get Specific Task in 'ignite' - Markdown Format
    {"name": "Get Specific Task in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite/1?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of a specific task in 'ignite' project in Markdown format."},
    
    ### 2.3 Get Specific Subtask in 'ignite' - Markdown Format
    {"name": "Get Specific Subtask in 'ignite' - Markdown Format", "endpoint": f"{base_url}/tasks/ignite/1.1?format=md", "method": "GET", "params": {"format": "md"}, "overview": "Testing retrieval of a specific subtask in 'ignite' project in Markdown format."},

    ## 3. Update Tasks 6-9

    ### 3.1 Update Task 1 Status in 'ignite'
    {"name": "Update Task 1 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/1", "method": "PUT", "data": {"status": True}, "overview": "Testing update of task 1 status to true in 'ignite' project."},

    ### 3.2 Update Task 2 Status and Description in 'ignite
    {"name": "Update Task 2 Status and Description in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/2", "method": "PUT", "data": {"status": False, "description": "Updated description for task 2"}, "overview": "Testing update of task 2 status and description in 'ignite' project."},

    ### 3.3 Update Subtask 1.1 Status in 'ignite'
    {"name": "Update Subtask 1.1 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/1.1", "method": "PUT", "data": {"status": True}, "overview": "Testing update of subtask 1.1 status to true in 'ignite' project."},

    ### 3.1 Update Subtask 2.2 Status in 'ignite'
    {"name": "Update Subtask 2.2 Status in 'ignite'", "endpoint": f"{base_url}/tasks/ignite/2.2", "method": "PUT", "data": {"status": False}, "overview": "Testing update of subtask 2.2 status to false in 'ignite' project."},
   
    ## 4. Notes Manager
    ### 4.1 Note Tests 10-13
    {
        "name": "Add a Note", 
        "endpoint": f"{base_url}/notes/ignite/add", 
        "method": "POST", 
        "overview": "Testing addition of a new note to the 'ignite' project.", 
        "headers": {"X-API-Key": "_mu0WygMRETwooV39aj0PQ"},
        "data": {
            "content": "BEST 5"
        },
        "params": {
            "identifier": "<file:src/main.py>/<class:MyClass>/<method:my_method>"
        }
    },

    ### 4.2. Updating a Note (Note ID needs to be specified)
    {
        "name": "Update a Note", 
        "endpoint": f"{base_url}/notes/ignite/update/ace725e2-bf8d-4004-bf30-a4d47985a2fe", 
        "method": "PUT", 
        "overview": "Testing updating an existing note in the 'ignite' project.", 
        "headers": {"X-API-Key": "_mu0WygMRETwooV39aj0PQ"},
        "data": {
            "updates": {"content": "Updated note content AAAA"}
        },
        "params": {
            "identifier": "<file:src/main.py>/<class:MyClass>/<method:my_method>"
        }
    },

    ### 4.3. Deleting a Note (Note ID needs to be specified)
    {
        "name": "Delete a Note", 
        "endpoint": f"{base_url}/notes/ignite/delete/ace725e2-bf8d-4004-bf30-a4d47985a2fe", 
        "method": "DELETE", 
        "overview": "Testing deletion of a note from the 'ignite' project.", 
        "headers": {"X-API-Key": "_mu0WygMRETwooV39aj0PQ"},
        "params": {
            "identifier": "<file:src/main.py>/<class:MyClass>/<method:my_method>"
        }
    },

    ### 4.4. Getting Notes by Identifier
    {
        "name": "Get Notes by Identifier", 
        "endpoint": f"{base_url}/notes/ignite/get/", 
        "method": "GET", 
        "overview": "Testing retrieval of notes by identifier for the 'ignite' project.",
        "headers": {"X-API-Key": "_mu0WygMRETwooV39aj0PQ"},
        "params": {
            "identifier": "<file:src/main.py>/<class:MyClass>/<method:my_method>"
        }
    },

    ### 5.1. Testing prompt retrieval of a markdown prompt 14
    {
        "name": "Get Prompt", 
        "endpoint": f"{base_url}/prompts/get/", 
        "method": "GET", 
        "overview": "Testing retrieval of a markdown prompt.",
        "headers": {"X-API-Key": "_mu0WygMRETwooV39aj0PQ"}
    },

    ## 6. Disk Management 15-21
    ### 6.1. Retrieve API Schema in JSON Format
    {
        "name": "Retrieve API Schema in JSON", 
        "endpoint": f"{base_url}/disk/ignite/schema/api", 
        "method": "GET", 
        "overview": "Testing retrieval of API schema in JSON format.", 
        "params": {
            "format": "json"
        }
    },

    #### 6.2. Retrieve API Schema in Markdown Format
    {
        "name": "Retrieve API Schema in Markdown", 
        "endpoint": f"{base_url}/disk/ignite/schema/api", 
        "method": "GET", 
        "overview": "Testing retrieval of API schema in Markdown format.", 
        "params": {
            "format": "md"
        }
    },

    #### 6.3. Retrieve API Schema in YAML Format
    {
        "name": "Retrieve API Schema in YAML", 
        "endpoint": f"{base_url}/disk/ignite/schema/api", 
        "method": "GET", 
        "overview": "Testing retrieval of API schema in YAML format.", 
        "params": {
            "format": "yml"
        }
    },

    #### 6.4. Update API Schema in JSON Format
    {
        "name": "Update API Schema in JSON", 
        "endpoint": f"{base_url}/disk/ignite/schema/api", 
        "method": "PUT", 
        "overview": "Testing update of API schema in JSON format.", 
        "headers": {
            "Content-Type": "application/json"
        },
        "params": {
            "format": "json"
        },
        "data": {
            "new_schema_content": "Your JSON schema here"
        }
    },

    #### 6.5. Update API Schema in Markdown Format
    {
        "name": "Update API Schema in Markdown", 
        "endpoint": f"{base_url}/disk/ignite/schema/api", 
        "method": "PUT", 
        "overview": "Testing update of API schema in Markdown format.", 
        "headers": {
            "Content-Type": "text/plain"
        },
        "params": {
            "format": "md"
        },
        "data": {
            "content": "Your Markdown content here"
        }
    },

    ### 6.6. Update API Schema in YAML Format
    {
        "name": "Update API Schema in YAML", 
        "endpoint": f"{base_url}/disk/ignite/schema/api", 
        "method": "PUT", 
        "overview": "Testing update of API schema in YAML format.", 
        "headers": {
            "Content-Type": "text/plain"
        },
        "params": {
            "format": "yml"
        },
        "data": {
            "content": "Your YAML content here"
        }
    }


    ### Notes:
    # - Replace `{base_url}` and `{project_name}` with the appropriate values for your application.
    # - The `headers` key should be adjusted based on the content type you're sending or expecting (JSON, Markdown, YAML).
    # - The `data` field in the PUT requests should contain the new content that you want to write to the file. Make sure to format this content correctly depending on whether it's JSON, Markdown, or YAML.


    # 5.1 
    #{"name": "Get Prompt", "endpoint": endpoints["get_prompt"], "method": "GET", "overview": "Testing retrieval of a markdown prompt."},
    #{"name": "Get Tasks", "endpoint": endpoints["get_tasks"], "method": "GET", "overview": "Testing retrieval of tasks in Markdown format."},
    #{"name": "Get Specific Task", "endpoint": endpoints["get_specific_task"], "method": "GET", "overview": "Testing retrieval of a specific task in Markdown format."},
    #{"name": "Get Specific Subtask", "endpoint": endpoints["get_specific_subtask"], "method": "GET", "overview": "Testing retrieval of a specific subtask in Markdown format."},
    #{"name": "Invalid Task Retrieval", "endpoint": f"{base_url}/tasks/nonexistent_project", "method": "GET", "expected_status": 404, "overview": "Expected to fail due to a non-existent project name."},
]
