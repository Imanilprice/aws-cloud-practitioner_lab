import boto3
import os
from datetime import date, datetime

sns = boto3.client('sns')

STUDY_TIPS = {
    "Monday": {
        "topic": "AI & ML Fundamentals (Domain 1 — 20%)",
        "tip": "Review the differences between AI, ML, deep learning, and generative AI. Know the ML lifecycle: data collection → training → evaluation → deployment."
    },
    "Tuesday": {
        "topic": "Generative AI Fundamentals (Domain 2 — 24%)",
        "tip": "Focus on foundation models, tokens, embeddings, and how LLMs generate text. Know what makes a prompt effective."
    },
    "Wednesday": {
        "topic": "Applications of Foundation Models (Domain 3 — 28%)",
        "tip": "This is the biggest domain. Review Amazon Bedrock, RAG architecture, prompt engineering techniques (zero-shot, few-shot, chain-of-thought), and when to fine-tune vs. use RAG."
    },
    "Thursday": {
        "topic": "Responsible AI (Domain 4 — 14%)",
        "tip": "Study hallucination, bias, explainability, and fairness. Know AWS's approach to responsible AI and how to evaluate model outputs."
    },
    "Friday": {
        "topic": "Security, Compliance & Governance (Domain 5 — 14%)",
        "tip": "Review IAM roles for AI workloads, the AWS shared responsibility model, and how Amazon Bedrock handles data privacy and compliance."
    }
}

def lambda_handler(event, context):
    today = datetime.utcnow()
    day_name = today.strftime("%A")

    # Only send on weekdays
    if day_name not in STUDY_TIPS:
        return {'statusCode': 200, 'body': 'Weekend — no reminder sent.'}

    focus = STUDY_TIPS[day_name]

    # Countdown to exam
    exam_date = date(2026, 6, 30)
    days_remaining = (exam_date - today.date()).days

    if days_remaining > 0:
        countdown = f"Your AWS AI Practitioner exam is in {days_remaining} day(s) — June 30, 2026."
    elif days_remaining == 0:
        countdown = "TODAY IS EXAM DAY. You've put in the work. Go get it."
    else:
        countdown = "Exam complete! Now prep for AWS Cloud Practitioner — next stop: certified."

    message = f"""
Good morning, Imani! It's time to study. 🅿️☁️

{countdown}

TODAY'S FOCUS: {focus['topic']}
{focus['tip']}

After your session, log into the AWS console and review your hands-on projects.
Every day you show up is a day closer to certified.
Your future self is counting on you.

— Your AWS Study Reminder (built by you, powered by Lambda)
    """.strip()

    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=message,
        Subject=f"AWS Study Reminder | {day_name} | {days_remaining} days to go"
    )

    return {
        'statusCode': 200,
        'body': f'Reminder sent for {day_name}!'
    }
