# Imani Price 🅿️☁️ AWS Cloud Practitioner Lab

> Building real projects while studying for AWS Cloud Practitioner. Every lab is proof of concept — not just completed, but understood.

**Philadelphia, PA → NYC (2027)**
📅 AWS Exam: **July 1, 2026** | 🎓 CompTIA A+: **July 13 – October 2026** (Montgomery Community College)

---

## About This Repo

I'm Imani — Assistant Director of Postsecondary Partnerships at Mastery Schools, pivoting into cloud and IT infrastructure. I've spent my career at the intersection of systems, data, and people. Now I'm going deeper on the technical side, and I'm documenting the whole thing here.

This isn't a course project repo. It's a portfolio of things I've actually built, broken, and understood.

---

## Certification Roadmap

| Certification | Status | Date |
|---|---|---|
| AWS Cloud Practitioner (CLF-C02) | In Progress | Exam: July 1, 2026 |
| CompTIA A+ | Enrolled | July 13 – October 2026 |
| AWS Solutions Architect – Associate | Planned | 2027 |

---

## Projects

### Project 1: Static Resume Hosted on AWS S3

**Objective:** Deploy a personalized static website on Amazon S3 and keep it live as a portfolio artifact.

**Live site:** http://imani-cloud-resume-2026.s3-website.us-east-2.amazonaws.com

**Services used:**
- Amazon S3 (Static Website Hosting)
- AWS IAM (Bucket Policy)
- AWS Cost Explorer

**What I actually learned:**
- The difference between Block Public Access settings and bucket policies — and why both matter
- How S3 serves static files without a web server running anywhere
- How to write a bucket policy JSON granting `s3:GetObject` to the public
- How to monitor costs with AWS Cost Explorer (this site costs ~$0.00/month)
- Why keeping a bucket live (vs deleting) preserves the link for a portfolio

**Screenshots:**

| S3 Bucket Created | Static Hosting Enabled | Site Live |
|---|---|---|
| ![Bucket List](project-1-cloud-resume/screenshots/bucket%20list.png) | ![Static Hosting](project-1-cloud-resume/screenshots/Static%20Hosting.png) | ![Live Site](project-1-cloud-resume/screenshots/Screenshot%202026-06-16%20224848.png) |

**Cost analysis:**
- S3 storage: ~$0.0005/month
- Data transfer: Free (within same region)
- Keeping it live: intentional — this is a portfolio link

---

### Project 2: Coming Soon

Planning to add a visitor counter using DynamoDB + Lambda, or explore S3 + CloudFront for HTTPS delivery. Will be added after the AWS exam.

---

## How to Recreate Project 1

If you need to re-upload your site files:

### Step 1 — Prepare your files
Download `index.html` from this repo (in `project-1-cloud-resume/`)

### Step 2 — Create or verify your S3 bucket
1. Go to **S3** in the AWS Console
2. If the bucket `imani-cloud-resume-2026` still exists, skip to Step 3
3. If recreating: **Create bucket** → name it `imani-cloud-resume-2026` → region `us-east-2`
4. Uncheck **Block all public access**

### Step 3 — Enable static website hosting
1. Bucket → **Properties** tab → **Static website hosting** → Enable
2. Index document: `index.html` → Save

### Step 4 — Add bucket policy
Permissions tab → Bucket policy → paste:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::imani-cloud-resume-2026/*"
    }
  ]
}
```

### Step 5 — Upload index.html
Objects tab → Upload → select `index.html` → Upload

### Step 6 — Verify
Visit: http://imani-cloud-resume-2026.s3-website.us-east-2.amazonaws.com

---

## Note on Cleanup

Unlike typical lab tutorials, **I am not deleting this bucket** after the project. The live URL is part of the portfolio. AWS S3 static hosting costs essentially nothing for a lightweight personal site (~$0.00–$0.01/month).

---

*This repo is updated as I complete each project. Follow along if you're on a similar path.*
