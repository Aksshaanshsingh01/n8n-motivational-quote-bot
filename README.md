# Automated Motivational Quote Email Bot

> A serverless automation project demonstrating API integration and data handling with n8n and Python.

This workflow runs on a daily schedule, fetches a random motivational quote from a public API, formats the data using a Python script, and emails it to a specified recipient. The project was built to showcase skills directly relevant to an automation-focused role, including scheduled task execution, API consumption, and scripting.

<img width="1669" height="786" alt="image" src="https://github.com/user-attachments/assets/0477d7f8-e9e0-42c8-96b7-aec421e008cc" />

---
## Key Features

* **📅 Automated Daily Execution:** A schedule trigger runs the workflow every morning at 8 AM.
* **🌐 Live Data Fetching:** Connects to the `api.quotable.io` public API to get a new quote for each run.
* **🐍 Python for Data Formatting:** A Python script cleans and transforms the raw JSON data from the API into a user-friendly message.
* **📧 Email Notification:** Delivers the final formatted quote directly to an email inbox via SMTP.

---
## Tech Stack

* **Automation Platform:** [n8n](https://n8n.io/)
* **Scripting Language:** **Python**
* **Key n8n Nodes:** Schedule Trigger, HTTP Request, Code, Send Email
* **API:** [Quotable](https://github.com/lukePeavey/quotable) (`api.quotable.io`)

---
## Workflow Breakdown

The automation pipeline consists of four main steps:

1.  **Schedule Trigger:** Initiates the workflow on a daily schedule.

2.  **HTTP Request Node:** Makes a `GET` request to the Quotable API to fetch a random quote in JSON format.

3.  **Code Node:** A Python script ([format_quote.py](./format_quote.py)) processes the raw JSON response. It extracts the `content` and `author` keys and formats them into a clean, multi-line string.

4.  **Send Email Node:** Sends the final formatted quote as the body of an email to the specified recipient.

---
## Repository Contents

* **`README.md`**: This overview file.
* **`workflow.json`**: The complete n8n workflow, which can be imported into any n8n instance.
* **`format_quote.py`**: The standalone Python script used for data formatting within the Code Node.

### How to Use

To run this project yourself, you can import the [`workflow.json`](./workflow.json) file into your n8n canvas. You will need to configure your own credentials for the `Send Email` node.




