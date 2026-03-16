import re
import pandas as pd
import json

def extract_emails(text):
    """
    Extracts email addresses from text using regular expressions.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    # Normalize to lowercase and remove duplicates
    unique_emails = list(set(email.lower() for email in emails))
    return unique_emails

def prioritize_emails(emails):
    """
    Prioritizes general business contact emails.
    """
    priority_keywords = ['info', 'contact', 'hello', 'sales', 'support', 'hi']
    prioritized = []
    others = []

    for email in emails:
        user = email.split('@')[0]
        if any(keyword in user for keyword in priority_keywords):
            prioritized.append(email)
        else:
            others.append(email)

    return prioritized + others

def score_lead(text, industry):
    """
    Scores a lead based on the presence of AI automation keywords and target industry match.
    """
    ai_keywords = [
        'ai automation', 'artificial intelligence', 'machine learning',
        'chatbot', 'llm', 'workflow automation', 'document analysis',
        'predictive analytics', 'natural language processing', 'gpt',
        'openai', 'automation agency', 'intelligent automation'
    ]

    score = 0
    text_lower = text.lower()

    # Check for AI interest/keywords
    for keyword in ai_keywords:
        if keyword in text_lower:
            score += 2

    # Check if they are in the specified target industry
    if industry.lower() in text_lower:
        score += 5  # Stronger weight for a direct industry match

    # Also check for general high-potential industries if not already matched
    potential_industry_keywords = [
        'consulting', 'law firm', 'legal', 'recruitment', 'marketing agency',
        'software', 'saas', 'data management', 'accounting', 'real estate'
    ]
    for keyword in potential_industry_keywords:
        if keyword in text_lower and keyword != industry.lower():
            score += 1

    return score

def save_leads(leads, csv_path='leads.csv', json_path='leads.json'):
    """
    Saves the list of leads to CSV and JSON formats.
    """
    if not leads:
        print("No leads to save.")
        return

    df = pd.DataFrame(leads)

    # Export to CSV
    df.to_csv(csv_path, index=False)

    # Export to JSON
    with open(json_path, 'w') as f:
        json.dump(leads, f, indent=4)

    print(f"Saved {len(leads)} leads to {csv_path} and {json_path}")

def get_company_description(text, max_length=200):
    """
    Extracts a short company description from the website text.
    """
    # Simple approach: take the first few lines or look for 'About Us' section
    lines = [line.strip() for line in text.split('\n') if len(line.strip()) > 50]
    if lines:
        description = lines[0]
        if len(description) > max_length:
            return description[:max_length] + "..."
        return description
    return "No description available."
