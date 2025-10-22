# Goodfair Playwright Scraper

## Description

A small playwright script targeted specifically at goodfair.com (Shopify Website) to:

- Open login page, pre-fill credentials, and pause so user can solve hCaptcha and click submit manually
    * Note that there is some user input due to the hCaptchas
- Run a search to find a specific targeted item and extract its price

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
