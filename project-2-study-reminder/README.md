# 🅿️☁️ Project 2: Auto-Study Reminder
### AWS Lambda + Amazon SNS + Amazon EventBridge

> A serverless reminder system that sends a personalized weekday morning study message with a rotating daily focus topic and exam countdown — built to support my AWS certification journey.

---

## What It Does

Every weekday at 5:00 AM ET, this function automatically:

- Sends a personalized email reminder to study
- Displays a rotating focus topic mapped to each AIF-C01 exam domain
- Counts down the days remaining to the exam date
- Skips weekends automatically

This project is live and actively sending reminders as I prepare for the **AWS Certified AI Practitioner (AIF-C01)** exam.

---

## Architecture

```
EventBridge (cron schedule — weekdays 5 AM ET)
                    ↓
          AWS Lambda Function
          (StudyReminderFunction)
                    ↓
         Amazon SNS Topic
         (aws-study-reminder)
                    ↓
           Email Delivery
```

---

## Services Used

| Service | Purpose |
|---|---|
| AWS Lambda | Runs the Python function serverlessly — no servers to manage |
| Amazon SNS | Delivers the reminder message via email |
| Amazon EventBridge | Triggers Lambda on a cron schedule every weekday at 5 AM ET |
| AWS IAM | Grants Lambda permission to publish to SNS |

---

## Daily Study Topics

The function rotates through all five AIF-C01 exam domains across the week:

| Day | Domain | Exam Weight |
|---|---|---|
| Monday | Fundamentals of AI and ML | 20% |
| Tuesday | Fundamentals of Generative AI | 24% |
| Wednesday | Applications of Foundation Models | 28% |
| Thursday | Guidelines for Responsible AI | 14% |
| Friday | Security, Compliance & Governance | 14% |

---

## Sample Message

```
Good morning, Imani! It's time to study. 🅿️☁️

Your AWS AI Practitioner exam is in 9 days — June 30, 2026.

TODAY'S FOCUS: Applications of Foundation Models (Domain 3 — 28%)
This is the biggest domain. Review Amazon Bedrock, RAG architecture,
prompt engineering techniques (zero-shot, few-shot, chain-of-thought),
and when to fine-tune vs. use RAG.

After your session, log into the AWS console and review your hands-on projects.
Every day you show up is a day closer to certified.
Your future self is counting on you.

— Your AWS Study Reminder (built by you, powered by Lambda)
```

---

## Project Files

```
project-2-study-reminder/
├── lambda_function.py     # Python function code
├── BUILD_GUIDE.md         # Step-by-step setup instructions
└── README.md              # This file
```

---

## How to Deploy This Yourself

### Prerequisites
- An AWS account (Free Tier is enough)
- An email address to receive reminders

### Steps

**1. Create an SNS Topic**
- Go to SNS → Topics → Create topic
- Type: Standard | Name: `aws-study-reminder`
- Copy the ARN

**2. Subscribe your email**
- Create subscription → Protocol: Email → enter your address
- Confirm the subscription link sent to your inbox

**3. Create the Lambda function**
- Go to Lambda → Create function → Author from scratch
- Name: `StudyReminderFunction` | Runtime: Python 3.12
- Paste `lambda_function.py` code → Deploy

**4. Add environment variable**
- Configuration → Environment variables → Add
- Key: `SNS_TOPIC_ARN` | Value: your SNS ARN from Step 1

**5. Attach IAM policy**
- Configuration → Permissions → click the execution role
- Add permissions → Attach `AmazonSNSFullAccess`

**6. Test it**
- Click Test → create event with `{}` → run
- Check your inbox

**7. Schedule with EventBridge**
- Add trigger → EventBridge → Create new rule
- Schedule expression: `cron(0 9 ? * MON-FRI *)`
  *(9:00 AM UTC = 5:00 AM ET)*

---

## What I Learned

- How to write and deploy a Python Lambda function from scratch
- How SNS pub/sub messaging works and how to confirm subscriptions
- How to use EventBridge cron expressions to schedule automated tasks
- How IAM execution roles control what Lambda is allowed to do
- How environment variables keep sensitive values out of code
- How to read CloudWatch logs to troubleshoot a failed execution

---

## Part of My AWS Certification Journey

This is Project 2 in my hands-on cloud portfolio, built alongside my AWS certification path:

- AWS Certified AI Practitioner (AIF-C01) — June 2026
- AWS Certified Cloud Practitioner — July 2026
- CompTIA A+ — October 2026

View my full portfolio: [github.com/Imanilprice/aws-cloud-practitioner_lab](https://github.com/Imanilprice/aws-cloud-practitioner_lab)

---

*Built by Imani Price | Philadelphia, PA | 🅿️☁️ Cloud in progress*
