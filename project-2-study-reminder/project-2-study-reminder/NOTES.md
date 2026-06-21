🅿️☁️ Project Notes: Auto-Study Reminder


Why I built this

I was nine days out from my AWS AI Practitioner exam and needed something that would hold me accountable. I already knew Lambda could run code on a schedule, so instead of building something generic, I built something I would actually use. That motivation carried me through the parts that did not work on the first try.


What I ran into

The weekend problem

During testing I ran the function, got a clean "Executing function: succeeded" response, and never received an email. No errors, no failures, just nothing in my inbox.

I went back through everything: confirmed my SNS subscription was active, double-checked my environment variable, reviewed the IAM permissions. Everything looked correct.

The function was working exactly as designed. I was testing on a Sunday, and the code has a weekend check that exits early without sending anything. The function succeeded, it just had nothing to do.

The fix was temporarily commenting out the weekend check to force a send during testing, confirming the email landed, then restoring the original logic before setting up the EventBridge schedule. It was a small thing, but it taught me to think about when my code runs, not just whether it runs.

Reading CloudWatch logs

When the email did not arrive I went to CloudWatch to look at the execution logs. There was no error, which turned out to be the clue. If SNS had failed, there would have been an exception in the logs. The clean log with no publish call confirmed the function was exiting before it even tried to send. That was my first hands-on experience using CloudWatch as a debugging tool rather than just a monitoring checkbox.


Decisions I made

Environment variable for the SNS ARN: I kept the Topic ARN out of the code and stored it as a Lambda environment variable. Hardcoding resource identifiers into function code is a bad practice in any real environment, and I wanted to build that habit from the start.

5 AM ET schedule: I set the EventBridge cron to cron(0 9 ? * MON-FRI *), which is 9:00 AM UTC and translates to 5:00 AM Eastern Daylight Time. AWS cron always runs in UTC, so working through the timezone offset was a necessary step I had not thought about going in.

Domain-based rotation: Rather than sending the same generic message every day, I mapped each weekday to a specific AIF-C01 exam domain weighted by how much it appears on the test. Wednesday covers Domain 3 (Foundation Models) because it carries 28% of the scored content. That was a deliberate choice, not a default.


What I would do differently

I attached AmazonSNSFullAccess to get the project running, but that gives Lambda more permissions than it actually needs. In a production environment the right approach would be a custom policy scoped specifically to publish on this one SNS topic ARN. I prioritized getting it working first and would lock it down before anything went to production.

I would also add error handling around the SNS publish call so failures surface clearly in CloudWatch rather than failing silently.


What this project taught me

Going into this I understood Lambda conceptually. Coming out of it I understand how the pieces actually connect: how EventBridge hands off to Lambda, how Lambda needs explicit IAM permission to touch any other service, and how SNS sits in the middle as a delivery layer that is completely separate from the function itself. Troubleshooting the weekend issue is what made that click, because I had to trace the execution path end to end to figure out where it stopped.


Built by Imani Price | Philadelphia, PA | 🅿️☁️ Cloud in progress
