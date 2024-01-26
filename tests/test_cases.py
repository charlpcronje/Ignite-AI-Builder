# test_cases.py
# Definition of individual API test cases

from test_config import endpoints, base_url, api_key, project_name

"""
project_name = "ignite"
api_key = "_mu0WygMRETwooV39aj0PQ"
base_url = "https://api.ignite.webally.co.za"    
"""

tests = [

    # Task Manager
    ## 1. Tasks in JSON Format 0-2
    
    ### 1.1 Get All Tasks in 'ignite' - JSON Format (Test 0)
    {
        "name": f"Get All Tasks in '{project_name}' - JSON Format", 
        "endpoint": f"{base_url}/tasks/{project_name}", 
        "method": "GET", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "overview": f"Testing retrieval of all tasks in '{project_name}' project in JSON format."
    },
    
    ### 1.2 Get Specific Task in 'ignite' - JSON Format (Test 1)
    {
        "name": f"Get Specific Task in '{project_name}' - JSON Format", 
        "endpoint": f"{base_url}/tasks/{project_name}/1", 
        "method": "GET", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "overview": f"Testing retrieval of a specific task in '{project_name}' project in JSON format."
    },
    
    ### 1.3 Get Specific Subtask in 'ignite' - JSON Format (Test 2)
    {
        "name": f"Get Specific Subtask in '{project_name}' - JSON Format", 
        "endpoint": f"{base_url}/tasks/{project_name}/1.1", 
        "method": "GET", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "overview": f"Testing retrieval of a specific subtask in '{project_name}' project in JSON format."
    },
    
    ## 2. Tasks in Markdown, format=mdt 3-5
    
    ### 2.1 Get All Tasks in 'ignite' - Markdown Format (Test 3)
    {
        "name": f"Get All Tasks in '{project_name}' - Markdown Format", 
        "endpoint": f"{base_url}/tasks/{project_name}?format=md", 
        "method": "GET", 
        "params": {
            "format": "md"
        }, 
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"{api_key}"
        },
        "overview": f"Testing retrieval of all tasks in '{project_name}' project in Markdown format."
    },
    
    ### 2.2 Get Specific Task in 'ignite' - Markdown Format (Test 4)
    {
        "name": f"Get Specific Task in '{project_name}' - Markdown Format", 
        "endpoint": f"{base_url}/tasks/{project_name}/1?format=md", 
        "method":"GET", 
        "params": {
            "format": "md"
        }, 
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"{api_key}"
        },
        "overview": f"Testing retrieval of a specific task in '{project_name}' project in Markdown format."
    },
    
    ### 2.3 Get Specific Subtask in 'ignite' - Markdown FormatD (Test 5)
    {
        "name": f"Get Specific Subtask in '{project_name}' - Markdown Format", 
        "overview": f"Testing retrieval of a specific subtask in '{project_name}' project in Markdown format.",
        "endpoint": f"{base_url}/tasks/{project_name}/1.1?format=md", 
        "method": "GET", 
        "params": {
            "format": "md"
        },
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"{api_key}",
        }
    },

    ## 3. Update Tasks 6-9

    ### 3.1 Update Task 1 Status in 'ignite' (Test 6)
    {
        "name": f"Update Task 1 Status in '{project_name}'", 
        "overview": f"Testing update of task 1 status to true in '{project_name}' project.",
        "endpoint": f"{base_url}/tasks/{project_name}/1", 
        "method": "PUT", 
        "data": {
            "status": True
        },
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        
    },

    ### 3.2 Update Task 2 Status and Description in 'ignite' (Test 7)
    {
        "name": f"Update Task 2 Status and Description in '{project_name}'",
        "overview": f"Testing update of task 2 status and description in '{project_name}' project.", 
        "endpoint": f"{base_url}/tasks/{project_name}/2", 
        "method": "PUT", 
        "data": {
            "status": False, 
            "description": "Updated description for task 2"
        }, 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        }
    },

    ### 3.3 Update Subtask 1.1 Status in 'ignite' (Test 8)
    {
        "name": f"Update Subtask 1.1 Status in '{project_name}'", 
        "overview": f"Testing update of subtask 1.1 status to true in '{project_name}' project.",
        "endpoint": f"{base_url}/tasks/{project_name}/1.1", 
        "method": "PUT", 
        "data": {
            "status": True
        },
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        }
    },

    ### 3.1 Update Subtask 2.2 Status in 'ignite' (Test 9)
    {
        "name": f"Update Subtask 2.2 Status in '{project_name}'", 
        "overview":f"Testing update of subtask 2.2 status to false in '{project_name}' project.",
        "endpoint": f"{base_url}/tasks/{project_name}/2.2", 
        "method": "PUT", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "data": {
            "status": False
        }
    },
   
    ## 4. Notes Manager
    ### 4.1 Note Tests 10-13 (Test 10)
    {
        "name": f"Add a Note to a project {project_name}", 
        "overview": f"Testing addition of a new note to the '{project_name}' project.",
        "endpoint": f"{base_url}/notes/{project_name}/add", 
        "method": "POST", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "data": {
            "content": "BEST 5"
        },
        "params": {
            "identifier": "<file:src/main.py>/<class:MyClass>/<method:my_method>"
        }
    },

    ### 4.2. Updating a Note (Note ID needs to be specified) (Test 11)
    {
        "name": f"Update a Note by Note ID to project {project_name}", 
        "overview": "Testing updating an existing note in the '{project_name}' project.",
        "endpoint": f"{base_url}/notes/{project_name}/update/ace725e2-bf8d-4004-bf30-a4d47985a2fe", 
        "method": "PUT", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "data": {
            "updates": {
                "content": "Updated note content AAAA"
            }
        },
        "params": {
            "identifier": "<file:src/main.py>/<class:MyClass>/<method:my_method>"
        }
    },

    ### 4.3. Deleting a Note (Note ID needs to be specified) (Test 12)
    {
        "name": f"Delete a Note by Note ID to project {project_name}", 
        "overview": f"Testing deletion of a note from the '{project_name}' project.",
        "endpoint": f"{base_url}/notes/{project_name}/delete/ace725e2-bf8d-4004-bf30-a4d47985a2fe", 
        "method": "DELETE", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "format": "json",
            "identifier": "<file:src/main.py>/<class:MyClass>/<method:my_method>"
        }
    },

    ### 4.4. Getting Notes by Identifier (Test 13)
    {
        "name": "Get Notes by Identifier", 
        "overview": f"Testing retrieval of notes by identifier for the '{project_name}' project.",
        "endpoint": f"{base_url}/notes/{project_name}/get/", 
        "method": "GET", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "identifier": "<file:src/main.py>/<class:MyClass>/<method:my_method>"
        },
        "params": {
            "format": "json"
        }
    },

    ### 5.1. Testing prompt retrieval of a markdown prompt (Test 14)
    {
        "name": "Get Prompt", 
        "overview": f"Testing retrieval of a markdown prompt.",
        "endpoint": f"{base_url}/prompts/get/", 
        "method": "GET", 
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "format": "json"
        }
    },

    ## 6. Disk Management 15-21
    ### 6.1. Retrieve API Schema in JSON Format (Test 15)
    {
        "name": "Retrieve API Schema in JSON", 
        "overview": "Testing retrieval of API schema in JSON format.",
        "endpoint": f"{base_url}/disk/{project_name}/schema/api", 
        "method": "GET", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "format": "json"
        }
    },

    ### 6.2. Retrieve API Schema in JSON Format (Test 16)
    {
        "name": "Retrieve API Schema in JSON",
        "overview": "Testing retrieval of Privacy Policy in Markdown format.",
        "endpoint": f"{base_url}/disk/{project_name}/docs/privacy-policy",
        "method": "GET", 
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"_mu0WygMRETwooV39aj0PQ"
        },
        "params": {
            "format": "md"
        }
    },

    #### 6.3. Retrieve API Schema in Markdown Format (Test 17)
    {
        "name": "Retrieve API Schema in Markdown", 
        "overview": f"Testing retrieval of API schema for '{project_name}' in Markdown format.",
        "endpoint": f"{base_url}/disk/{project_name}/schema/api", 
        "method": "GET", 
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "format": "md"
        }
    },

    #### 6.4. Retrieve API Schema in YAML Format (Test 18)
    {
        "name": "Retrieve API Schema in YAML for '{project_name}'", 
        "overview": "Testing retrieval of API schema in YAML format.", 
        "endpoint": f"{base_url}/disk/{project_name}/schema/api", 
        "method": "GET", 
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "format": "yml"
        }
    },

    #### 6.5. Update API Schema in JSON Format (Test 19)
    {
        "name": f"Update API Schema in JSON for {project_name}", 
        "overview": "Testing update of API schema in JSON format.",
        "endpoint": f"{base_url}/disk/{project_name}/schema/api", 
        "method": "PUT", 
        "headers": {
            "Content-Type": "application/json",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "format": "json"
        },
        "data": {
            "new_schema_content": "Your JSON schema here"
        }
    },

    #### 6.6. Update API Schema in Markdown Format (Test 20)
    {
        "name": f"Update API Schema in Markdown for {project_name}", 
        "overview": "Testing update of API schema in Markdown format.", 
        "endpoint": f"{base_url}/disk/{project_name}/schema/api", 
        "method": "PUT", 
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "format": "md"
        },
        "data": {
            "content": "Your Markdown content here"
        }
    },

    ### 6.7. Update API Schema in YAML Format (Test 21)
    {
        "name": f"Update API Schema in YAML for {project_name}",
        "overview": "Testing update of API schema in YAML format.",
        "endpoint": f"{base_url}/disk/{project_name}/schema/api", 
        "method": "PUT", 
        "headers": {
            "Content-Type": "text/plain",
            "X-API-Key": f"{api_key}"
        },
        "params": {
            "format": "yml"
        },
        "data": {
            "content": "Your YAML content here"
        }
    }
]
