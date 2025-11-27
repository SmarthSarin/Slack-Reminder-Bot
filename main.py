from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os
import time
import csv
from datetime import datetime

# ==========================
# Step 1: Setup and Inputs
# ==========================
load_dotenv()
slack_token = os.getenv("SLACK_BOT_TOKEN")

if not slack_token:
    raise ValueError("❌ SLACK_BOT_TOKEN not found in .env file")

# Create Slack client
client = WebClient(token=slack_token)

# Create logs folder if missing
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Ask for log file name
file_name = input("Enter log file name (no extension): ").strip()
if not file_name:
    file_name = f"SlackLog_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

CSV_REPORT = os.path.join(LOG_DIR, f"{file_name}.csv")

print(f"\n🧾 Log file will be saved at: {CSV_REPORT}\n")

# ==========================
# Step 2: Email List
# ==========================
emails = [
]

# ==========================
# Step 3: Base Message
# ==========================
base_message = (
)

# ==========================
# Step 4: Prepare CSV
# ==========================
csv_headers = ["Timestamp", "Email", "User Name", "Status", "Details"]

with open(CSV_REPORT, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

# ==========================
# Step 5: Send Messages
# ==========================
for email in emails:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        print(f"🔍 Looking up user: {email}")
        user_info = client.users_lookupByEmail(email=email)
        user_id = user_info["user"]["id"]
        user_real_name = user_info["user"]["real_name"]

        message = f"Hi {user_real_name}, {base_message}"
        client.chat_postMessage(channel=user_id, text=message)

        print(f"✅ Message sent to {email} ({user_real_name})")

        # Write success to CSV
        with open(CSV_REPORT, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, email, user_real_name, "✅ Sent", "Message delivered successfully"])

        time.sleep(1)  # Avoid hitting Slack rate limits

    except SlackApiError as e:
        error_msg = e.response.get("error", "Unknown Slack API error")
        print(f"❌ Slack API error for {email}: {error_msg}")

        with open(CSV_REPORT, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, email, "-", "❌ Failed", error_msg])

    except Exception as e:
        print(f"⚠️ Unknown error for {email}: {e}")

        with open(CSV_REPORT, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, email, "-", "⚠️ Error", str(e)])

print("\n📜 Message dispatch completed successfully!")
print(f"📁 CSV report saved at: {CSV_REPORT}")
