import time

class Email:
    def __init__(self, sender, subject, body):
        self.sender = sender
        self.subject = subject
        self.body = body

    def __str__(self):
        return f"From: {self.sender}\nSubject: {self.subject}\nBody: {self.body[:50]}...\n"

class ZeroOutputSpamFilterAgent:
    """
    This AI agent embodies the 'Zero Output' paradigm.
    It silently filters spam emails, preventing them from reaching the user's inbox.
    The user's experience is simply a clean inbox, without explicit notifications
    about the agent's actions or the number of emails filtered.
    """
    def __init__(self):
        self.spam_keywords = ["viagra", "money now", "free prize", "urgent action", "unsubscribe here", "lottery win"]
        self.suspicious_domains = ["bad-domain.com", "scam-mail.net"]
        self.filtered_count = 0 # Internal tracking, not exposed to user

    def _is_spam(self, email):
        """Internal method to determine if an email is spam."""
        # Check sender domain
        if any(domain in email.sender for domain in self.suspicious_domains):
            return True
        # Check subject and body for keywords
        for keyword in self.spam_keywords:
            if keyword in email.subject.lower() or keyword in email.body.lower():
                return True
        return False

    def process_inbox(self, inbox):
        """
        Processes the inbox to remove spam.
        This is the 'zero output' part: it doesn't tell the user what it did,
        it just returns the desired state (a clean inbox).
        """
        clean_inbox = []
        for email in inbox:
            if not self._is_spam(email):
                clean_inbox.append(email)
            else:
                self.filtered_count += 1 # Agent silently tracks its work
                # The agent takes action (deletes/moves to spam) without user notification.
                # This is the core of the 'zero output' concept.
        return clean_inbox

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Initial Inbox (as seen by the system) ---")
    raw_inbox = [
        Email("alice@example.com", "Meeting Reminder", "Hi team, just a reminder about our meeting tomorrow."),
        Email("bob@bad-domain.com", "URGENT: Your Account Needs Attention!", "Click here now to avoid account suspension!"),
        Email("charlie@dev.to", "New Article Alert", "Check out my latest post on AI paradigms."),
        Email("spam-bot@scam-mail.net", "You've Won a FREE PRIZE!", "Claim your lottery winnings by providing your bank details."),
        Email("diana@example.com", "Project Update", "The project is progressing well, details attached."),
        Email("pharma@generic.com", "Enhance Your Life with VIAGRA!", "Special offer, buy now!"),
    ]

    for i, email in enumerate(raw_inbox):
        print(f"Email {i+1}:\n{email}")
    print(f"Total emails in raw inbox: {len(raw_inbox)}\n")

    # Initialize the zero-output AI agent
    spam_filter = ZeroOutputSpamFilterAgent()

    print("--- AI Agent (Spam Filter) is working silently... ---")
    # Simulate processing time
    time.sleep(2)

    # The agent processes the inbox. The user doesn't see any explicit output from this call.
    # The value is delivered by the *absence* of spam in the returned inbox.
    clean_inbox = spam_filter.process_inbox(raw_inbox)

    print("\n--- User's Clean Inbox (after agent's silent work) ---")
    if not clean_inbox:
        print("Your inbox is empty!")
    else:
        for i, email in enumerate(clean_inbox):
            print(f"Email {i+1}:\n{email}")
    print(f"Total emails in clean inbox: {len(clean_inbox)}")

    # Internally, the agent knows what it did, but it doesn't tell the user.
    # This is for demonstration purposes only, an actual zero-output agent
    # would not expose this count directly to the user interface.
    print(f"\n(Agent's internal log: Silently filtered {spam_filter.filtered_count} spam emails.)")
    print("The user's experience is simply a clean, productive inbox.")
