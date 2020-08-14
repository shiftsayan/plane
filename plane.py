#! /usr/bin/env python3
from cli import prompt_category, prompt_settings
from secrets import secrets
from send import PlaneSendTemplate, PlaneSendReminder

def plane():
    category = prompt_category()
    settings = prompt_settings(category)

    # PlaneSendTemplate("yoohoo", secrets).send()
    # PlaneSendTemplate("yoohoo", secrets).__send(1, 2, 3)

if __name__ == "__main__":
    plane()