from PyInquirer import prompt

from schema import schema

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

def prompt_settings(category):
    if len(schema[category]) == 1:
        return schema[category][0]
    
    questions = [
        {
            'type': 'list',
            'name': 'settings',
            'message': 'What type of email do you want to send?',
            'choices': [ ps.name for ps in schema[category] ],
        }
    ]
    answers = prompt(questions)
    return answers['settings']