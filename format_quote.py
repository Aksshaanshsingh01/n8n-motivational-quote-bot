# This script runs inside an n8n Code node.
# It takes the JSON data from the previous HTTP Request node and formats it.

# Get the data from the previous node and convert it to a Python dictionary
data = items[0].json.to_py()

# Format the quote and author into a clean, readable string
formatted_quote = f"\"{data['content']}\"\n\n- {data['author']}"

# Return the formatted text for the next node in the workflow
return [{'json': {'quote_text': formatted_quote}}]
