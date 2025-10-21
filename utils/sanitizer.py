import re

def sanitize_content(text: str) -> str:
    # Emails
    text = re.sub(r'[\w\.-]+(\s*[@|[(at)]\s*)[\w\.-]+', '[removed]', text)
    # Phone numbers
    text = re.sub(r'(\+?\d[\d\s\-\(\)]{7,}\d)', '[removed]', text)
    # URLs (even obfuscated)
    text = re.sub(r'((https?:\/\/|www\.)\S+|[\w\-]+\s*\.\s*[\w\-]+(\s*\.\s*[\w\-]+)*)', '[removed]', text)
    return text
