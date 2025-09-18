# n8n-motivational-quote-bot

# Automated Motivational Quote Email Bot

A simple, serverless automation workflow built with n8n that fetches a random motivational quote from a public API and emails it to a recipient every morning.

This project was built to demonstrate proficiency in API integration, Python scripting for data manipulation, and building automated workflows using low-code platforms like n8n.

## Key Features

* **Automated Daily Execution:** Runs automatically every day at 8 AM.
* **Live Data Fetching:** Connects to the `api.quotable.io` public API to get a new quote for each run.
* **Data Formatting:** A Python script cleans and formats the raw API data into a user-friendly message.
* **Email Notification:** Delivers the final quote directly to an email inbox.

## Tech Stack

* **Automation Platform:** n8n (Cloud)
* **Core Logic:** Python (for data manipulation)
* **Key Nodes:** Schedule Trigger, HTTP Request, Code, Send Email
* **API:** [Quotable](https://github.com/lukePeavey/quotable) (api.quotable.io)

## Workflow Overview

The automation pipeline consists of four main steps:

1.  **Schedule Trigger:** The workflow is initiated every morning at 8 AM.
2.  **HTTP Request Node:** Makes a `GET` request to the Quotable API to fetch a random quote.
3.  **Code Node:** A Python script receives the raw JSON data from the API. It extracts the `content` and `author`, then formats them into a clean, readable string.
4.  **Send Email Node:** The final formatted string is sent as the body of an email to the specified recipient.

### Workflow Screenshot

*(A screenshot of your final n8n workflow goes here)*
