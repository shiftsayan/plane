import secrets

class PlaneProfileBase():

    def __init__(self):
        self.api_key = secrets.api_key
        self.domain = secrets.domain
        self.sender = secrets.sender
        self.reply_to = secrets.reply_to
        self.recepients = []
        
        
class PlaneProfile(PlaneProfileBase):

    def __init__(self, id, recepients):
        super().__init__()
        self.id = id
        self.recepients.extend(recepients)


profiles = [
    PlaneProfile('general', secrets.recepients_general),
    PlaneProfile('testing', secrets.recepients_testing),
    PlaneProfile('tech', secrets.recepients_tech),
]