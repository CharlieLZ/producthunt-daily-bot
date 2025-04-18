from datetime import datetime, timezone
from typing import List
from .common_utils import ensure_directory_exists
from .ph_utils import Product

def generate_markdown_file(products: List[Product], language: str) -> None:
    """
    Generate Markdown content and save to data directory
    
    Args:
        products: list of Product objects
        date_str: date string
        language: language: en/zh
    """
    today = datetime.now(timezone.utc)
    date_today = today.strftime('%Y-%m-%d')

    # Generate markdown content
    markdown_content = generate_markdown_content(products, date_today, language)

    # Save file
    save_markdown_file(markdown_content, date_today, language)

def generate_markdown_content(products: List[Product], date_today: str, language: str) -> str:
    """
    Generate Markdown content
    
    Args:
        products: list of Product objects
        date_today: today's date string
    
    Returns:
        str: generated Markdown content
    """
    if language == 'zh':
        markdown_content = f"# Product Hunt 今日热榜 | {date_today}\n\n"
    else:
        markdown_content = f"# Product Hunt Daily Hot | {date_today}\n\n"
    for rank, product in enumerate(products, 1):
        markdown_content += product.to_markdown(rank, language)
    return markdown_content

def save_markdown_file(content: str, date_today: str, language: str) -> None:
    """
    Save Markdown file to data directory
    
    Args:
        content: Markdown content
        date_today: today's date string
    """
    ensure_directory_exists(f'data/{language}')
    file_name = f"data/{language}/producthunt-daily-{date_today}.md"

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"File {file_name} generated and overwritten successfully.")