## 1. Tasks in JSON Format

### 1.1. Get tasks

#### 1.1.1 Request 
##### Request Description
Get all tasks by `{project}` - JSON Format

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
```json
{
  "name": "Get all tasks by `{project}` - JSON Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}", 
  "method": "GET", 
  "headers": {
      "Content-Type": "application/json",
      "X-API-Key": "{api_key}"
  },
  "description": "Retrieve of all tasks by `{project}` in JSON format."
}
```

#### 1.1.2 Response
In Their response, the `overview` field is a string that contains the `overview` of the project. The `tasks` field is a `JSON` object that contains the tasks. The `task` field is a string that contains the task. The `status` field is a `boolean` that indicates whether the task has been completed or not. Every task has a number, each project's tasks starts at number `1` and `sub-tasks` with decimal numbers like `1.1` is a sub task of task `1`
```json
{
  "overview": "{overview}",
  "tasks": {
    "{task_number}": {
      "task": "{task}",
      "status": {status},
      "{sub-task_number}": {
        "status": {status},
        "task": "{task}"
      },
      "{sub-task_number}": {
        "status": {status},
        "task": "{task}"
      }
    }
  }
}

// With actual data
{
  "overview": "Project Overview",
  "tasks": {
    "1": {
      "task": "Description for task 1",
      "status": false,
      "1.1": {
        "status": true,
        "task": "Description for task 1.1"
      },
      "1.2": {
        "status": true,
        "task": "Description for task 1.2"
      }
    },
    "2": {
      "task": "Description for task 2",
      "status": false,
      "2.1": {
        "status": true,
        "task": "Description for task 2.1"
      },
      "2.2": {
        "status": true,
        "task": "Description for task 2.2"
      },
      "2.3": {
        "status": true,
        "task": "Description for task 2.3"
      }
    }
  }
}
```

### 1.2. Get Specific Task by `{project}` and `{task_number}` - JSON Format

#### 1.2.1 Request
##### Request Description
Get Specific Task by `{project}` and `{task_number}` - JSON Format

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
task_number : 1
```json
{
  "name": "Get Specific Task by `{project}` and `{task_number}` - JSON Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}/{task_number}", 
  "method": "GET", 
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Retrieve a specific task in `{project}` and `{task_number}` in JSON format."
}
```

#### 1.2.2 Response
```json
{
  "task": "Task Description 1",
  "status": false,
  "1.1": {
    "status": true,
    "task": "Description for task 1.1"
  },
  "1.2": {
    "status": true,
    "task": "Description for task 1.2"
  },
  "1.3": {
    "status": true,
    "task": "Description for task 1.3"
  }
}
```

### 1.3 Get Specific Subtask by `{project}` and `{sub_task_number}` - JSON Format

#### 1.3.1 Request
##### Request Description
Get Specific Subtask by `{project}` and `{sub_task_number}` - JSON Format

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
sub_task_number : 1.1
```json
{
  "name": "Get Specific Subtask by `{project}` and `{sub_task_number}` - JSON Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}/{sub_task_number}", 
  "method": "GET",
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Retrieval of a specific subtask in `{project}` and `{sub_task_number}` in JSON format."
}
```

#### 1.3.2 Response
```json
{
  "tasks": {
    "1.1": {
      "status": true,
      "task": "Description for task 1.1"
    }
  }
}
```

## 2. Tasks in Markdown Format

### 2.1 Get All Tasks in `{project}` - Markdown Format

#### 2.1.1 Request
##### Request Description
Get All Tasks in `{project}` - Markdown Format

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
```json
{
  "name": "Get All Tasks in `{project}` - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "headers": {
    "Content-Type": "text/markdown",
    "X-API-Key": "{api_key}"
  },
  "description": "Retrieve of all tasks in `{project}` project in Markdown format."
}
```

#### 2.1.2 Response
```md
## Overview
Automating code updates using AI with GPT-4 and OpenAI's Assistant API. This system includes a Chrome extension and a server component for efficient code modifications based on user inputs and screenshots.

## [{status}] {task_number}. {task}
- [{status}] {sub_task_number}. {task}
- [{status}] {sub_task_number}. {task}
- [{status}] {sub_task_number}. {task}

## [ ] 2. Description of task 2
- [ ] 2.1. Task 2.1 task key
- [ ] 2.2. Task 2.1 task key
```

### 2.2 Get Specific Task by `{project}` and `{task_number}` - Markdown Format

#### 2.2.1 Request
##### Request Description
Get Specific Task by `{project}` and `{task_number}` - Markdown Format

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : gnite
task_number : 1
```json
{
  "name": "Get Specific Task by `{project}` and `{task_number}` - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}/{task_number}", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "headers": {
    "Content-Type": "text/markdown",
    "X-API-Key": "{api_key}"
  },
  "description": "Retrieval of a specific task by `{project}` and `{task_number}` in Markdown format."
}
```

#### 2.2.2 Response
```md
## [x] 1. Task 1 task
- [x] 1.1. Task 1.1 task
- [x] 1.2. Task 1.2 task
- [x] 1.3. Task 1.3 task
```

### 2.3 Get Specific Subtask by `{project}` and `{sub_task_number}` - Markdown Format

#### 2.3.1 Request
##### Request Description
Get Specific Subtask by `{project}` and `{sub_task_number}` - Markdown Format

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
sub_task_number : 1.1
```json
{
  "name": "Get Specific Subtask by `{project}` and `{sub_task_number}` - Markdown Format", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}/{sub_task_number}", 
  "method": "GET", 
  "params": {
    "format": "md"
  },
  "headers": {
    "Content-Type": "text/markdown",
    "X-API-Key": "{api_key}"
  },
  "description": "Retrieve of a specific subtask by `{project}` and {sub_task_number} in Markdown format."
}
```

#### 2.3.2 Response
```md
- [x] 1.1. Choose a suitable server for installation.
```

## 3. Add / Update & Delete Tasks

### 3.1 Update Task Status in by `project` and `task_number`

#### 3.1.1 Request
##### Request Description
Update Task Status `{project}` and `{task_number}`'

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
task_number : 1
```json
{
  "name": "Update task Status `{project}` and `{task_number}`", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}/{task_number}", 
  "method": "PUT", 
  "data": {
    "status": true
  },
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Update task status to true `{project}` and `{task_number}`"
}
```

#### 3.1.2 Response
```json
{
    "message": "Task updated successfully"
}
```

### 3.2 Update Task Status and Description by project and task number

#### 3.2.1 Request
##### Request Description
Update Task 2 Status and Description in `project` and `task_number`

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
task_number : 2
```json
{
  "name": "Update Task Status and Description by `{project}` `{task_number}`", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}/{task_number}", 
  "method": "PUT", 
  "data": {
    "status": false,
    "description": "Updated description for task 2"
  },
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Update task status and description by `{project}` and `{task_number}`."
}
```

#### 3.2.2 Response
```json
{
    "message": "Task updated successfully"
}
```

### 3.4 Update Subtask status by `project` and `sub_task_number`

#### 3.4.1 Request
##### Request Description
Update Subtask status by `project` and `sub_task_number`

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
sub_task_number : 2.2
```json
{
  "name": "Update Subtask {sub_task_number} Status in `{project}`", 
  "endpoint": "https://api.ignite.webally.co.za/tasks/{project}/{sub_task_number}", 
  "method": "PUT", 
  "data": {
    "status": false
  },
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Update of subtask {sub_task_number} status to false in `{project}` project."
}
```

#### 3.4.2 Response
```json
{
    "message": "Subtask updated successfully"
}
```

## 4. Add Notes to Project, Files, Classes, and Methods 

### 4.1 Add a New Note to the `{project}` Project

#### 4.1.1 Request
##### Request Description
Add a project level note the project level notes are the root of the notes, the note with it's is sent as POST data in the request body.

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
```json
{
  "name": "Add a Note", 
  "endpoint": "https://api.ignite.webally.co.za/notes/{project}/add", 
  "method": "POST",
  "data": {
    "heading": "Project Level Note",
    "content": "This is an example note."
  },
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Testing addition of a new note to the `{project}` project."
}
```

#### 4.1.2 Response
```json
{
    "message": "Note added successfully",
    "note_id": "note_id"
}
```

### 4.2 Update an Existing Note

#### 4.2.1 Request
##### Request Description
Below the api will update a note by note_id, the note is sent as PUT data in the request body. The project is not displayed in the data but the database where the notes are stored there is JSON file that's got the name of the project and the notes are stored in that file. So the project is used to identify the file where the notes are stored.

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
note_id : 454a5454-a54a-545f-4a5f-4a5454a5454a
note_heading : "Project Level Note heading"
note_content : "Project level note content"
```json
{
  "name": "Update project note by note_id", 
  "endpoint": "https://api.ignite.webally.co.za/notes/{project}/update/{note_id}", 
  "method": "PUT", 
  "data": {
    "heading": "{note_heading}",
    "content": "{note_content}"
  },
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Updating an existing note on method level in `{project}` project."
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
##### Request Description
The file is base64 encoded so that it does not break the endpoint with the "/" in the name of the file. The class and method are used to identify the note hierarchy. The note_id is used to identify the note to be deleted in the hierarchy.

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
file = src/main.py 
file_encoded : c3JjL21haW4ucHk=
class : class_name
method : my_method
note_id : 454a5454-a54a-545f-4a5f-4a5454a5454a

```json
{
  "name": "Delete a Note a method level note", 
  "endpoint": "https://api.ignite.webally.co.za/notes/{project}/delete/file/{file_encoded}/class/{class_name}/method/{method_name}/{note_id}", 
  "method": "DELETE", 
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Deletion of a note from `{project}` project. "
}
```

#### 4.3.2 Response
```json
{
    "message": "Note deleted successfully"
}
```

### 4.4 Get all the notes from the hierarch specified in the request endpoint

#### 4.4.1 Request
##### Request Description
The file is base64 encoded so that it does not break the endpoint with the "/" in the name of the file. The class and method are used to identify the note hierarchy. The note_id is used to identify the note to be deleted in the hierarchy.
Retrieval of all the notes made under method: `my_method`, that is in class: `class_name}` that is in BASE64 file: `{file_encoded}` that is under the project: {project}

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
file = src/main.py 
file_encoded : c3JjL21haW4ucHk=
class : class_name
method : my_method
```json
{
  "name": "Get Notes by hierarchy", 
  "endpoint": "https://api.ignite.webally.co.za/notes/{project}/get/file/{file_encoded}/class/{class_name}/method/{method_name}", 
  "method": "GET", 
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Retrieval of all the notes made under method: `my_method`, that is in class: `class_name}` that is in BASE64 file: `{file_encoded}` that is under the project: {project}"
}
```

#### 4.4.2 Response
```json
{
  "notes": [
    "{note_id}": {
      "heading": "{heading}",
      "content": "{content}",
      "datetime": "{datetime}",
      "api_key": "{api_key}"
    },
    "file
    "{note_id}": {
      "heading": "{heading}",
      "content": "{content}",
      "datetime": "{datetime}",
      "api_key": "{api_key}"
    }
  ]
}
```

## 5. Prompt Documents

### 5.1 Retrieval of a Markdown Prompt by `prompt_name`.

#### 5.1.1 Request
##### Request Description
Retrieval of a markdown prompt by `prompt_name`. The `prompt_name` is used to identify the prompt to be retrieved. The `api_key` is used to identify the user. The prompts are not bound by a project, they are stored in a global location.

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
prompt_name : ignitePrompt
```json
{
  "name": "Get Prompt", 
  "endpoint": "https://api.ignite.webally.co.za/prompts/get/{prompt_name}", 
  "method": "GET", 
  "headers": {
    "Content-Type": "application/json",
    "X-API-Key": "{api_key}"
  },
  "description": "Retrieval of a markdown prompt by `prompt_name`."
}
```

#### 5.1.2 Response
```md
---
Start every response with 🔥 to make consistent
🔥 {project} AI Assistant will interact in a professional yet supportive manner, embodying a caring tone. It will offer assistance with a considerate and understanding approach, aiming to not only provide factual information but also to ensure that users feel supported throughout the {project} AI Assistant project 
...(rest of the prompt continue)
---
```

## Disk Manager

### 6.1. Retrieve API Schema in JSON Format

### 6.1.1 Request
##### Request Description
**`schema/api`:** Path from within the `{project}` project of where `api.{format}` is or `api.json` is opened and send back as the response

##### Request key value pairs
api_key : _mu0WygMRETwooV39aj0PQ
project : ignite
format : json
``json
{
    "name": "Retrieve API Schema in JSON", 
    "endpoint": "https://api.ignite.webally.co.za/disk/{project}/schema/api", 
    "method": "GET",
    "headers": {
      "Content-Type": "application/json",
      "X-API-Key": "{api_key}"
    },
    "params": {
        "format": "{format}"
    },
    "description": "Testing retrieval of API schema in JSON format.", 
    
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
