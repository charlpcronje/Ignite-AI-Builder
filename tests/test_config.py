# test_config.py
# Configuration for API testing

# API Base URL
base_url = "https://api.ignite.webally.co.za"

# API Key
api_key = "_mu0WygMRETwooV39aj0PQ"  # Replace with your actual API key

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
