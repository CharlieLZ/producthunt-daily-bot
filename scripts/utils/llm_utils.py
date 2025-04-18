import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY')
)

def generate_ai_keywords(name: str, tagline: str, description: str, language: str) -> str:
    """
    Generate keywords using AI
    
    Args:
        name: product name
        tagline: product tagline
        description: product description
    
    Returns:
        str: generated keywords string, separated by commas
    """
    prompt = f"Generate suitable {language} keywords based on the following content, separated by English commas:\n\nProduct Name: {name}\n\nTagline: {tagline}\n\nDescription: {description}"
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Generate suitable keywords in language {language} based on the product information provided. The keywords should be separated by commas and in the language {language}."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=50,
            temperature=0.7,
        )
        keywords = response.choices[0].message.content.strip()
        if ',' not in keywords:
            keywords = ', '.join(keywords.split())
        return keywords
    except Exception as e:
        print(f"Error occurred during keyword generation: {e}")
        return "No keywords"

def translate_with_ai(text: str, language: str) -> str:
    """
    Translate text using AI
    
    Args:
        text: text to be translated
        language: language: en/zh
    Returns:
        str: translated text
    """
    try:
        response = client.chat.completions.create(
            extra_headers={
                #  Site url for including your app on openrouter.ai rankings.
                "HTTP-Referer": "https://aibest.tools",
                #  Site name shows in rankings on openrouter.ai.
                "X-Title": "AI Best Tools",
            },
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are the world's most professional translation tool, proficient in multiple languages. You are a professional translator fluent in {language}, especially good at translating IT jargon and technical terms into concise and idiomatic expressions. Your task is to translate the following content into idiomatic {language}, in a style similar to popular science magazines or daily conversation."},
                {"role": "user", "content": text},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error occurred during translation: {e}")
        return text