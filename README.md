# Ignite AI Builder

## Overview
This Flask-based web application is a multi-faceted system designed to handle tasks, notes, prompts, disk operations through a RESTful API. It employs various modules for handling different aspects like file operations, markdown conversion, API authentication, and more. Each module is tailored to a specific functionality, ensuring modularity and maintainability

- [Ignite AI Builder](#ignite-ai-builder)
  - [Overview](#overview)
  - [Autonomous software creation](#autonomous-software-creation)
    - [Taking Notes](#taking-notes)
    - [Retrieving Files](#retrieving-files)
    - [Managing Tasks](#managing-tasks)
    - [Autonomous Software Management](#autonomous-software-management)
    - [Considerations for AI Integration](#considerations-for-ai-integration)
  - [General Overview and Usage Instructions](#general-overview-and-usage-instructions)
  - [Usage Instructions](#usage-instructions)
  - [Roadmap](#roadmap)
  - [Detailed Documentation for File Handler](#detailed-documentation-for-file-handler)
    - [Module Overview: `file_handler.py`](#module-overview-file_handlerpy)
    - [Class: FileHandler](#class-filehandler)
      - [Methods:](#methods)
    - [Error Handling:](#error-handling)
    - [Concurrency Control:](#concurrency-control)
    - [Assumptions and Limitations:](#assumptions-and-limitations)
  - [Detailed Documentation for Markdown Converter](#detailed-documentation-for-markdown-converter)
    - [Module Overview: `markdown_converter.py`](#module-overview-markdown_converterpy)
    - [Class: MarkdownConverter](#class-markdownconverter)
      - [Methods:](#methods-1)
  - [Error Handling:](#error-handling-1)
  - [Assumptions and Limitations:](#assumptions-and-limitations-1)
  - [Detailed Documentation forAPI Authenticator](#detailed-documentation-forapi-authenticator)
  - [Module Overview: `api_authenticator.py`](#module-overview-api_authenticatorpy)
    - [Class: APIAuthenticator](#class-apiauthenticator)
      - [Methods:](#methods-2)
    - [Error Handling:](#error-handling-2)
    - [Assumptions an  d Limitations:](#assumptions-an--d-limitations)
  - [Detailed Documentation for Task Routes](#detailed-documentation-for-task-routes)
    - [Module Overview: `task_routes.py`](#module-overview-task_routespy)
    - [Flask Blueprint: task\_routes](#flask-blueprint-task_routes)
      - [Functions:](#functions)
    - [Error Handling:](#error-handling-3)
    - [Security and Access Control:](#security-and-access-control)
    - [Assumptions and Limitations:](#assumptions-and-limitations-2)
  - [Detailed Documentation for Notes Routes](#detailed-documentation-for-notes-routes)
    - [Module Overview: `notes_routes.py`](#module-overview-notes_routespy)
    - [Flask Blueprint: notes\_routes](#flask-blueprint-notes_routes)
      - [Functions:](#functions-1)
    - [Error Handling](#error-handling-4)
    - [Security and Access Control](#security-and-access-control-1)
    - [Assumptions and Limitations](#assumptions-and-limitations-3)
  - [Detailed Documentation for Prompt Routes](#detailed-documentation-for-prompt-routes)
    - [Module Overview: `prompt_routes.py`](#module-overview-prompt_routespy)
    - [Flask Blueprint: prompt\_routes](#flask-blueprint-prompt_routes)
      - [Function: get\_prompt(project\_name)](#function-get_promptproject_name)
    - [Module's Role in the Application](#modules-role-in-the-application)
    - [Assumptions and Limitations](#assumptions-and-limitations-4)
  - [Detailed Documentation for Notes Manager](#detailed-documentation-for-notes-manager)
    - [Module Overview: `notes_manager.py`](#module-overview-notes_managerpy)
    - [Class: NotesManager](#class-notesmanager)
      - [Methods:](#methods-3)
    - [Error Handling:](#error-handling-5)
    - [Assumptions and Limitations](#assumptions-and-limitations-5)
  - [Detailed Documentation for App](#detailed-documentation-for-app)
    - [Module Overview: `app.py`](#module-overview-apppy)
    - [Flask Application Setup and Configuration](#flask-application-setup-and-configuration)
      - [Key Components:](#key-components)
  - [Detailed Documentation for Type Hierarchy Validator](#detailed-documentation-for-type-hierarchy-validator)
    - [Module Overview: `type_hierarchy_validator.py`](#module-overview-type_hierarchy_validatorpy)
    - [Class: TypeHierarchyValidator](#class-typehierarchyvalidator)
      - [Methods:](#methods-4)
    - [Error Handling](#error-handling-6)
    - [Functionality and Usage](#functionality-and-usage)
    - [Assumptions and Limitations](#assumptions-and-limitations-6)
  - [Detailed Documentation for Prompt Manager](#detailed-documentation-for-prompt-manager)
    - [Module Overview](#module-overview)
    - [Class: PromptManager](#class-promptmanager)
      - [Methods:](#methods-5)
    - [Error Handling](#error-handling-7)
    - [Functionality and Usag](#functionality-and-usag)
    - [Assumptions and Limitations](#assumptions-and-limitations-7)
  - [Detailed Documentation for Task Manager](#detailed-documentation-for-task-manager)
    - [Module Overview: `task_manager.py`](#module-overview-task_managerpy)
    - [Class: TaskManager](#class-taskmanager)
      - [Methods:](#methods-6)
    - [Error Handling](#error-handling-8)
    - [Functionality and Usage](#functionality-and-usage-1)
    - [Assumptions and Limitations](#assumptions-and-limitations-8)
  - [Detailed Documentation for Task Manager](#detailed-documentation-for-task-manager-1)
  - [Module Overview: `task_manager.py`](#module-overview-task_managerpy-1)
    - [Class: TaskManager](#class-taskmanager-1)
      - [Methods:](#methods-7)
    - [Error Handling](#error-handling-9)
    - [Functionality and Usage](#functionality-and-usage-2)
    - [Assumptions and Limitations](#assumptions-and-limitations-9)
  - [Detailed Documentation for Disk Routes](#detailed-documentation-for-disk-routes)
  - [Module Overview: `disk_routes.py`](#module-overview-disk_routespy)
    - [Flask Blueprint: disk\_routes](#flask-blueprint-disk_routes)
      - [Function: get\_file(project\_name, file\_path)](#function-get_fileproject_name-file_path)
  - [Module's Role in the Application](#modules-role-in-the-application-1)
  - [Assumptions and Limitations](#assumptions-and-limitations-10)
  - [Detailed Documentation for Disk Manager](#detailed-documentation-for-disk-manager)
    - [Module Overview:`disk_manager.py`](#module-overviewdisk_managerpy)
    - [Class: DiskManager](#class-diskmanager)
      - [Methods:](#methods-8)
    - [Error Handling](#error-handling-10)
    - [Functionality and Usage](#functionality-and-usage-3)
    - [Assumptions and Limitations](#assumptions-and-limitations-11)
  - [Project Summary and Interactions](#project-summary-and-interactions)
    - [Overview](#overview-1)
    - [Key Modules and Their Roles](#key-modules-and-their-roles)
    - [Interactions and Data Flow](#interactions-and-data-flow)
    - [Application Configuration and Execution](#application-configuration-and-execution)
  - [Documentation for `Test Runner`, `Test Logger` and `Test Cases`](#documentation-for-test-runner-test-logger-and-test-cases)
    - [Overview](#overview-2)
      - [Test Runner](#test-runner)
      - [Test Logger](#test-logger)
      - [Test Cases](#test-cases)
    - [Application and Testing Workflow](#application-and-testing-workflow)
    - [Key Considerations](#key-considerations)
  - [Tests and Validation](#tests-and-validation)
  - [1. Tasks in JSON Format](#1-tasks-in-json-format)
    - [1.1. Get tasks](#11-get-tasks)
      - [1.1.1 Request](#111-request)
        - [Request Description](#request-description)
        - [Request key value pairs](#request-key-value-pairs)
      - [1.1.2 Response](#112-response)
    - [1.2. Get Specific Task by `{project}` and `{task_number}` - JSON Format](#12-get-specific-task-by-project-and-task_number---json-format)
      - [1.2.1 Request](#121-request)
        - [Request Description](#request-description-1)
        - [Request key value pairs](#request-key-value-pairs-1)
      - [1.2.2 Response](#122-response)
    - [1.3 Get Specific Subtask by `{project}` and `{sub_task_number}` - JSON Format](#13-get-specific-subtask-by-project-and-sub_task_number---json-format)
      - [1.3.1 Request](#131-request)
        - [Request Description](#request-description-2)
        - [Request key value pairs](#request-key-value-pairs-2)
      - [1.3.2 Response](#132-response)
  - [2. Tasks in Markdown Format](#2-tasks-in-markdown-format)
    - [2.1 Get All Tasks in `{project}` - Markdown Format](#21-get-all-tasks-in-project---markdown-format)
      - [2.1.1 Request](#211-request)
        - [Request Description](#request-description-3)
        - [Request key value pairs](#request-key-value-pairs-3)
      - [2.1.2 Response](#212-response)
    - [2.2 Get Specific Task by `{project}` and `{task_number}` - Markdown Format](#22-get-specific-task-by-project-and-task_number---markdown-format)
      - [2.2.1 Request](#221-request)
        - [Request Description](#request-description-4)
        - [Request key value pairs](#request-key-value-pairs-4)
      - [2.2.2 Response](#222-response)
    - [2.3 Get Specific Subtask by `{project}` and `{sub_task_number}` - Markdown Format](#23-get-specific-subtask-by-project-and-sub_task_number---markdown-format)
      - [2.3.1 Request](#231-request)
        - [Request Description](#request-description-5)
        - [Request key value pairs](#request-key-value-pairs-5)
      - [2.3.2 Response](#232-response)
  - [3. Add / Update \& Delete Tasks](#3-add--update--delete-tasks)
    - [3.1 Update Task Status in by `project` and `task_number`](#31-update-task-status-in-by-project-and-task_number)
      - [3.1.1 Request](#311-request)
        - [Request Description](#request-description-6)
        - [Request key value pairs](#request-key-value-pairs-6)
      - [3.1.2 Response](#312-response)
    - [3.2 Update Task Status and Description by project and task number](#32-update-task-status-and-description-by-project-and-task-number)
      - [3.2.1 Request](#321-request)
        - [Request Description](#request-description-7)
        - [Request key value pairs](#request-key-value-pairs-7)
      - [3.2.2 Response](#322-response)
    - [3.4 Update Subtask status by `project` and `sub_task_number`](#34-update-subtask-status-by-project-and-sub_task_number)
      - [3.4.1 Request](#341-request)
        - [Request Description](#request-description-8)
        - [Request key value pairs](#request-key-value-pairs-8)
      - [3.4.2 Response](#342-response)
  - [4. Add Notes to Project, Files, Classes, and Methods](#4-add-notes-to-project-files-classes-and-methods)
    - [4.1 Add a New Note to the `{project}` Project](#41-add-a-new-note-to-the-project-project)
      - [4.1.1 Request](#411-request)
        - [Request Description](#request-description-9)
        - [Request key value pairs](#request-key-value-pairs-9)
      - [4.1.2 Response](#412-response)
    - [4.2 Update an Existing Note](#42-update-an-existing-note)
      - [4.2.1 Request](#421-request)
        - [Request Description](#request-description-10)
        - [Request key value pairs](#request-key-value-pairs-10)
      - [4.2.2 Response](#422-response)
    - [4.3 Delete a Note](#43-delete-a-note)
      - [4.3.1 Request](#431-request)
        - [Request Description](#request-description-11)
        - [Request key value pairs](#request-key-value-pairs-11)
      - [4.3.2 Response](#432-response)
    - [4.4 Get all the notes from the hierarch specified in the request endpoint](#44-get-all-the-notes-from-the-hierarch-specified-in-the-request-endpoint)
      - [4.4.1 Request](#441-request)
        - [Request Description](#request-description-12)
        - [Request key value pairs](#request-key-value-pairs-12)
      - [4.4.2 Response](#442-response)
  - [5. Prompt Documents](#5-prompt-documents)
    - [5.1 Retrieval of a Markdown Prompt by `prompt_name`.](#51-retrieval-of-a-markdown-prompt-by-prompt_name)
      - [5.1.1 Request](#511-request)
        - [Request Description](#request-description-13)
        - [Request key value pairs](#request-key-value-pairs-13)
      - [5.1.2 Response](#512-response)
  - [Disk Manager](#disk-manager)
    - [6.1. Retrieve API Schema in JSON Format](#61-retrieve-api-schema-in-json-format)
    - [6.1.1 Request](#611-request)
        - [Request Description](#request-description-14)
        - [Request key value pairs](#request-key-value-pairs-14)
  - [OpenAI Schema](#openai-schema)

## Autonomous software creation

The integration of this API into an AI system for autonomous software creation, updating, and management offers a fascinating use case. Here's an overview of how an AI agent might leverage this API for various operations:

### Taking Notes

- **Functionality**: The AI could use the endpoints defined in `notes_routes.py` for note management. This would allow the AI to keep track of changes, ideas, bugs, or any relevant information during software development.
- **Process**: The AI can add notes using the POST endpoint, update them through PUT, and delete them with DELETE. It also can retrieve notes, either all or based on specific identifiers, using GET requests.
- **Use Case**: For instance, during the development process, the AI might encounter a bug or a new feature request. It could then log this information as a note for future reference or action.

### Retrieving Files

- **Functionality**: The endpoints in `disk_routes.py` enable file management. This allows the AI to access different types of files (e.g., API schemas, documentation) stored on the server.
- **Process**: Through GET requests, the AI can retrieve files in various formats like JSON, Markdown, or YAML. The AI can also update these files using PUT requests.
- **Use Case**: The AI might need to access API documentation stored in Markdown format or retrieve a JSON schema of another service it interacts with.

### Managing Tasks

- **Functionality**: Using `task_routes.py`, the AI can manage tasks related to software development, such as feature implementations, bug fixes, or testing.
- **Process**: It can create new tasks, update the status of existing tasks, or mark tasks as completed/deleted. This is done through GET, POST, PUT, and DELETE requests.
- **Use Case**: The AI could automatically create tasks for new features or bugs it identifies. It could also update the status of tasks as it progresses in its development work.

### Autonomous Software Management

- **Autonomy**: By integrating these functionalities, the AI agent becomes capable of autonomously managing various aspects of software development. It can keep track of tasks, store and retrieve necessary information, and log activities or issues.
- **Decision Making**: The AI can make informed decisions based on the data it retrieves from the API. For instance, it might prioritize tasks based on urgency or dependencies.
- **Learning and Adaptation**: Over time, the AI can learn from past activities, optimizing its decision-making process for efficiency and effectiveness.

### Considerations for AI Integration

- **API Limitations**: The AI's capabilities will be bounded by what the API can handle. It's crucial to ensure the API supports all necessary operations the AI might need.
- **Security**: Given the autonomous nature of the AI, robust security measures must be in place to prevent unauthorized access and ensure data integrity.
- **Error Handling**: The AI should be capable of handling errors returned by the API gracefully and should have fallback or retry mechanisms.

---

## General Overview and Usage Instructions

1. **file_handler.py**: Manages file operations, specifically for JSON files. Includes methods for reading and writing JSON files with file locking mechanisms to handle concurrent access.
2. **markdown_converter.py**: Converts JSON data to Markdown format. Useful for presenting structured data in a readable format.
3. **api_authenticator.py**: Handles API authentication, ensuring secure access to the application's endpoints.
4. **task_routes.py**: Flask routes for managing tasks. It includes functionalities like retrieving, updating, and marking tasks as deleted.
5. **notes_routes.py**: Flask routes for managing notes. This includes adding, updating, deleting, and retrieving notes.
6. **prompt_routes.py**: Flask routes for managing markdown prompt documents.
7. **notes_manager.py**: Manages the operations related to notes stored in a JSON file.
8. **app.py**: The main Flask application file. It integrates all the modules and handles the overall operation of the application.
9. **type_hierarchy_validator.py**: Validates the hierarchy of note types based on a defined JSON structure.
10. **prompt_manager.py**: Manages the retrieval of markdown prompt files.
11. **task_manager.py**: Responsible for extracting specific tasks or subtasks from JSON data.
12. **disk_routes.py**: Defines routes for handling file operations in different formats.
13. **disk_manager.py**: Provides functionality for managing disk operations such as reading and writing files.
14. **conversion.py**: Contains functions for converting JSON data to different formats, such as Markdown.

## Usage Instructions
Each module is designed to be standalone yet integrable within the Flask application. To utilize these modules, import them into your Flask app or other Python scripts as needed. The `app.py` file is your entry point, tying all the modules together into a cohesive application.

## Roadmap

📖 To expand the capabilities of the AI agent for autonomous software creation, updating, and management, it's essential to consider additional functionalities that the API might need to support. Here are some key areas to explore:

1. **Advanced Task Scheduling and Dependency Management**
  - **Requirement**: Ability to schedule tasks for future dates and manage dependencies between tasks.
  - **Reasoning**: The AI might need to plan tasks in a sequence, where the completion of one task triggers the start of another.

2. **Integrated Version Control System (VCS) Support**
  - **Requirement**: Direct interaction with VCS (like Git) for tracking changes, committing code, and managing branches.
  - **Reasoning**: Automating version control processes is crucial for software development, allowing the AI to handle code updates and maintain historical records of changes.

3. **Real-time Collaboration and Notification System**
  - **Requirement**: Mechanisms for the AI to collaborate with human team members, including notification systems.
  - **Reasoning**: The AI should be able to notify team members about updates, receive feedback, and possibly integrate inputs from different sources.

4. **Automated Testing and Continuous Integration/Deployment (CI/CD)**
  - **Requirement**: Ability to initiate and manage automated tests, and integrate with CI/CD pipelines.
  - **Reasoning**: Continuous testing and deployment are vital for agile development, ensuring that changes made by the AI are viable and do not introduce bugs.

5. **Dynamic Resource Allocation and Scaling**
  - **Requirement**: Manage computational resources, scale services based on demand.
  - **Reasoning**: Depending on the task's complexity and urgency, the AI might need to allocate more resources or scale down to optimize usage.

6. **Enhanced Security Protocols**
  - **Requirement**: Robust authentication and authorization mechanisms, especially if the AI handles sensitive data or critical operations.
  - **Reasoning**: As the AI has a high level of access, security is paramount to protect the system from internal errors and external threats.

7. **Data Analytics and Reporting**
  - **Requirement**: Tools for analyzing performance metrics, generating reports, and extracting insights.
  - **Reasoning**: To improve over time, the AI needs to understand its performance and the impact of its actions.

8. **Customizable Workflow and Process Automation**
  - **Requirement**: Ability to define and automate specific workflows or processes.
  - **Reasoning**: Different projects might require unique workflows, and the AI should adapt its operations accordingly.

9. **Feedback and Learning Loop Integration**
  - **Requirement**: Mechanisms to receive feedback, learn from it, and adapt strategies.
  - **Reasoning**: For continuous improvement, the AI should evolve its approach based on success rates and feedback.

## Detailed Documentation for File Handler

### Module Overview: `file_handler.py`
`file_handler.py` is a Python module in this Flask application responsible for handling file operations, specifically focusing on JSON files. It provides functionality to read from and write to JSON files, with an emphasis on handling concurrent file access through file locking mechanisms.

### Class: FileHandler
This class encapsulates the methods for interacting with JSON files.

#### Methods:
1. **__init__(self)**:
   - Initializes the FileHandler instance.
   - Configures the basic logging level to INFO.

2. **read_json_file(self, file_path)**:
   - Reads a JSON file from the given file path.
   - Implements a file locking mechanism to prevent concurrent modifications.
   - **Parameters**:
     - `file_path` (str): Path to the JSON file.
   - **Returns**:
     - A dictionary representing the JSON file's content, or None if an error occurs.
   - **Usage**:
     ```python
     file_handler = FileHandler()
     data = file_handler.read_json_file("path/to/file.json")
     ```

3. **write_json_file(self, file_path, data)**:
   - Writes data to a JSON file at the specified file path.
   - Ensures exclusive access to the file during the operation to avoid conflicts.
   - **Parameters**:
     - `file_path` (str): Path to the JSON file.
     - `data` (dict): The data to write to the file.
   - **Returns**:
     - None. Raises an exception if writing fails.
   - **Usage**:
     ```python
     file_handler = FileHandler()
     file_handler.write_json_file("path/to/file.json", {"key": "value"})
     ```

### Error Handling:
Both methods handle various exceptions, including FileNotFoundError and JSONDecodeError. These are logged using the standard logging module.

### Concurrency Control:
The module uses `fcntl` for file locking, which is a Unix-specific library. Therefore, this module is not compatible with Windows.

### Assumptions and Limitations:
- The module assumes the files being read and written are valid JSON.
- File locking is implemented using `fcntl`, which may not be suitable for all environments (e.g., non-Unix systems).
- Error handling is primarily logging-based, without custom exception handling.

## Detailed Documentation for Markdown Converter

### Module Overview: `markdown_converter.py` 
`markdown_converter.py` is a Python module designed to convert JSON data into Markdown format. This module is particularly useful for presenting structured JSON data in a more human-readable form, enhancing the user's interaction with the data.

### Class: MarkdownConverter
This class provides the core functionality for converting JSON to Markdown.

#### Methods:
1. **__init__(self)**:
   - Initializes the MarkdownConverter instance.
   - Sets up basic logging configuration.
   - **Usage**:
     ```python
     markdown_converter = MarkdownConverter()
     ```

2. **convert_to_markdown(self, data)**:
   - Converts the provided JSON data to a Markdown formatted string.
   - **Parameters**:
     - `data` (dict): JSON data to be converted to Markdown.
   - **Returns**:
     - A string in Markdown format representing the given JSON data.
   - **Usage**:
     ```python
     markdown_converter = MarkdownConverter()
     json_data = {"overview": "Example data", "tasks": {...}}
     markdown_text = markdown_converter.convert_to_markdown(json_data)
     ```
   - **Details**:
     - The method processes different structures within the JSON, such as tasks and subtasks, and formats them appropriately in Markdown.
     - In case of unexpected data formats, an error message is included in the Markdown output.

## Error Handling:
The method includes try-except blocks to catch and log exceptions, ensuring that any conversion errors are appropriately handled.

## Assumptions and Limitations:
- The input data is expected to be a dictionary with a specific structure. Unrecognized formats may not convert correctly.
- The method currently handles a predefined structure (e.g., tasks and subtasks). Modifications are required to support different JSON structures.

## Detailed Documentation forAPI Authenticator

## Module Overview: `api_authenticator.py`
`api_authenticator.py` is a crucial module in the Flask application, responsible for handling API authentication. This module ensures that access to various API endpoints is secure and restricted to authorized users only.

### Class: APIAuthenticator
This class is designed to manage the authentication process, primarily using API keys.

#### Methods:
1. **__init__(self)**:
   - Initializes the APIAuthenticator instance.
   - Prepares for dynamic loading of API keys per request.
   - **Usage**:
     ```python
     api_authenticator = APIAuthenticator()
     ```

2. **load_api_keys(self, api_keys_file)**:
   - Loads API keys from a specified JSON file.
   - **Parameters**:
     - `api_keys_file` (str): Path to the JSON file containing API keys.
   - **Usage**:
     ```python
     api_authenticator.load_api_keys("path/to/api_keys.json")
     ```

3. **require_api_key(self, view_function)**:
   - A decorator function to secure Flask routes with API key authentication.
   - **Parameters**:
     - `view_function` (function): The Flask view function to decorate.
   - **Returns**:
     - The decorated view function with API key authentication.
   - **Usage**:
     ```python
     @api_authenticator.require_api_key
     def protected_route():
         # route implementation
     ```

###3Security and Authentication:
- The API keys are dynamically loaded for each request, ensuring that changes to API keys do not require application restarts.
- The `require_api_key` decorator is used to protect Flask routes. It checks for the presence of a valid API key in the request headers.

### Error Handling:
Errors such as missing or invalid API keys result in appropriate HTTP responses with error messages, preventing unauthorized access.

### Assumptions an  d Limitations: 
- API keys are stored in a JSON file, which might need to be secured and backed up appropriately.
- The current implementation supports only one type of authentication (API key). Additional methods like OAuth or JWT might be necessary for more complex applications.

## Detailed Documentation for Task Routes

### Module Overview: `task_routes.py`
`task_routes.py` defines the Flask routes related to task management within the application. This module interfaces with `FileHandler`, `TaskManager`, and `MarkdownConverter` to perform operations like retrieving, updating, and 'deleting' tasks. Each route is secured through API key authentication and includes detailed logging.

### Flask Blueprint: task_routes
A Blueprint named `task_routes` is created to organize and group the task-related routes.

#### Functions:
1. **get_task(project_name, task_number=None)**:
   - Flask route for retrieving task data.
   - **Parameters**:
     - `project_name` (str): Identifies the JSON file containing tasks.
     - `task_number` (str, optional): Specifies a particular task or subtask.
   - **Returns**:
     - Task data in JSON or Markdown format, or an error message.
   - **Usage**:
     ```python
     # Accessed via HTTP GET to /<project_name>/<task_number>
     ```

2. **update_task(project_name, task_number)**:
   - Flask route for updating specific task details.
   - **Parameters**:
     - `project_name` (str): Identifies the JSON file containing tasks.
     - `task_number` (str): Specifies the task to update.
   - **Returns**:
     - Confirmation of the update or an error message.
   - **Usage**:
     ```python
     # Accessed via HTTP PUT to /<project_name>/<task_number>
     ```

### Error Handling:
Each function includes error handling to respond with appropriate HTTP status codes and error messages in case of issues like file not found, task not found, or internal server errors.

### Security and Access Control:
The routes can be secured with API key authentication, though the decorator is commented out in the provided code. Uncommenting the `@api_auth_instance.require_api_key` will enforce API key checks.

### Assumptions and Limitations:
- The module assumes that task data is stored in a JSON format and is structured in a specific way.
- Error handling primarily focuses on common scenarios like file not found or task not found. More complex error scenarios may require additional handling.

## Detailed Documentation for Notes Routes

### Module Overview: `notes_routes.py`
`notes_routes.py` contains Flask routes for managing notes within the application. This module leverages `NotesManager` and `TypeHierarchyValidator` to perform operations like adding, updating, deleting, and retrieving notes, all of which are secured via API key authentication.

### Flask Blueprint: notes_routes
This Blueprint groups and organizes note-related routes, facilitating clear and modular route management.

#### Functions:
1. **add_note_route(project_name)**:
   - A POST route for adding a new note to a project.
   - **Parameters**:
     - `project_name` (str): The name of the project to add the note to.
   - **Returns**:
     - A JSON response indicating the success or failure of the note addition.
   - **Usage**:
     ```python
     # Accessed via HTTP POST to /<project_name>/add
     ```

2. **update_note(project_name, note_id)**:
   - A PUT route for updating an existing note.
   - **Parameters**:
     - `project_name` (str): The name of the project.
     - `note_id` (str): The unique ID of the note to update.
   - **Returns**:
     - A JSON response indicating the success or failure of the update.
   - **Usage**:
     ```python
     # Accessed via HTTP PUT to /<project_name>/update/<note_id>
     ```

3. **delete_note(project_name, note_id)**:
   - A DELETE route for removing a specific note.
   - **Parameters**:
     - `project_name` (str): The name of the project.
     - `note_id` (str): The unique ID of the note to delete.
   - **Returns**:
     - A JSON response indicating the success or failure of the deletion.
   - **Usage**:
     ```python
     # Accessed via HTTP DELETE to /<project_name>/delete/<note_id>
     ```

4. **get_notes_by_identifier(project_name, identifier)**:
   - A GET route for retrieving notes based on a hierarchical identifier.
   - **Parameters**:
     - `project_name` (str): The name of the project.
     - `identifier` (str): The hierarchical identifier of the notes.
   - **Returns**:
     - A JSON response containing the notes or an error message.
   - **Usage**:
     ```python
     # Accessed via HTTP GET to /<project_name>/<identifier>
     ```
### Error Handling
Each route includes error handling to appropriately respond to different scenarios, such as invalid input, inability to find notes, and server errors.

### Security and Access Control
Routes are protected with the `@api_auth.require_api_key` decorator, ensuring that only authenticated requests can access these endpoints.

### Assumptions and Limitations
- The module assumes that notes are structured in a specific format within the JSON file.
- Notes are identified and accessed based on a hierarchical structure, which may not be suitable for all use cases.

## Detailed Documentation for Prompt Routes

### Module Overview: `prompt_routes.py`
`prompt_routes.py` is a module in the Flask application dedicated to managing markdown prompt documents. It includes Flask routes for retrieving content from markdown files, focusing on secure access and efficient file handling.

### Flask Blueprint: prompt_routes
This Blueprint manages the routes associated with markdown prompts, enhancing the organization and maintainability of the code.

#### Function: get_prompt(project_name)
- **Purpose**: This route is designed to retrieve and return the content of markdown prompt files based on a given project name.
- **Parameters**:
  - `project_name` (str): Represents the project name corresponding to the markdown file.
- **Returns**:
  - The content of the markdown file or an error message.
- **HTTP Method**: `GET`
- **Path**: `/<project_name>/get`
- **Usage Example**:
  ```python
  # Accessed via HTTP GET to /<project_name>/get
  ```
- **Security**: The route is secured with the `@api_auth_instance.require_api_key` decorator, ensuring that access is limited to authenticated users.
- **Error Handling**: Errors in file retrieval are logged, and an appropriate error message is returned to the client.

### Module's Role in the Application
`prompt_routes.py` serves as a crucial component for serving markdown-based documentation or prompts, integral for applications requiring dynamic content retrieval based on project-specific data.

### Assumptions and Limitations
- Assumes markdown files are named after the project names and stored in a specific directory.
- Error handling is primarily focused on file retrieval errors. More complex scenarios may need additional handling.

## Detailed Documentation for Notes Manager

### Module Overview: `notes_manager.py`
`notes_manager.py` is a Python module in the Flask application that manages the operations related to notes stored in a JSON file. It provides functionalities for adding, updating, deleting, and retrieving notes, with each operation considering the note's hierarchical structure.

### Class: NotesManager
This class is responsible for managing notes and interacts with the JSON file that stores the note data.

#### Methods:
1. **__init__(self, notes_file, validator)**:
   - Initializes the NotesManager with the notes file path and a hierarchy validator.
   - **Parameters**:
     - `notes_file` (str): Path to the notes JSON file.
     - `validator` (TypeHierarchyValidator): Validator for note type hierarchy.
   - **Usage**:
     ```python
     validator = TypeHierarchyValidator('type_hierarchy.json')
     notes_manager = NotesManager('notes.json', validator)
     ```

2. **add_note(self, identifier, content, api_key)**:
   - Adds a new note to the notes structure based on the given identifier.
   - **Parameters**:
     - `identifier` (str): Hierarchical path of the note.
     - `content` (str): Content of the note.
     - `api_key` (str): API key associated with the note.
   - **Returns**:
     - Boolean indicating the success of the operation.

3. **update_note(self, note_id, identifier, updates)**:
   - Updates an existing note based on its ID and identifier.
   - **Parameters**:
     - `note_id` (str): Unique ID of the note to update.
     - `identifier` (str): Hierarchical identifier of the note.
     - `updates` (dict): Updated fields.
   - **Returns**:
     - Boolean indicating the success of the operation.

4. **delete_note(self, note_id, identifier)**:
   - Deletes a note based on its ID and identifier.
   - **Parameters**:
     - `note_id` (str): Unique ID of the note to delete.
     - `identifier` (str): Hierarchical identifier of the note.
   - **Returns**:
     - Boolean indicating the success of the operation.

5. **get_note_by_id(self, note_id, identifier)**:
   - Retrieves a note by its ID and identifier.
   - **Parameters**:
     - `note_id` (str): Unique ID of the note.
     - `identifier` (str): Hierarchical identifier of the note.
   - **Returns**:
     - The note if found, None otherwise.

6. **get_notes_by_note_type(self, identifier)**:
   - Retrieves notes based on the note type specified in the identifier.
   - **Parameters**:
     - `identifier` (str): Hierarchical identifier specifying the note type.
   - **Returns**:
     - A dictionary of notes of the specified type.

### Error Handling:
The class includes error handling to manage exceptions during file operations and note management tasks.

### Assumptions and Limitations
- Assumes that the notes are structured in a JSON format.
- Depends on `TypeHierarchyValidator` for validating the note hierarchy.
- Designed for use within the Flask application and might require adaptation for standalone use.

## Detailed Documentation for App

### Module Overview: `app.py`
`app.py` is the main Flask application file for this project. It orchestrates various functionalities by integrating different modules for tasks, notes, and prompts management. It also sets up the application environment, including configurations, error handling, and routing.

### Flask Application Setup and Configuration
This file initializes and configures the Flask application, integrating various components and setting up the necessary middleware.

#### Key Components:
1. **Flask Instance**:
   - Creates an instance of the Flask application.
   - **Usage**:
     ```python
     app = Flask(__name__)
     ```

2. **Environment Variables**:
   - Loads environment variables using `load_dotenv()` from the dotenv package.
   - Configures the application based on these variables.

3. **CORS (Cross-Origin Resource Sharing)**:
   - Initializes CORS settings for the application to handle cross-origin requests.
   - **Usage**:
     ```python
     init_cors(app)
     ```

4. **Error Handlers**:
   - Sets up custom error handlers for different HTTP error codes.
   - **Usage**:
     ```python
     init_error_handlers(app)
     ```

5. **Logging Middleware**:
   - Configures logging for the application, aiding in debugging and monitoring.
   - **Usage**:
     ```python
     configure_logging()
     init_log_middleware(app)
     ```

6. **Blueprint Registration**:
   - Registers various blueprints for tasks, notes, prompts, and disk operations.
   - **Usage**:
     ```python
     app.register_blueprint(task_blueprint, url_prefix='/tasks')
     app.register_blueprint(notes_blueprint, url_prefix='/notes')
     # ... other blueprints
     ```

7. **Application Run**:
   - The entry point to run the Flask application.
   - Configured to use host and port details from environment variables.
   - Debug mode is set based on the `FLASK_ENV` variable.

**Application Structure and Flow**:
`app.py` serves as the central hub for the application. It integrates various modules, each handling specific aspects like API authentication (`api_authenticator`), task management (`task_routes`), etc., creating a cohesive and functional web service.

**Assumptions and Limitations**:
- Assumes that the necessary environment variables are set in a `.env` file or the environment.
- The application's behavior, especially error handling and CORS, can be customized as per requirements.

## Detailed Documentation for Type Hierarchy Validator

### Module Overview: `type_hierarchy_validator.py`
`type_hierarchy_validator.py` is a Python module designed to validate the hierarchy of note types in the application. It is essential for ensuring that the notes adhere to a predefined hierarchical structure, which is crucial for maintaining consistency and order in note management.

### Class: TypeHierarchyValidator
This class handles the validation of note types based on a JSON-defined type hierarchy.

#### Methods:
1. **__init__(self, json_file)**:
   - Initializes the TypeHierarchyValidator by loading a type hierarchy from a JSON file.
   - **Parameters**:
     - `json_file` (str): Path to the JSON file containing the type hierarchy.
   - **Usage**:
     ```python
     validator = TypeHierarchyValidator('path/to/type_hierarchy.json')
     ```

2. **validate_hierarchy(self, identifier)**:
   - Validates if a sequence of note types in the identifier adheres to the type hierarchy.
   - **Parameters**:
     - `identifier` (str): The hierarchical identifier of the note.
   - **Returns**:
     - Boolean indicating whether the hierarchy is valid.
   - **Usage**:
     ```python
     is_valid = validator.validate_hierarchy('project:example/file:sample')
     ```

### Error Handling
The class includes robust error handling for file loading and JSON decoding. It logs appropriate messages for different error scenarios, such as file not found or JSON decoding errors.

### Functionality and Usage
- Primarily used by the `NotesManager` to validate the hierarchical structure of notes.
- Ensures that the note types and their parent-child relationships conform to the predefined structure.

### Assumptions and Limitations
- The hierarchy must be predefined and stored in a JSON file.
- It assumes a specific format for the type hierarchy and the identifiers.
- Currently tailored for notes but can be adapted for other hierarchical data types.

## Detailed Documentation for Prompt Manager

### Module Overview
`prompt_manager.py` is a dedicated module in the Flask application for managing markdown prompt files. It is designed to handle requests for specific markdown documents, ensuring efficient and organized access to these resources.

### Class: PromptManager
This class is responsible for retrieving markdown prompt files from a specified directory.

#### Methods:
1. **__init__(self, prompts_dir)**:
   - Initializes the PromptManager with a directory path where markdown files are stored.
   - **Parameters**:
     - `prompts_dir` (str): Path to the directory containing markdown files.
   - **Usage**:
     ```python
     prompt_manager = PromptManager("path/to/prompts")
     ```

2. **get_prompt(self, filename)**:
   - Retrieves the content of a markdown file based on the provided filename.
   - **Parameters**:
     - `filename` (str): The name of the markdown file to retrieve.
   - **Returns**:
     - The content of the markdown file or an error message.
   - **Usage**:
     ```python
     content, error = prompt_manager.get_prompt("example.md")
     ```
### Error Handling
The class includes error handling to manage exceptions during file reading, such as file not found or access errors. Errors are returned along with the content, allowing the calling function to handle them appropriately.

### Functionality and Usag
- The `PromptManager` class is primarily used in the `prompt_routes.py` module to serve markdown content through Flask routes.
- It simplifies the process of retrieving markdown content, centralizing the file reading logic in one place.

### Assumptions and Limitations
- Assumes that all markdown files are stored in a single directory specified at initialization.
- Designed to handle text-based markdown files; other file formats might require modifications to the retrieval process.

## Detailed Documentation for Task Manager

### Module Overview: `task_manager.py`
`task_manager.py` plays a key role in the Flask application by handling task-related operations. Specifically, it focuses on extracting specific tasks or subtasks from JSON data, ensuring that task data is processed and managed efficiently and accurately.

### Class: TaskManager
This class provides functionalities to interact with and manipulate task data stored in JSON format.

#### Methods:
1. **__init__(self)**:
   - Initializes the TaskManager instance.
   - Sets up basic logging configuration.
   - **Usage**:
     ```python
     task_manager = TaskManager()
     ```

2. **extract_task_data(self, data, task_number)**:
   - Extracts and returns specific task or subtask data from the provided JSON.
   - **Parameters**:
     - `data` (dict): The JSON data containing tasks.
     - `task_number` (str): The task number (including subtasks) to extract.
   - **Returns**:
     - A dictionary with the extracted task or subtask data, or None if not found.
   - **Usage**:
     ```python
     tasks_data = {"tasks": {...}}
     specific_task_data = task_manager.extract_task_data(tasks_data, "1.1")
     ```

### Error Handling
The class includes error handling to manage scenarios where the specified task or subtask is not found in the data. Such cases are logged as errors.

### Functionality and Usage
- Essential for operations that require task-specific data extraction, such as retrieving or updating tasks in the `task_routes.py` module.
- Accommodates both main tasks and subtasks, allowing for flexible task management.

### Assumptions and Limitations 
- Assumes that task data is structured in a specific way, particularly for tasks and subtasks.
- The method is tailored for JSON data formats; other formats might require modification of the extraction logic.


## Detailed Documentation for Task Manager

## Module Overview: `task_manager.py`
`task_manager.py` plays a key role in the Flask application by handling task-related operations. Specifically, it focuses on extracting specific tasks or subtasks from JSON data, ensuring that task data is processed and managed efficiently and accurately.

### Class: TaskManager
This class provides functionalities to interact with and manipulate task data stored in JSON format.

#### Methods:
1. **__init__(self)**:
   - Initializes the TaskManager instance.
   - Sets up basic logging configuration.
   - **Usage**:
     ```python
     task_manager = TaskManager()
     ```

2. **extract_task_data(self, data, task_number)**:
   - Extracts and returns specific task or subtask data from the provided JSON.
   - **Parameters**:
     - `data` (dict): The JSON data containing tasks.
     - `task_number` (str): The task number (including subtasks) to extract.
   - **Returns**:
     - A dictionary with the extracted task or subtask data, or None if not found.
   - **Usage**:
     ```python
     tasks_data = {"tasks": {...}}
     specific_task_data = task_manager.extract_task_data(tasks_data, "1.1")
     ```

### Error Handling
The class includes error handling to manage scenarios where the specified task or subtask is not found in the data. Such cases are logged as errors.

### Functionality and Usage
- Essential for operations that require task-specific data extraction, such as retrieving or updating tasks in the `task_routes.py` module.
- Accommodates both main tasks and subtasks, allowing for flexible task management.

### Assumptions and Limitations
- Assumes that task data is structured in a specific way, particularly for tasks and subtasks.
- The method is tailored for JSON data formats; other formats might require modification of the extraction logic.


## Detailed Documentation for Disk Routes

## Module Overview: `disk_routes.py`
`disk_routes.py` is a Flask module within the application, designed to handle file operations through specific API endpoints. It provides routes for retrieving files stored on the server's disk in various formats, including JSON and Markdown, ensuring a flexible and efficient file handling mechanism.

### Flask Blueprint: disk_routes
This Blueprint manages routes related to file operations, facilitating structured and organized API endpoints for file access.

#### Function: get_file(project_name, file_path)
- **Purpose**: This route is designed to retrieve the content of files based on the specified project name and file path. It supports different file formats, enhancing the application's flexibility in handling file data.
- **Parameters**:
  - `project_name` (str): Specifies the project folder name.
  - `file_path` (str): The relative path of the file within the project folder.
- **Returns**:
  - The file's content in the requested format or an error message.
- **HTTP Method**: `GET`
- **Path**: `/<project_name>/<path:file_path>`
- **Usage Example**:
  ```python
  # Accessed via HTTP GET to /<project_name>/<file_path>
  ```
- **Error Handling**: The route includes error handling to manage scenarios like file not found or format conversion errors. Appropriate HTTP status codes and messages are returned.
- **Supported Formats**: Besides JSON, it can handle formats like Markdown and plain text, as specified by the `format` query parameter.

## Module's Role in the Application
`disk_routes.py` serves as a crucial component for file management, allowing the application to serve or process files stored on the server dynamically.

## Assumptions and Limitations
- Assumes file paths and project names are correctly specified by the client.
- Requires the `DiskManager` module for handling the low-level file operations.
- The ability to handle different file formats depends on the implementation in `DiskManager`.

## Detailed Documentation for Disk Manager

### Module Overview:`disk_manager.py`
`disk_manager.py` is a critical component of the Flask application, tasked with managing disk operations such as reading and writing files in various formats. It serves as the backbone for file operations, supporting functionalities like file format conversion and file system interactions.

### Class: DiskManager
This class encapsulates the logic for file operations, offering a unified interface for reading and writing files on the server's disk.

#### Methods:
1. **__init__(self, base_path='./disk')**:
   - Initializes the DiskManager with a base directory for file operations.
   - **Parameters**:
     - `base_path` (str): The base directory path for file operations.
   - **Usage**:
     ```python
     disk_manager = DiskManager('path/to/base/directory')
     ```

2. **read_file(self, project_name, file_path, format_type)**:
   - Reads a file based on the project name, file path, and format type.
   - **Parameters**:
     - `project_name` (str): The project folder name.
     - `file_path` (str): The relative path of the file within the project folder.
     - `format_type` (str): The format type of the file (e.g., 'json', 'yaml', 'txt').
   - **Returns**:
     - The content of the file in the specified format.
   - **Usage**:
     ```python
     content = disk_manager.read_file('project_name', 'file/path', 'json')
     ```

3. **write_file(self, project_name, file_path, content, format_type)**:
   - Writes content to a file based on the project name, file path, and format type.
   - **Parameters**:
     - `project_name` (str): The project folder name.
     - `file_path` (str): The relative path of the file within the project folder.
     - `content`: The content to write to the file.
     - `format_type` (str): The format type of the file (e.g., 'json', 'yaml').
   - **Usage**:
     ```python
     disk_manager.write_file('project_name', 'file/path', data, 'json')
     ```

### Error Handling
The class includes comprehensive error handling for various scenarios such as file not found, access errors, and format-related issues. Errors are logged, and appropriate exceptions are raised.

### Functionality and Usage
- Centralizes file operations, providing a consistent approach to read and write files in different formats.
- The flexibility of the class allows for easy integration with various parts of the application, particularly with `disk_routes.py`.

### Assumptions and Limitations
- Assumes a structured file system with files organized under project-specific directories.
- The class's functionality is dependent on the availability and accessibility of the file system where the application is hosted.

As we have covered detailed documentation for all the provided Python modules, I will now summarize the overall project and its components, highlighting their interactions and functionalities within the Flask application.

## Project Summary and Interactions

### Overview
This Flask-based web application is a robust system designed for managing tasks, notes, prompts, and file operations. It integrates various modules, each responsible for specific functionalities, to create a cohesive and efficient application.

### Key Modules and Their Roles
1. **File Handler**: Manages file operations for JSON files, implementing read and write functionalities with concurrency control.
2. **markdown_converter**: Converts JSON data to Markdown format, facilitating readable and structured documentation.
3. **API Authenticator**: Ensures API security by managing API key authentication for the application’s routes.
4. **Task Routes**: Handles Flask routes for task-related operations, interfacing with `FileHandler`, `TaskManager`, and `MarkdownConverter`.
5. **Notes Routes**: Manages Flask routes for note operations, leveraging `NotesManager` and `TypeHierarchyValidator`.
6. **Prompt Routes**: Defines routes for retrieving markdown prompt documents, using `PromptManager`.
7. **Notes Manager**: Manages the addition, update, deletion, and retrieval of notes, maintaining a structured JSON data format.
8. **App**: The central Flask application file, integrating all modules and managing configurations, CORS, and error handling.
9. **Type Hierarchy Validator**: Validates hierarchical structures of note types based on a JSON-defined schema.
10. **Prompt Manager**: Handles the retrieval of markdown files, centralizing the logic for file reading.
11. **Task Manager**: Responsible for extracting specific task data from JSON, crucial for task-related operations.
12. **Disk Routes**: Defines routes for disk-related file operations, supporting various file formats.
13. **Disk Manager**: Manages disk operations, providing a unified interface for reading and writing files in different formats.
14. **Conversion**: Converts JSON data to Markdown, primarily used for generating readable API documentation.

### Interactions and Data Flow
- **Task and Note Management**: The `Task Routes` and `Notes Routesy` modules utilize respective manager classes (`TaskManager`, `NotesManager`) to perform specific operations. They interact with the `File Handler` module for file I/O operations.
- **Markdown Conversion**: The `Markdown Convertery` module is used primarily in `Task Routes` for presenting tasks in a Markdown format.
- **API Security**: The `aAPI Authenticator` module provides decorators to secure Flask routes across the application.
- **File Operations**: `Disk Routes` and `Disk Manager` work in tandem to handle file operations requested through API endpoints.
- **Error Handling and Logging**: Implemented throughout the modules, enhancing debugging and application monitoring.

### Application Configuration and Execution
- **App.py**: As the entry point, it sets up the Flask application, registers blueprints for routing, and configures middleware for CORS and logging.
- **Environment Setup**: Utilizes environment variables for configuration, ensuring flexibility and adaptability to different deployment environments.


This summary provides an overview of the application's architecture and the interactions between its components.

## Documentation for `Test Runner`, `Test Logger` and `Test Cases`

### Overview
The provided Python scripts form a comprehensive testing framework for a Flask-based API application. They cover various aspects such as executing tests (`test_runner.py`), logging test results (`test_logger.py`), and defining test cases (`test_cases.py`). This framework ensures that different components of the Flask application are functioning correctly and as expected.

#### Test Runner
- **Purpose**: Executes API tests for different endpoints.
- **Key Functions**:
  - `test_endpoint()`: Sends requests to specified API endpoints and logs responses based on the HTTP method, status code, and content type.
  - `run_tests()`: Executes a series of predefined tests from `test_cases.py`.
- **Usage**:
  - Can be run directly or used as a module to execute specific tests.
  - Supports command-line arguments for selective test execution.
- **Integration with Other Components**:
  - Utilizes `test_cases.py` for test definitions.
  - Relies on `test_logger.py` for logging test outcomes.
  - Requires `test_config.py` for configuration settings like API keys.

#### Test Logger
- **Purpose**: Manages the logging of test results in Markdown format.
- **Key Functions**:
  - Logging functions (`log_json_response`, `log_response`, `log_error`, `log_exception`, `log_markdown_response`) for different test outcomes.
- **Usage**:
  - Automatically called by `test_runner.py` to log test results.
  - Outputs logs to a Markdown file, making them easily readable and accessible.

#### Test Cases
- **Purpose**: Contains the definitions of individual API test cases.
- **Key Features**:
  - Test cases are defined as a list of dictionaries, each representing a specific API call.
  - Includes details like endpoint, method, headers, data, and a brief overview of the test.
- **Usage**:
  - Imported and used by `test_runner.py` to execute tests.
  - Can be easily modified to add or change test cases.

### Application and Testing Workflow
1. **Setting Up Tests**: Test cases are defined in `test_cases.py`, including the expected outcomes.
2. **Executing Tests**: `test_runner.py` runs the tests, making requests to the API and handling responses.
3. **Logging Results**: Responses are logged by `test_logger.py`, providing a detailed record of each test.
4. **Running Specific Tests**: The framework supports running specific tests through command-line arguments.

### Key Considerations
- **Error Handling**: Comprehensive error handling is implemented to capture and log exceptions and unexpected responses.
- **Modularity**: The modular structure allows for easy modification and extension of tests and logging mechanisms.
- **Scalability**: New tests can be added to `test_cases.py` without altering the core testing mechanism.

---

## Tests and Validation

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

## OpenAI Schema

```json
{
    "openapi": "3.1.0",
    "info": {
        "title": "Tasks, Notes and Documents API for Custom GPT",
        "description": "API for managing tasks, notes, and documents in the '{project}' project, including task updates, note management, and document retrieval.",
        "version": "1.0.0"
    },
    "servers": [
        {
            "url": "https://api.ignite.webally.co.za"
        }
    ],
    "security": [
        {
            "ApiKeyAuth": []
        }
    ],
    "paths": {
        "/tasks/{project}": {
            "get": {
                "operationId": "getTasksByProject",
                "summary": "Get All Tasks in '{project}'",
                "description": "Retrieves a complete list of tasks associated with a specified '{project}'. Results can be formatted in either JSON or Markdown, based on the 'format' query parameter.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    },
                    {
                        "name": "format",
                        "in": "query",
                        "description": "Format of the tasks (json/md)",
                        "schema": {
                            "type": "string",
                            "enum": [
                                "json",
                                "md"
                            ]
                        },
                        "required": false
                    }
                ],
                "responses": {
                    "200": {
                        "description": "A list of tasks",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/GetTasksResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/tasks/{project}/{taskId}": {
            "get": {
                "operationId": "getTasksByProjectAndTaskId",
                "summary": "Get Specific Task in '{project}'",
                "description": "Fetches details for a specific task, identified by 'taskId', within the '{project}'. Supports JSON or Markdown output formats, selectable through the 'format' query parameter.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    },
                    {
                        "name": "taskId",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "format",
                        "in": "query",
                        "description": "Format of the tasks (json/md)",
                        "schema": {
                            "type": "string",
                            "enum": [
                                "json",
                                "md"
                            ]
                        },
                        "required": false
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Details of the specified task",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/TaskDetails"
                                }
                            }
                        }
                    }
                }
            },
            "put": {
                "operationId": "updateTaskByProjectAndTaskId",
                "summary": "Update Task or Subtask in '{project}'",
                "description": "Updates the status, description, or other modifiable fields of a specified task or subtask within the '{project}'. Requires 'taskId' for identifying the specific task.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    },
                    {
                        "name": "taskId",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    }
                ],
                "requestBody": {
                    "required": true,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/UpdateTaskRequest"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Task updated successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/SimpleMessageResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/notes/{project}/add": {
            "post": {
                "operationId": "addNoteToProject",
                "summary": "Add a Note in '{project}'",
                "description": "Creates a new note within the '{project}'. The note content is specified in the request body. Optionally, a unique identifier can be provided for note categorization or location tagging.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    },
                    {
                        "name": "action",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": [
                                "add",
                                "update/{noteId}"
                            ]
                        }
                    },
                    {
                        "name": "identifier",
                        "in": "query",
                        "description": "Unique identifier for the note location",
                        "schema": {
                            "type": "string"
                        },
                        "required": false
                    }
                ],
                "requestBody": {
                    "required": true,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/NoteRequest"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Note added or updated successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/NoteResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/notes/{project}/update/{noteId}": {
            "post": {
                "operationId": "updateNoteByProjectAndNoteId",
                "summary": "Update Note in '{project}'",
                "description": "Modifies an existing note, identified by 'noteId', within the '{project}'. The updated content or other note attributes are provided in the request body.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    },
                    {
                        "name": "noteId",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "identifier",
                        "in": "query",
                        "description": "Unique identifier for the note location",
                        "schema": {
                            "type": "string"
                        },
                        "required": true
                    }
                ],
                "requestBody": {
                    "required": true,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/NoteRequest"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Note updated successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/NoteResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/notes/{project}/delete/{noteId}": {
            "delete": {
                "operationId": "deleteProjectNoteByNoteId",
                "summary": "Delete a Note in '{project}'",
                "description": "Permanently removes a specified note, identified by 'noteId', from the '{project}'. This action cannot be undone.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    },
                    {
                        "name": "noteId",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "string"
                        }
                    },
                    {
                        "name": "identifier",
                        "in": "query",
                        "description": "Unique identifier for the note location",
                        "schema": {
                            "type": "string"
                        },
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Note deleted successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/SimpleMessageResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/notes/{project}/get": {
            "get": {
                "operationId": "getNotesByIdentifier",
                "summary": "Get Notes by Identifier",
                "description": "Fetches all notes associated with a given identifier within the '{project}'. This allows for retrieving notes grouped or categorized under a common identifier.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    },
                    {
                        "name": "identifier",
                        "in": "query",
                        "description": "Unique identifier for the note location",
                        "schema": {
                            "type": "string"
                        },
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "List of notes for the given identifier",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/NotesByIdentifierResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/prompts/{project}/get": {
            "get": {
                "operationId": "getPromptByProject",
                "summary": "Retrieve a Markdown Prompt",
                "description": "Retrieves a markdown-formatted prompt related to the '{project}'. This endpoint is typically used for fetching structured text or prompts for documentation or guides related to the project.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Markdown prompt retrieved successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/MarkdownPromptResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/disk/{project}/schema/api": {
            "get": {
                "operationId": "getSchemaByProject",
                "summary": "Get OpenAPI Schema",
                "description": "Provides the complete OpenAPI schema for the '{project}' API, encompassing tasks, notes, and other related endpoints. The schema can be requested in JSON, Markdown, or YAML formats.",
                "parameters": [
                    {
                        "name": "project",
                        "in": "path",
                        "required": true,
                        "description": "The name of the current project",
                        "schema": {
                            "type": "string",
                            "default":"ignite"
                        }
                    },
                    {
                        "name": "format",
                        "in": "query",
                        "required": true,
                        "description": "Format of the schema (json/md/yml)",
                        "schema": {
                            "type": "string",
                            "enum": [
                                "json",
                                "md",
                                "yml"
                            ]
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "The complete OpenAPI schema for the '{project}' API",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "openapi": {"type": "string"},
                                        "info": {"$ref": "#/components/schemas/Info"},
                                        "servers": {"type": "array", "items": {"$ref": "#/components/schemas/Server"}},
                                        "paths": {
                                            "type": "object",
                                            "additionalProperties": {
                                                "type": "object",
                                                "properties": {
                                                    "get": {"$ref": "#/components/schemas/Operation"},
                                                    "post": {"$ref": "#/components/schemas/Operation"},
                                                    "put": {"$ref": "#/components/schemas/Operation"},
                                                    "delete": {"$ref": "#/components/schemas/Operation"}
                                                }
                                            }
                                        },
                                        "components": {
                                            "type": "object",
                                            "properties": {
                                                "schemas": {"type": "object"},
                                                "responses": {"type": "object"},
                                                "parameters": {"type": "object"},
                                                "examples": {"type": "object"},
                                                "requestBodies": {"type": "object"},
                                                "headers": {"type": "object"},
                                                "securitySchemes": {"type": "object"},
                                                "links": {"type": "object"},
                                                "callbacks": {"type": "object"}
                                            }
                                        }
                                    },
                                    "additionalProperties": false
                                }
                            }
                        }
                    }
                }
            }
        }
    },        
    "components": {
        "securitySchemes": {
            "ApiKeyAuth": {
                "type": "apiKey",
                "in": "header",
                "name": "X-API-Key"
            }
        },
        "schemas": {
            "GetTasksResponse": {
                "type": "object",
                "properties": {
                    "overview": {
                        "type": "string"
                    },
                    "tasks": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/TaskDetails"
                        }
                    }
                }
            },
            "TaskDetails": {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "boolean"
                    },
                    "task": {
                        "type": "string"
                    }
                }
            },
            "UpdateTaskRequest": {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "boolean"
                    },
                    "description": {
                        "type": "string",
                        "nullable": true
                    }
                }
            },
            "SimpleMessageResponse": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string"
                    }
                }
            },
            "NoteRequest": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string"
                    }
                },
                "required": [
                    "content"
                ]
            },
            "NoteResponse": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string"
                    },
                    "note_id": {
                        "type": "string",
                        "nullable": true
                    }
                }
            },
            "NotesByIdentifierResponse": {
                "type": "object",
                "properties": {
                    "notes": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/NoteDetails"
                        }
                    }
                }
            },
            "NoteDetails": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                }
            },
            "MarkdownPromptResponse": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "format": "markdown"
                    }
                }
            }
        }
    }
}
```