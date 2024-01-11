# Tasks and Notes API for Custom GPT

## 1. Tasks in JSON Format

### 1.1. Get All Tasks in 'ignite' - JSON Format

- **Endpoint:** `https://api.ignite.webally.co.za/tasks/ignite`

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
    "10": {
      "10.1": {
        "status": false,
        "task": "Plan a comprehensive system test covering all components."
      },
      "10.2": {
        "status": false,
        "task": "Document test cases and expected outcomes."
      },
      "10.3": {
        "status": false,
        "task": "Execute the system test with a team."
      },
      "10.4": {
        "status": false,
        "task": "Collect feedback and logs for analysis."
      },
      "10.5": {
        "status": false,
        "task": "Make necessary adjustments based on test results."
      },
      "description": "End-to-End System Test",
      "status": false
    },
    "2": {
      "2.1": {
        "status": false,
        "task": "Set up a new Chrome extension project."
      },
      "2.2": {
        "status": false,
        "task": "Create a manifest file with necessary permissions."
      },
      "2.3": {
        "status": false,
        "task": "Design a basic popup UI for the extension."
      },
      "2.4": {
        "status": false,
        "task": "Implement background scripts for core functionalities."
      },
      "2.5": {
        "status": false,
        "task": "Test the basic extension in Chrome."
      },
      "description": "Develop Chrome Extension Basic Structure",
      "status": false
    },
    "3": {
      "3.1": {
        "status": false,
        "task": "Research Chrome APIs for taking screenshots."
      },
      "3.2": {
        "status": false,
        "task": "Write a function to capture the current tab."
      },
      "3.3": {
        "status": false,
        "task": "Integrate screenshot functionality into the extension UI."
      },
      "3.4": {
        "status": false,
        "task": "Test screenshot capture and storage."
      },
      "3.5": {
        "status": false,
        "task": "Optimize screenshot quality and performance."
      },
      "description": "Implement Screenshot Functionality",
      "status": false
    },
    "4": {
      "4.1": {
        "status": false,
        "task": "Design a user-friendly input interface in the popup."
      },
      "4.2": {
        "status": false,
        "task": "Implement form handling and data validation."
      },
      "4.3": {
        "status": false,
        "task": "Ensure responsive design for different screen sizes."
      },
      "4.4": {
        "status": false,
        "task": "Test the interface for usability."
      },
      "4.5": {
        "status": false,
        "task": "Incorporate feedback mechanism for user inputs."
      },
      "description": "Create User Input Interface",
      "status": false
    },
    "5": {
      "5.1": {
        "status": false,
        "task": "Choose a backend technology (Node.js, Python, etc.)."
      },
      "5.2": {
        "status": false,
        "task": "Initialize a new server application project."
      },
      "5.3": {
        "status": false,
        "task": "Create API endpoints to receive data from the extension."
      },
      "5.4": {
        "status": false,
        "task": "Implement data processing and storage mechanisms."
      },
      "5.5": {
        "status": false,
        "task": "Test server functionality and extension communication."
      },
      "description": "Set Up Server-Side Application",
      "status": false
    },
    "6": {
      "6.1": {
        "status": false,
        "task": "Obtain OpenAI API key and set up environment variables."
      },
      "6.2": {
        "status": false,
        "task": "Write a function to send data to OpenAI API."
      },
      "6.3": {
        "status": false,
        "task": "Process the API response for actionable insights."
      },
      "6.4": {
        "status": false,
        "task": "Implement error handling and logging for the API integration."
      },
      "6.5": {
        "status": false,
        "task": "Test API integration with sample data."
      },
      "description": "Integrate OpenAI Assistant API",
      "status": false
    },
    "7": {
      "7.1": {
        "status": false,
        "task": "Design logic to interpret suggestions from the API."
      },
      "7.2": {
        "status": false,
        "task": "Map suggestions to actionable code updates."
      },
      "7.3": {
        "status": false,
        "task": "Develop a system to apply updates to the codebase."
      },
      "7.4": {
        "status": false,
        "task": "Test the application of updates in a controlled environment."
      },
      "7.5": {
        "status": false,
        "task": "Set up rollback mechanisms in case of faulty updates."
      },
      "description": "Handle Server Responses and Suggestions",
      "status": false
    },
    "8": {
      "8.1": {
        "status": false,
        "task": "Create test cases for data transmission."
      },
      "8.2": {
        "status": false,
        "task": "Simulate various user scenarios."
      },
      "8.3": {
        "status": false,
        "task": "Monitor server logs during testing."
      },
      "8.4": {
        "status": false,
        "task": "Optimize data transmission efficiency."
      },
      "8.5": {
        "status": false,
        "task": "Ensure data integrity and security."
      },
      "description": "Testing Extension-Server Communication",
      "status": false
    },
    "9": {
      "9.1": {
        "status": false,
        "task": "Develop integration points between the extension and code-server."
      },
      "9.2": {
        "status": false,
        "task": "Test extension access to the code-server environment."
      },
      "9.3": {
        "status": false,
        "task": "Implement user authentication and authorization."
      },
      "9.4": {
        "status": false,
        "task": "Ensure stable and secure connection."
      },
      "9.5": {
        "status": false,
        "task": "Document the process for future users."
      },
      "description": "Link Extension with Code Server",
      "status": false
    }
  }
}
```

### 1.2. Get Specific Task in 'ignite' - JSON Format

- **Endpoint:** `https://api.ignite.webally.co.za/tasks/ignite/1`

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

- **Endpoint:** https://api.ignite.webally.co.za/tasks/ignite/1.1

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

### 2.1. Get All Tasks in 'ignite' - Markdown Format

- **Endpoint:** https://api.ignite.webally.co.za/tasks/ignite?format=md

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

## [ ] 3. Implement Screenshot Functionality
- [ ] 3.1. Research Chrome APIs for taking screenshots.
- [ ] 3.2. Write a function to capture the current tab.
- [ ] 3.3. Integrate screenshot functionality into the extension UI.
- [ ] 3.4. Test screenshot capture and storage.
- [ ] 3.5. Optimize screenshot quality and performance.

## [ ] 4. Create User Input Interface
- [ ] 4.1. Design a user-friendly input interface in the popup.
- [ ] 4.2. Implement form handling and data validation.
- [ ] 4.3. Ensure responsive design for different screen sizes.
- [ ] 4.4. Test the interface for usability.
- [ ] 4.5. Incorporate feedback mechanism for user inputs.

## [ ] 5. Set Up Server-Side Application
- [ ] 5.1. Choose a backend technology (Node.js, Python, etc.).
- [ ] 5.2. Initialize a new server application project.
- [ ] 5.3. Create API endpoints to receive data from the extension.
- [ ] 5.4. Implement data processing and storage mechanisms.
- [ ] 5.5. Test server functionality and extension communication.

## [ ] 6. Integrate OpenAI Assistant API
- [ ] 6.1. Obtain OpenAI API key and set up environment variables.
- [ ] 6.2. Write a function to send data to OpenAI API.
- [ ] 6.3. Process the API response for actionable insights.
- [ ] 6.4. Implement error handling and logging for the API integration.
- [ ] 6.5. Test API integration with sample data.

## [ ] 7. Handle Server Responses and Suggestions
- [ ] 7.1. Design logic to interpret suggestions from the API.
- [ ] 7.2. Map suggestions to actionable code updates.
- [ ] 7.3. Develop a system to apply updates to the codebase.
- [ ] 7.4. Test the application of updates in a controlled environment.
- [ ] 7.5. Set up rollback mechanisms in case of faulty updates.

## [ ] 8. Testing Extension-Server Communication
- [ ] 8.1. Create test cases for data transmission.
- [ ] 8.2. Simulate various user scenarios.
- [ ] 8.3. Monitor server logs during testing.
- [ ] 8.4. Optimize data transmission efficiency.
- [ ] 8.5. Ensure data integrity and security.

## [ ] 9. Link Extension with Code Server
- [ ] 9.1. Develop integration points between the extension and code-server.
- [ ] 9.2. Test extension access to the code-server environment.
- [ ] 9.3. Implement user authentication and authorization.
- [ ] 9.4. Ensure stable and secure connection.
- [ ] 9.5. Document the process for future users.

## [ ] 10. End-to-End System Test
- [ ] 10.1. Plan a comprehensive system test covering all components.
- [ ] 10.2. Document test cases and expected outcomes.
- [ ] 10.3. Execute the system test with a team.
- [ ] 10.4. Collect feedback and logs for analysis.
- [ ] 10.5. Make necessary adjustments based on test results.
```

### 2.2. Get Specific Task in 'ignite' - Markdown Format

**Endpoint:** `https://api.ignite.webally.co.za/tasks/ignite/1?format=md`

```md
## [x] 1. Install and Configure Code Server
- [x] 1.1. Choose a suitable server for installation.
- [x] 1.2. Install code-server following the official documentation.
- [x] 1.3. Configure access and security settings.
- [x] 1.4. Set up a domain or subdomain for code-server access.
- [x] 1.5. Test the code-server setup.
```

### 2.3. Get Specific Subtask in 'ignite' - Markdown Format

**Endpoint:** `https://api.ignite.webally.co.za/tasks/ignite/1.1?format=md`

```md
- [x] 1.1. Choose a suitable server for installation.
```

## 3. Add / Update & Delete Tasks

### 3.1. Testing update of task 1 status to true in 'ignite' project.

- **Endpoint:** `https://api.ignite.webally.co.za/tasks/ignite/1`
- **Status Code:** `200`

```json
{
    "message": "Task updated successfully"
}
```

### 3.2. Testing update of task 2 status and description in 'ignite' project.

- **Endpoint:** `https://api.ignite.webally.co.za/tasks/ignite/2`
- **Status Code:** `200`

```json
{
    "message": "Task updated successfully"
}
```

### 3.3. Testing update of subtask 1.1 status to true in 'ignite' project.

- **Endpoint:** `https://api.ignite.webally.co.za/tasks/ignite/1.1`
- **Status Code:** `200`

```json
{
    "message": "Task updated successfully"
}
```

### 3.4. Testing update of subtask 2.2 status to false in 'ignite' project.

- **Endpoint:** `https://api.ignite.webally.co.za/tasks/ignite/2.2`
-** Status Code:** `200`

```json
{
    "message": "Task updated successfully"
}
```

## 4. Add Notes to Project, Files, Classes and Files 

### 4.1. Testing retrieval of notes in Markdown format.

**Endpoint:** `https://api.ignite.webally.co.za/notes/ignite?format=md`

Error: Unrecognized data format for Markdown conversion.

### 4.2. Testing addition of a new note.

- **Endpoint:** `https://api.ignite.webally.co.za/notes/ignite/add`
- **Status Code:** `200`

```json
{
    "message": "Note added successfully",
    "note_id": "8"
}
```

### 4.3. Testing update of an existing note.

**Endpoint:** `https://api.ignite.webally.co.za/notes/ignite/update`

```json
No response
```

### 4.4. Testing deletion of a note.

**Endpoint:** https://api.ignite.webally.co.za/notes/ignite/delete

```json
No response
```

# Get Prompt

## Overview
Testing retrieval of a markdown prompt.

### Endpoint: https://api.ignite.webally.co.za/prompts/ignite?format=md
```json
No response
```




