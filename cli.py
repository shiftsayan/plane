from PyInquirer import prompt

from schema import schema
from profiles import profiles

def prompt_category():
    questions = [
        {
            'type': 'list',
            'name': 'category',
            'message': 'What category of email do you want to send?',
            'choices': schema.keys()
        }
    ]
    answers = prompt(questions)
    return answers['category']

def prompt_schema(category):
    if len(schema[category]) == 1:
        return schema[category][0]
    
    questions = [
        {
            'type': 'list',
            'name': 'settings',
            'message': 'What type of email do you want to send?',
            'choices': [ ps.id for ps in schema[category] ],
        }
    ]
    answers = prompt(questions)
    return answers['settings']

def prompt_profile():
    questions = [
        {
            'type': 'list',
            'name': 'profile',
            'message': 'Which profile do you want to use?',
            'choices': [ profile.id for profile in profiles ],
        }
    ]
    answers = prompt(questions)
    
    for profile in profiles:
        if profile.id == answers['profile']:
            return profile