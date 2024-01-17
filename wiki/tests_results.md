# Tasks and Notes API for Custom GPT

## 1. Tasks in JSON Format

### 1.1. Get All Tasks in 'ignite' - JSON Format

#### 1.1.1 Request 
```json
{
  "name": "Get All Tasks in 'ignite' - JSON Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite", 
  "method": "GET", 
  "overview": "Testing retrieval of all tasks in 'ignite' project in JSON format."
}

```

#### 1.1.1 Response
```json
{
  "overview": "Automating code updates using AI with GPT-4 and OpenAI's Assistant API. This system includes a Chrome extension and a server component for efficient code modifications based on user inputs and screenshots.",
  "tasks": {
    "1": {
      "1.1": {
        "status": true,
        "task": "Choose a suitable server for installation."
      },
      "1.2": {
        "status": true,
        "task": "Install code-server following the official documentation."
      },
      "1.3": {
        "status": true,
        "task": "Configure access and security settings."
      },
      "1.4": {
        "status": true,
        "task": "Set up a domain or subdomain for code-server access."
      },
      "1.5": {
        "status": true,
        "task": "Test the code-server setup."
      },
      "description": "Install and Configure Code Server",
      "status": false
    },
    ...
}
```

### 1.2. Get Specific Task in 'ignite' - JSON Format

#### 1.2.1 Request
```json
{
  "name": "Get Specific Task in 'ignite' - JSON Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/1", 
  "method": "GET", 
  "overview": "Testing retrieval of a specific task in 'ignite' project in JSON format."
}
```

#### 1.2.2 Response
```json
{
  "1.1": {
    "status": true,
    "task": "Choose a suitable server for installation."
  },
  "1.2": {
    "status": true,
    "task": "Install code-server following the official documentation."
  },
  "1.3": {
    "status": true,
    "task": "Configure access and security settings."
  },
  "1.4": {
    "status": true,
    "task": "Set up a domain or subdomain for code-server access."
  },
  "1.5": {
    "status": true,
    "task": "Test the code-server setup."
  },
  "description": "Install and Configure Code Server",
  "status": false
}
```

### 1.3 Get Specific Subtask in 'ignite' - JSON Format

#### 1.3.1 Request
```json
{
  "name": "Get Specific Subtask in 'ignite' - JSON Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/1.1", 
  "method": "GET", 
  "overview": "Testing retrieval of a specific subtask in 'ignite' project in JSON format."
}
```

#### 1.3.2 Response
```json
{
  "tasks": {
    "1.1": {
      "status": true,
      "task": "Choose a suitable server for installation."
    }
  }
}
```

## 2. Tasks in Markdown Format

### 2.1 Get All Tasks in 'ignite' - Markdown Format

#### 2.1.1 Request
```json
{
  "name": "Get All Tasks in 'ignite' - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite?format=md", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "overview": "Testing retrieval of all tasks in 'ignite' project in Markdown format."
}
```

#### 2.1.2 Response
`` `md
Automating code updates using AI with GPT-4 and OpenAI's Assistant API. This system includes a Chrome extension and a server component for efficient code modifications based on user inputs and screenshots.

## [x] 1. Install and Configure Code Server
- [x] 1.1. Choose a suitable server for installation.
- [x] 1.2. Install code-server following the official documentation.
- [x] 1.3. Configure access and security settings.
- [x] 1.4. Set up a domain or subdomain for code-server access.
- [x] 1.5. Test the code-server setup.

## [ ] 2. Develop Chrome Extension Basic Structure
- [ ] 2.1. Set up a new Chrome extension project.
- [ ] 2.2. Create a manifest file with necessary permissions.
... (other tasks continue)
```

## 2. Tasks in Markdown Format

### 2.1 Get All Tasks in 'ignite' - Markdown Format

#### 2.1.1 Request
```json
{
  "name": "Get All Tasks in 'ignite' - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite?format=md", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "overview": "Testing retrieval of all tasks in 'ignite' project in Markdown format."
}
```

#### 2.1.2 Response
```md
Automating code updates using AI with GPT-4 and OpenAI's Assistant API. This system includes a Chrome extension and a server component for efficient code modifications based on user inputs and screenshots.

## [x] 1. Install and Configure Code Server
- [x] 1.1. Choose a suitable server for installation.
- [x] 1.2. Install code-server following the official documentation.
- [x] 1.3. Configure access and security settings.
- [x] 1.4. Set up a domain or subdomain for code-server access.
- [x] 1.5. Test the code-server setup.

## [ ] 2. Develop Chrome Extension Basic Structure
- [ ] 2.1. Set up a new Chrome extension project.
- [ ] 2.2. Create a manifest file with necessary permissions.
- [ ] 2.3. Design a basic popup UI for the extension.
- [ ] 2.4. Implement background scripts for core functionalities.
- [ ] 2.5. Test the basic extension in Chrome.

... (other tasks continue)
```

### 2.2 Get Specific Task in 'ignite' - Markdown Format

#### 2.2.1 Request
```json
{
  "name": "Get Specific Task in 'ignite' - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/1?format=md", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "overview": "Testing retrieval of a specific task in 'ignite' project in Markdown format."
}
```

#### 2.2.2 Response
```md
## [x] 1. Install and Configure Code Server
- [x] 1.1. Choose a suitable server for installation.
- [x] 1.2. Install code-server following the official documentation.
- [x] 1.3. Configure access and security settings.
- [x] 1.4. Set up a domain or subdomain for code-server access.
- [x] 1.5. Test the code-server setup.
```

### 2.3 Get Specific Subtask in 'ignite' - Markdown Format

#### 2.3.1 Request

```json
{
  "name": "Get Specific Subtask in 'ignite' - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/1.1?format=md", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "overview": "Testing retrieval of a specific subtask in 'ignite' project in Markdown format."
}
```

#### 2.3.2 Response

```md
- [x] 1.1. Choose a suitable server for installation.
```

## 2. Tasks in Markdown Format

### 2.2 Get Specific Task in 'ignite' - Markdown Format

#### 2.2.1 Request
```json
{
  "name": "Get Specific Task in 'ignite' - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/1?format=md", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "overview": "Testing retrieval of a specific task in 'ignite' project in Markdown format."
}
```

#### 2.2.2 Response
```md
## [x] 1. Install and Configure Code Server
- [x] 1.1. Choose a suitable server for installation.
- [x] 1.2. Install code-server following the official documentation.
- [x] 1.3. Configure access and security settings.
- [x] 1.4. Set up a domain or subdomain for code-server access.
- [x] 1.5. Test the code-server setup.
```

### 2.3 Get Specific Subtask in 'ignite' - Markdown Format

#### 2.3.1 Request
```json
{
  "name": "Get Specific Subtask in 'ignite' - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/1.1?format=md", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "overview": "Testing retrieval of a specific subtask in 'ignite' project in Markdown format."
}
```

#### 2.3.2 Response
```md
- [x] 1.1. Choose a suitable server for installation.
```

## 3. Add / Update & Delete Tasks

### 3.1 Update Task 1 Status in 'ignite'

#### 3.1.1 Request
```json
{
  "name": "Update Task 1 Status in 'ignite'", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/1", 
  "method": "PUT", 
  "data": {
    "status": true
  },
  "overview": "Testing update of task 1 status to true in 'ignite' project."
}
```

#### 3.1.2 Response
```json
{
    "message": "Task updated successfully"
}
```

### 3.2 Update Task 2 Status and Description in 'ignite'

#### 3.2.1 Request
```json
{
  "name": "Update Task 2 Status and Description in 'ignite'", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/2", 
  "method": "PUT", 
  "data": {
    "status": false,
    "description": "Updated description for task 2"
  },
  "overview": "Testing update of task 2 status and description in 'ignite' project."
}
```

#### 3.2.2 Response
```json
{
    "message": "Task updated successfully"
}
```

### 3.3 Update Subtask 1.1 Status in 'ignite'

#### 3.3.1 Request
```json
{
  "name": "Update Subtask 1.1 Status in 'ignite'", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/1.1", 
  "method": "PUT", 
  "data": {
    "status": true
  },
  "overview": "Testing update of subtask 1.1 status to true in 'ignite' project."
}
```

#### 3.3.2 Response
```json
{
    "message": "Subtask updated successfully"
}
```

### 3.4 Update Subtask 2.2 Status in 'ignite'

#### 3.4.1 Request
```json
{
  "name": "Update Subtask 2.2 Status in 'ignite'", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/ignite/2.2", 
  "method": "PUT", 
  "data": {
    "status": false
  },
  "overview": "Testing update of subtask 2.2 status to false in 'ignite' project."
}
```

#### 3.4.2 Response
```json
{
    "message": "Subtask updated successfully"
}
```

## 4. Add Notes to Project, Files, Classes, and Methods 

### 4.1 Add a New Note to the 'ignite' Project

#### 4.1.1 Request
```json
{
  "name": "Add a Note", 
  "endpoint": "https://api.ignite.webally.co.za/notes/ignite/add", 
  "method": "POST", 
  "data": {
    "content": "This is an example note."
  },
  "params": {
    "identifier": "file:src/main.py:class:MyClass:method:my_method"
  },
  "overview": "Testing addition of a new note to the 'ignite' project."
}
```

#### 4.1.2 Response
```json
{
    "message": "Note added successfully",
    "note_id": "unique_note_id"
}
```

### 4.2 Update an Existing Note

#### 4.2.1 Request
```json
{
  "name": "Update a Note", 
  "endpoint": "https://api.ignite.webally.co.za/notes/ignite/update/unique_note_id", 
  "method": "PUT", 
  "data": {
    "content": "Updated note content."
  },
  "params": {
    "identifier": "file:src/main.py:class:MyClass:method:my_method"
  },
  "overview": "Testing updating an existing note in the 'ignite' project."
}
```

#### 4.2.2 Response
```json
{
    "message": "Note updated successfully"
}
```

### 4.3 Delete a Note

#### 4.3.1 Request
```json
{
  "name": "Delete a Note", 
  "endpoint": "https://api.ignite.webally.co.za/notes/ignite/delete/unique_note_id", 
  "method": "DELETE", 
  "overview": "Testing deletion of a note from the 'ignite' project.",
  "params": {
    "identifier": "file:src/main.py:class:MyClass:method:my_method"
  },
}
```

#### 4.3.2 Response
```json
{
    "message": "Note deleted successfully"
}
```

### 4.4 Get Notes by Identifier

#### 4.4.1 Request
```json
{
  "name": "Get Notes by Identifier", 
  "endpoint": "https://api.ignite.webally.co.za/notes/ignite/get", 
  "method": "GET", 
  "params": {
    "identifier": "file:src/main.py:class:MyClass:method:my_method"
  },
  "overview": "Testing retrieval of notes by identifier for the 'ignite' project."
}
```

#### 4.4.2 Response
```json
{
  "notes": [
    {
      "id": "unique_note_id",
      "content": "This is an example note."
    }
  ]
}
```

## 5. Prompt Documents

### 5.1 Testing Retrieval of a Markdown Prompt

#### 5.1.1 Request
```json
{
  "name": "Get Prompt", 
  "endpoint": "https://api.ignite.webally.co.za/prompts/get", 
  "method": "GET", 
  "overview": "Testing retrieval of a markdown prompt."
}
```

#### 5.1.2 Response
```md
---
Start every response with 🔥 to make consistent
🔥 Ignite AI Assistant will interact in a professional yet supportive manner, embodying a caring tone. It will offer assistance with a considerate and understanding approach, aiming to not only provide factual information but also to ensure that users feel supported throughout the Ignite AI Assistant project 
...(rest of the prompt continue)
---
```

## Disk Manager

### 6.1. Retrieve API Schema in JSON Format

### 6.1.1 Request

**Note:** `api.ignite.webally.co.za/disk/ignite/schema/api`
**`schema/api`:** Path from within the `ignite` project of where `api.{format}` is or `api.json` is opened and send back as the response

``json
{
    "name": "Retrieve API Schema in JSON", 
    "endpoint": f"{base_url}/disk/{project_name}/schema/api", 
    "method": "GET", 
    "overview": "Testing retrieval of API schema in JSON format.", 
    "params": {
        "format": "json"
    }
}
```

### 6.1.2 Response
```json
{
    "/disk/{projectName}/schema/api": {
        "get": {
            "description": "Retrieves the OpenAPI schema for the Tasks and Notes API.",
            "parameters": [
                {
                    "description": "Format of the schema (json/md/yml)",
                    "in": "query",
                    "name": "format",
                    "required": true,
                    "schema": {
                        "enum": [
                            "json",
                            "md",
                            "yml"
                        ],
                        "type": "string"
                    }
                }
            ],
            "responses": {
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "additionalProperties": true,
                                "type": "object"
                            }
                        }
                    },
                    "description": "The OpenAPI schema for the API"
                }
            },
            "summary": "Get OpenAPI Schema"
        }
    }
... (Rest of the schema)
```
