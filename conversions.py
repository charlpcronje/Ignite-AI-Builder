# conversion_module.py
import json

def openapi_to_markdown(openapi_json):
    md_content = ""

    # Adding general information
    info = openapi_json.get("info", {})
    md_content += f"# {info.get('title', 'API Documentation')}\n"
    md_content += f"**Version:** {info.get('version', 'N/A')}\n\n"
    md_content += f"{info.get('description', '')}\n\n"

    # Adding server information
    servers = openapi_json.get("servers", [])
    if servers:
        md_content += "## Servers\n"
        for server in servers:
            md_content += f"- URL: {server.get('url', 'N/A')}\n"
        md_content += "\n"

    # Adding paths and operations
    paths = openapi_json.get("paths", {})
    for path, operations in paths.items():
        md_content += f"## Path: `{path}`\n\n"
        for operation, details in operations.items():
            md_content += f"### {operation.upper()}\n"
            md_content += f"**Summary:** {details.get('summary', 'N/A')}\n\n"
            md_content += f"**Description:** {details.get('description', 'N/A')}\n\n"
            md_content += "#### Parameters\n"
            for param in details.get('parameters', []):
                md_content += f"- {param.get('name', 'N/A')} ({param.get('in', 'N/A')}): {param.get('description', 'N/A')}\n"
            md_content += "\n"

            # Responses
            responses = details.get("responses", {})
            md_content += "#### Responses\n"
            for status_code, response_details in responses.items():
                md_content += f"- Status {status_code}: {response_details.get('description', 'N/A')}\n"
                md_content += "\n"


            # Components (Schemas)
            components = openapi_json.get("components", {}).get("schemas", {})
            if components:
                md_content += "## Components (Schemas)\n\n"
                for schema_name, schema_details in components.items():
                    md_content += f"### {schema_name}\n"
                    properties = schema_details.get('properties', {})
                    for prop_name, prop_details in properties.items():
                        md_content += f"- **{prop_name}**: {prop_details.get('type', 'N/A')}\n"
                        if 'description' in prop_details:
                            md_content += f"  - Description: {prop_details['description']}\n"
                    md_content += "\n"

            return md_content

