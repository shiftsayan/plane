import requests

class PlaneSendBase():

    def __init__(self, profile):
        self.domain = profile.domain
        self.api_key = profile.api_key
        self.sender = profile.sender
        self.recepients = profile.recepients
        self.reply_to = profile.reply_to or profile.sender


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

    def __init__(self, template, profile):
        self.template = template
        super().__init__(profile)

    def send(self):
        return

def PlaneSendReminder(PlaneSendBase):
    pass