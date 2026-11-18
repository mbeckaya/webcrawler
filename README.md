# Webcrawler

**Status: 🛠️ In Progress**

Python CLI to crawl websites, follow internal links, extract structured data, and store results in a SQLite database.

## Overview

Webcrawler is a Python-based command-line application designed to automatically explore websites and collect structured data.

The crawler starts with a URL provided by the user and follows internal links up to a predefined crawl depth. It is designed to process multiple pages concurrently while keeping track of visited URLs and crawl progress.

## Planned Technologies

- **Python** – Core application
- **asyncio** – Asynchronous execution and concurrent page fetching
- **SQLite** – Persistent storage for crawl jobs, URLs, and extracted data

## Project Goals

- Build a modular and maintainable web crawler.
- Explore websites by following internal links.
- Implement asynchronous page fetching.
- Prevent duplicate URL processing.
- Store crawl results persistently.
- Extract structured information from web pages.

## Current Status

The project is currently in the planning and development phase. The architecture and core components are being defined before implementation.

More details and functionality will be added as development progresses.

## Technologies

Python, asyncio, SQLite, and pytest.