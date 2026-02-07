# Slack Bulk Messenger with CSV Logging 📨

A robust Python utility designed to send personalized bulk messages to Slack users via email lookup. It features error handling, rate limiting to adhere to API standards, and generates detailed CSV reports for audit trails.

## 🚀 Features

- **Email-to-User Lookup:** Automatically resolves email addresses to Slack User IDs.
- **Personalized Messages:** Greets users by their real name (fetched from Slack).
- **Audit Logging:** Generates a timestamped CSV report (`logs/`) for every execution, tracking successful deliveries and errors.
- **Rate Limiting:** Built-in delays to prevent Slack API rate limit errors.
- **Secure Configuration:** Uses environment variables to keep sensitive tokens out of the source code.

## 🛠️ Prerequisites

- Python 3.8+
- A Slack Workspace
- A Slack App with a **Bot User OAuth Token** (`xoxb-...`)

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/SmarthSarin/Slack-Reminder-Bot.git && cd Slack-Reminder-Bot
```
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Set up Environment Variables:**
Create a file named `.env` in the root directory and add your Slack Bot Token:
```ini
SLACK_BOT_TOKEN=xoxb-your-token-here
```
*(Note: The `.env` file is ignored by Git to protect your secrets.)*

## ⚙️ Configuration & Usage

1. **Prepare your Target List:**
Open `main.py` and update the `emails` list with the recipients:
```python
emails = [
    "user1@example.com",
    "user2@example.com"
]

```


2. **Customize the Message:**
Edit the `base_message` variable in `main.py`. You can use Slack formatting (e.g., `*bold*`, `<https://link.com|Link>`).
3. **Run the Script:**
```bash
python main.py

```


4. **Check the Logs:**
After execution, check the `logs/` directory. A CSV file will be created (e.g., `SlackLog_20240210_103000.csv`) containing the status of every message.

## 🛡️ Required Slack Permissions

Ensure your Slack App has the following **Bot Token Scopes**:

* `chat:write` (To send messages)
* `users:read` (To view user profiles)
* `users:read.email` (To lookup users by email)

## ⚠️ Security Note

* **Never commit your `.env` file** or the `logs/` directory to GitHub.
* This repository includes a `.gitignore` file to prevent accidental uploads of sensitive data.
