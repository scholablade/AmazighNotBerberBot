# Import The Python Reddit API Wrapper
import praw
# Potenial words in the title
WORDS = ["berber","berbers"]
# Response to title
Reply = """Please use the correct to describe the Amazigh People which is Amazigh not Berbers, it is considered
 offensive by many Amazigh People, just so you know am a bot."""

def main():
    # Initiate Reddit instance with credintials
    # Subreddit
    subreddit = reddit.subreddit("AmazighPeople")
    # Look for submission and execute function
    for submission in subreddit.stream.submissions():
        process_submission(submission)

def process_submission(submission):

    # Make title lowercase for the WORDS list
    Title = submission.title.lower()
    for Phrase in WORDS:
        if Phrase in Title:
            print(f"Replying to: {submission.title}")
            submission.reply(body=Reply)
            break
