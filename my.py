from instagrapi import Client
import time

USERNAME = "bot__pagal_420"
PASSWORD = "vishu966"
THREAD_ID = "340282366841710301281175682371297263113"

BACK_MSG = "Hyy kaise ho aap? 😊"

client = Client()
client.login("bot__pagal_420","vishu966")

print("Bot Started...")

last_seen = {}  # user_id : last active timestamp
last_message_id = None

INACTIVE_LIMIT = 30 * 60   # 30 minutes

while True:
    messages = client.direct_messages(THREAD_ID, amount=1)  # latest message

    if messages:
        msg = messages[0]

        # ignore bot’s own messages
        if msg.user_id == client.user_id:
            pass
        else:
            user = msg.user_id

            # NEW MESSAGE?
            if msg.id != last_message_id:

                now = time.time()

                if user in last_seen:
                    # Agar user 30 minutes se inactive tha
                    if now - last_seen[user] > INACTIVE_LIMIT:
                        client.direct_send(BACK_MSG, thread_ids=[THREAD_ID])
                        print("30 min baad welcome back sent!")

                # Update last active time
                last_seen[user] = now
                last_message_id = msg.id

    time.sleep(3)