import requests
import os

class PlaneSendBase():

    def __init__(self, profile):
        self.domain = profile.domain
        self.api_key = profile.api_key
        self.sender = profile.sender
        self.recepients = profile.recepients
        self.reply_to = profile.reply_to or profile.sender

        self.path_root = 'html'
        self.shell = open(f'{self.path_root}/shell.html', 'r').read()        

    def __send(self, subject, html, deliverytime):
        return "May the source be with you!"
        return requests.post(
            f"https://api.mailgun.net/v3/{self.domain}/messages",
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

    def populate(self, content, kv):
        for (placeholder, replacement) in kv:
            content.replace(placeholder, replacement)

class PlaneSendTemplate(PlaneSendBase):

    def __init__(self, schema, profile):
        super().__init__(profile)
        self.delivery_day = schema.delivery_day
        
        self.id = f'{self.path_root}/{schema.id}' 
        self.path_body = f'{self.id}/body.html'
        self.path_content = f'{self.id}/content.html'
        self.path_default = f'{self.id}/default.html'
        self.path_backup = f'{self.id}/backup.html'


    def _restore(self):
        '''
        Restore contents of path_content using path_default and save previous version to path_backup
        '''
        os.system(f"cp {os.path.realpath(self.path_content)} {os.path.realpath(self.path_backup)}")
        os.system(f"cp {os.path.realpath(self.path_default)} {os.path.realpath(self.path_content)}")


    def execute(self):
        self._restore()
        # Read content and close
        # Generate data values using meetings.py
        # Run populate
        return


def PlaneSendReminder(PlaneSendBase):
    pass