# Product Hunt Daily Hot Bot

![License](https://img.shields.io/github/license/iAmCorey/producthunt-daily-bot) ![Python](https://img.shields.io/badge/python-3.x-blue)

## Project Introduction

Product Hunt Daily Hot Bot is an automation tool based on GitHub Actions. It can automatically generate a Markdown file of the hottest products on Product Hunt every day and submit it to the GitHub repository. The project aims to help users quickly view the daily Product Hunt hot list and provide more detailed product information.

## Features Overview

- **Automatic Data Fetching**: Automatically fetches the previous day's Product Hunt daily hot products.
- **Keyword Generation**: Generates concise and easy-to-understand keywords to help users better understand product content.
- **High-Quality Translation**: Uses OpenAI's GPT-4 model for high-quality translation of product descriptions.
- **Markdown File Generation**: Generates Markdown files containing product data, keywords, and translated descriptions for easy publishing on websites or other platforms.
- **Daily Automation**: Automatically generates and submits daily Markdown files via GitHub Actions.
- **Configurable Workflow**: Supports manual triggering or scheduled content generation via GitHub Actions.
- **Flexible Customization**: Scripts are easy to extend or modify, allowing for additional product details or file format adjustments.
- **Multi-language Support**: Handles multiple languages by simply modifying the language in environment variables.

## Quick Start

### Prerequisites

- Python 3.x
- GitHub account and repository
- OpenAI API Key
- Product Hunt API credentials

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/ViggoZ/producthunt-daily-hot.git
cd producthunt-daily-hot
```

2. **Install Python dependencies:**

Make sure your system has Python 3.x installed. Then install the required dependencies:

```bash
pip install -r requirements.txt
```

### Setup

1. **GitHub Secrets:**

   Add the following secrets to your GitHub repository:
   Path: Github repository -> Settings -> Secrets and variables -> Actions -> New repository secret

   - `OPENAI_BASE_URL`: Your OpenAI API base URL (e.g., openrouter).
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `PH_API_KEY`: Your Product Hunt API client ID.
   - `PH_API_SECRET`: Your Product Hunt API client secret.
   - `PAT`: Personal access token for pushing changes to the repository.
   - `LANGUAGE`: Language, e.g., `en`. Multiple languages separated by commas, e.g., `en,zh`.
   - `NUM`: Number of products to fetch, default is `10`.

2. **GitHub Actions Workflow:**

   The workflow is defined in `.github/workflows/generate.yml`.
   Workflow schedule: Standard time: every day at 8:01 UTC (16:01 Beijing time); Daylight saving time: every day at 7:01 UTC (15:01 Beijing time). It can also be triggered manually.

### Usage

After setup, GitHub Action will automatically generate and submit a Markdown file containing the daily hot products from Product Hunt. Files are stored in the `data/` directory.

### Customization

#### Code Structure

```
.
├── .github
│   └── workflows
│       └── generate.yml
├── data
│   └── language
│       └── producthunt-daily-YYYY-MM-DD.md
├── README.md
├── requirements.txt
└── scripts
│   └── main.py (main entry)
│   └── utils
│       └── ph_utils.py: Product Hunt utility for data fetching
│       └── markdown_utils.py: Markdown utility for file generation
│       └── common_utils.py: Common utilities
│       └── llm_utils.py: LLM utility for keyword generation and translation
│       └── web_utils.py: Web utility for fetching og images, parsing HTML, etc.
```

- You can refer to the above code structure to add or modify features as needed.
- If needed, you can adjust the scheduled task time in `.github/workflows/generate.yml`.

### Example Output

Generated files are stored in the `data/language` directory. Each file is named in the format `producthunt-daily-YYYY-MM-DD.md`.

### Notes

How to get PAT: Top right avatar -> Settings -> Developer settings -> Personal access tokens -> Generate new token

Make sure PAT has all workflow and repo permissions.

Also, in repository Settings -> Actions -> General -> Read and write permissions must be enabled.

### Acknowledgements

This project is modified from [ph-daily-hot](https://github.com/ViggoZ/producthunt-daily-hot)

### Contribution

Any form of contribution is welcome! If you have any suggestions for improvements or new features, please submit an issue or pull request.

### License

This project is open-sourced under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# My Open Source Domain Story: A Brand, Product, and Growth Journey from a "Non-Programmer" E-commerce Operator

Hi, I'm Charlie.

To be honest, I'm not a programmer. I don't know products, traffic, operations, marketing, or branding. My main job is Amazon e-commerce operations, as a third-party seller. I'm an outsider to the Internet, code, products, and brands. I grew up in an ordinary family and didn't touch a computer until college. At that time, I was curious about Python and programming, but the theory was too boring, and I couldn't get into video courses. Even now, five years after graduation, I still can't code, but I've always had respect and gratitude for "code."

---

## Why this open source project?

Honestly, I didn't understand open source, branding, copyright, traffic, or products at first. I was just an e-commerce operator, doing business under platform rules, feeling it was getting harder, and wanting to find a new way out. One day, I discovered Product Hunt, with so many new products, ideas, and trends every day. I was curious about the data, innovations, and logic behind these products. So I started researching, even "borrowing" the brand, bought a .ai domain, just because it sounded good, and put up an open source navigation project. The data wasn't much different from others. Later, I found that even with little traffic, Google indexed it. This made me realize that even a small attempt can be seen by the world.

But I wasn't satisfied with "copy-paste." I wanted to create something of my own. So I started thinking: can I use this domain to make an open source project that aggregates product data, APIs, and registration info, maybe even a "dashboard" for more people to use and see?

---

## Brand, Copyright, and Risk: My "Late Realization" and Respect

Frankly, I had no concept of brand, copyright, or domain risk at first. I just thought the brand was cool, the domain was handy, so I bought it. I didn't check trademarks or have brand awareness, just thought it was fun. Later, I realized there are risks, especially with well-known brands.

I used this brand's app data and products, indeed "borrowed" some brand heat, but had no malicious intent. I just wanted to do something interesting in my own way and study the data and trends of these innovative products.

Now I respect brands and copyrights very much, and I'm willing to make all project content public, with no commercial purpose or malice. **This article is to clearly express my respect for the brand, domain, and website. All my project content is open and transparent, with no malice or commercial purpose.** If the brand owner ever wants the domain back, I'll transfer it to them. After all, it's their brand, and I'm just a "dreamer passing by." But before that, I hope to use this domain to create something valuable, even if it's just an open source sample room.

---

## My Growth and Identity: Facing My "Ignorance" Honestly

I'm not a product manager, programmer, traffic expert, marketing guru, or brand specialist. I'm just an ordinary e-commerce operator, relying on understanding rules and a bit of execution on Amazon. I'm interested in code but never learned it. I'm interested in products but never made one. I don't understand branding, traffic, marketing, or copyright. But I believe that as long as you're willing to try, learn, and experiment, even "cross-industry," you can create something interesting.

---

## Open Source, Donation, and Personal Brand: My Little Plan

I always felt the greatest charm of open source is not the code itself, but the connection between people. I hope to meet more like-minded friends through this project, even if it's just remote communication, it's a gain.

If one day this project gets some attention, I'll proactively contact the brand owner and express my willingness to donate. Not to "sell for a good price," but to tell a story of "open source, sharing, and win-win." Maybe they won't care, maybe they'll think I'm overdoing it, but that's okay. The important thing is I did what I wanted and left myself a memorable experience.

---

## Operation and Strategy: My Pragmatism

1. **Focus on content and technology**: Regardless of whether the domain can be sold, the project itself must be valuable.
2. **Improve documentation and story**: Write my intentions, story, and donation willingness clearly in the README, project homepage, and blog.
3. **Develop several related projects**: Form my own "open source product matrix" to enhance personal influence.
4. **Fixed contact information**: Use a dedicated email and Twitter account for easy contact with brand owners and developers.
5. **Don't worry or stress**: Decide whether to renew or give up the domain when it expires, go with the flow.
6. **If the brand owner wants the domain, I'll transfer it and write a good story, positive marketing.**  But more importantly, this article is to express my respect for the brand and cherish the domain—**I'm not using this domain for big business, but to leave something interesting for the brand, the industry, and myself through this project.**  If the brand owner needs it, I can transfer the domain to them at any time; if not, I'll keep renewing and maintaining the project until one day it's really valuable and worth attention.
7. **If the account is banned, it means I did something wrong, adjust in time, never violate the rules.**
8. **If no one cares about the project, treat it as practice and slowly build influence.**
9. **If all goes well, keep going and enjoy the fun of open source.**

---

## My Bottom Line and Dedication

- All content of this project is public, with no malice or commercial purpose.
- I'm always willing to donate the domain to the brand owner, even if they don't care now, they can contact me anytime in the future.
- I wrote this article to clarify my thoughts, story, bottom line, respect, and dedication.
- I believe the most valuable thing in life is the products and stories you leave behind.
- **My biggest motivation for this project is to make more products. For me, the greatest meaning in life is to turn my ideas into good products. Even a small open source project is worth taking seriously.**

---

## Conclusion: Be Yourself, Do Open Source with Warmth

I'm not a big shot or an influencer, just an ordinary person who likes to tinker. But I believe that as long as you do things with heart, even a small open source project can shine. I hope my story can inspire you, and you're welcome to communicate, complain, or collaborate.

**Open source is not just code, but the warmth between people.**

---

**Contact:**  
- Email: [hi@producthunt.ai]  

---

If you find my project interesting, feel free to Star, Fork, or open an Issue. Brand owners are also welcome to contact me anytime. If you have a similar story, feel free to share it, let's do something interesting together!

---

> This is my open source domain story, and also my thoughts on products, brands, and the future.  
> What about you? What's your story? 
