import requests

class PlaneSendBase():

    def __init__(self, secrets):
        self.domain = secrets.domain
        self.api_key = secrets.api_key
        self.sender = secrets.sender
        self.recepients = secrets.recepients
        self.reply_to = secrets.reply_to or secrets.sender


    def __send(self, subject, html, deliverytime):
        return "May the source be with you!"
        return requests.post(
            "https://api.mailgun.net/v3/" + self.domain + "/messages",
            auth=("api", self.api_key),
            data={
                "from": self.sender,
                "to": self.recepients,
                'h:Reply-To': self.reply_to,
                "subject": subject,
                "html": html,
                "o:deliverytime": deliverytime,
            }
        )

class PlaneSendTemplate(PlaneSendBase):

    def __init__(self, template, secrets):
        self.template = template
        super().__init__(secrets)

    def send(self):
        return

def PlaneSendReminder(PlaneSendBase):
    pass