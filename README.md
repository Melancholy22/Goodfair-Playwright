# Goodfair Playwright Scraper

## Description

A small playwright script targeted specifically at goodfair.com (Shopify Website) to:

- Open login page, pre-fill credentials, and pause so user can solve hCaptcha and click submit manually
    * Note that there is some user input due my inability to find a workaround for captcha
- Run a search to find a specific targeted item and extract its price

## Table of Contents (Optional)

If your README is long, add a table of contents to make it easy for users to find what they need.

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Installation

Requirements:
- Python 3.10+
- Playwright (Python)

Run these on your terminal:
pip install playwright
playwright install

## Usage

To run just paste this into your terminal:
python PriceFinder.py
