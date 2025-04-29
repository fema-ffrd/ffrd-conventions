"""Utility to export schemas for viewing in markdown table."""

import json

import pandas as pd


def props_to_header(schema_props: dict, model: str = "HEC-RAS") -> str:
    """Export schema top level props to doc."""
    return f"""# {model} Naming Conventions
    Draft {schema_props['title']}\n
    schema version: {schema_props['version']}\n
    Description: {schema_props['title']}\n
    """


with open("hec-ras/json-schema/schema.json", "r") as f:
    schema = json.load(f)
    properties_data = [
        {
            "Property": prop_name,
            "Type": prop_details.get("type", ""),
            "Description": prop_details.get("description", ""),
            "Pattern": prop_details.get("pattern", ""),
            "Examples": ", ".join(prop_details.get("examples", [])),
        }
        for prop_name, prop_details in schema["properties"].items()
    ]
    df = pd.DataFrame(properties_data)


with open("hec-ras/readme.md", "w") as f:
    f.write(props_to_header(schema))
    f.write("\n" + df.to_markdown(index=False) + "\n")
