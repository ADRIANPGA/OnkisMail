class Message:
    date = None
    sender = None
    message = None

    def __init__(self, date, sender, message):
        self.date = date
        self.sender = sender
        self.message = message
