import requests
import time
from datetime import datetime

# Telegram bot credentials (provided by you)
BOT_TOKEN = "7585147463:AAGoeCbGBg3FlCKHmcelPcPypUgZRo4mBOY"
CHAT_ID = "1478603931"

def send_telegram_message(message):
    """Send a message to Telegram."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=params)
        if response.status_code != 200:
            print(f"Error sending Telegram message: {response.text}")
    except Exception as e:
        print(f"Exception occurred while sending Telegram message: {str(e)}")

def get_live_update():
    """Generate a live update message based on actual progress."""
    # Simulate real-time progress (replace this with actual development status)
    current_hour = datetime.now().hour
    if current_hour < 12:  # Morning update
        return (
            "Good morning! Here's the progress on Milkbot:\n"
            "- Scraped X posts/tweets/messages from social media.\n"
            "- Processed blockchain data for February 2024.\n"
            "- Currently working on March 2024 data collection."
        )
    elif current_hour < 18:  # Midday update
        return (
            "Midday update: Today we achieved:\n"
            "- Completed scraping 5,000 posts from X and Reddit.\n"
            "- Fetched data for 35 new tokens listed on Raydium.\n"
            "- Encountered no major challenges so far."
        )
    else:  # Evening update
        return (
            "Evening update: Today we achieved:\n"
            "- Finalized scraping for March 2024.\n"
            "- Trained sentiment analysis model on new data.\n"
            "- Preparing for tomorrow's tasks: April 2024 data collection."
        )

def main():
    """Main function to send live updates at specified times."""
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time in ["08:00", "12:00", "18:00"]:
            # Generate and send live update
            live_update = get_live_update()
            send_telegram_message(live_update)
            time.sleep(60)  # Avoid repeated triggers
        time.sleep(60)  # Check time every minute

if __name__ == "__main__":
    main()