#! /usr/bin/env python3
from cli import prompt_category, prompt_schema, prompt_profile
from send import PlaneSendTemplate, PlaneSendReminder

def plane():
    profile = prompt_profile()

    category = prompt_category()
    schema = prompt_schema(category)

    if category == 'template':
        PlaneSendTemplate(schema, profile).execute()
    elif category == 'reminder':
        pass
    elif category == 'longform':
        pass

if __name__ == "__main__":
    plane()