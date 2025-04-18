import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from utils.ph_utils import fetch_product_hunt_data
from utils.markdown_utils import generate_markdown_file

# Load environment variables
load_dotenv()

def main():

    # Validate environment variables
    ph_api_key = os.getenv('PH_API_KEY')
    ph_api_secret = os.getenv('PH_API_SECRET')
    if not ph_api_key or not ph_api_secret:
        raise ValueError("Error: PH_API_KEY or PH_API_SECRET environment variable not set. Please set these values in GitHub Actions secrets.")

    num = int(os.getenv('NUM')) if os.getenv('NUM') else 10
    language = os.getenv('LANGUAGE') if os.getenv('LANGUAGE') else 'en'
    print(f"Language: {language}")

    # Record start time
    start_time = datetime.now()
    print(f"Start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    date_str = yesterday.strftime('%Y-%m-%d')
    print(f"Generating hot list data for {date_str}")

    

    languages = language.split(',')

    for language in languages:
        print(f"Fetching Product Hunt data... Language: {language}, Number of products: {num}")
        start = datetime.now()

        # Fetch Product Hunt data
        products = fetch_product_hunt_data(
            num,
            language,
            ph_api_key,
            ph_api_secret
        )

        # Generate Markdown file
        print(f"Fetched {language} data, generating Markdown file...")
        generate_markdown_file(products, language)


        end = datetime.now()
        print(f"Generated {language} Markdown, time taken: {(end - start).total_seconds():.2f} seconds")


    end_time = datetime.now()
    print(f"End time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total time: {(end_time - start_time).total_seconds():.2f} seconds")

if __name__ == "__main__":
    main()