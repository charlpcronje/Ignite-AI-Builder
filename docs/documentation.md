# API Documentation

## Task Management Endpoints

1. **Retrieve Tasks**
   - Endpoint: `GET /tasks/<project_name>`
   - Description: Retrieves tasks from a specified JSON file.
   - Parameters: 
     - `project_name`: The name of the JSON file containing tasks.
   - Headers:
     - `X-API-Key`: Required API key for authentication.

2. **Retrieve Specific Task/Subtask**
   - Endpoint: `GET /tasks/<project_name>/<task_number>/<subtask_number>`
   - Description: Retrieves a specific task or subtask.
   - Parameters:
     - `project_name`: The name of the JSON file.
     - `task_number`: The specific task number to retrieve.
     - `subtask_number`: (Optional) The specific subtask number.

## Notes Management Endpoints

1. **Add Note**
   - Endpoint: `POST /notes/<project_name>/add`
   - Description: Adds a new note to the specified notes file.
   - Parameters:
     - `project_name`: The project name of the notes file.
   - Body: 
     ```
     {
       "content": "Note content",
       "level": "project"
     }
     ```
   - Headers:
     - `X-API-Key`: Required API key for authentication.

2. **Update Note**
   - Endpoint: `PUT /notes/<project_name>/update`
   - Description: Updates an existing note in the specified notes file.
   - Body: 
     ```
     {
       "note_id": "1",
       "content": "Updated note content",
       "level": "project"
     }
     ```
   - Headers:
     - `X-API-Key`: Required API key for authentication.

3. **Delete Note**
   - Endpoint: `DELETE /notes/<project_name>/delete`
   - Description: Deletes a note from the specified notes file.
   - Body: 
     ```
     {
       "note_id": "1",
       "level": "project"
     }
     ```
   - Headers:
     - `X-API-Key`: Required API key for authentication.

4. **Retrieve Notes**
   - Endpoint: `GET /notes/<project_name>`
   - Description: Retrieves notes, with optional Markdown formatting.
   - Parameters:
     - `project_name`: The project name of the notes file.
     - `format`: (Optional) Set to 'md' for Markdown format.
   - Headers:
     - `X-API-Key`: Required API key for authentication.

## Prompt Retrieval Endpoint

- **Retrieve Prompt**
  - Endpoint: `GET /prompts/<project_name>`
  - Description: Retrieves the markdown content of a prompt file based on the project name.
  - Parameters:
    - `project_name`: The project name corresponding to the markdown file.
  - Headers:
    - `X-API-Key`: Required API key for authentication.
