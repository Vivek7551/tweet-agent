import tweepy
import os
import re
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

def split_into_thread(text: str, max_length: int = 270) -> list[str]:
    """
    Splits text into tweet-sized chunks, respecting word boundaries.
    Reserves space for thread numbering e.g. (1/5)
    """
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        # +1 for the space before the word
        if len(current_chunk) + len(word) + 1 <= max_length:
            current_chunk += (" " if current_chunk else "") + word
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk)

    # Add numbering now that we know total count
    total = len(chunks)
    if total > 1:
        numbered = []
        for i, chunk in enumerate(chunks, 1):
            label = f" ({i}/{total})"
            numbered.append(chunk + label)
        return numbered

    return chunks


def post_thread(text: str):
    tweets = split_into_thread(text)
    total = len(tweets)

    print(f"\n--- Preview: {total} tweet(s) ---")
    for i, tweet in enumerate(tweets, 1):
        print(f"\n[{i}] ({len(tweet)} chars)\n{tweet}")

    confirm = input("\n\nPost this thread? (y/n): ")
    if confirm.lower() != 'y':
        print("Cancelled.")
        return

    previous_tweet_id = None

    for i, tweet in enumerate(tweets, 1):
        if previous_tweet_id:
            response = client.create_tweet(
                text=tweet,
                in_reply_to_tweet_id=previous_tweet_id
            )
        else:
            response = client.create_tweet(text=tweet)

        previous_tweet_id = response.data['id']
        print(f"Posted tweet {i}/{total} — ID: {previous_tweet_id}")

    print("\nThread posted successfully!")


if __name__ == "__main__":
    print("Paste your content below. When done, press Enter twice:\n")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)

    full_text = "\n".join(lines).strip()
    if full_text:
        post_thread(full_text)
    else:
        print("No content provided.")