# Inky Comics

A Python project to fetch and display random comic book covers on a Pimoroni Inky Impression e-ink display using the Metron Comic Database API.

## Features

- Fetch comic covers from the Metron Comic Database
- Display covers on Inky Impression e-ink displays
- Search for comics by series name
- Automatically rotate portrait-oriented covers to landscape
- Random selection from search results

## Files

### `comic.py`
Main script that fetches a random comic cover and displays it on an Inky Impression display.

**Features:**
- Downloads cover image from Metron API
- Automatically rotates portrait images to landscape
- Resizes image to fit Inky display resolution
- Updates the e-ink display with the cover

**Usage:**
```bash
python comic.py [search_term]
```

**Examples:**
```bash
# Display a random Batman comic cover
python comic.py batman

# Display a random Spider-Man comic cover
python comic.py "spider-man"

# Uses default search term (batman) if none provided
python comic.py
```

### `comic_download_test.py`
Test script that downloads comic covers to disk without requiring an Inky display.

**Features:**
- Downloads cover images as JPG files
- Useful for testing API connectivity
- Debug output showing available attributes

**Usage:**
```bash
python comic_download_test.py [search_term]
```

**Examples:**
```bash
# Download a random Batman cover
python comic_download_test.py batman

# Download a random X-Men cover
python comic_download_test.py "x-men"
```

## Setup

### Prerequisites

- Python 3.7+
- Pimoroni Inky Impression display (for `comic.py` only)
- Metron API account (free at https://metron.cloud/)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/WayneStallwood/inky-comics.git
cd inky-comics
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your Metron API credentials:
```bash
cp config.py.example config.py
```

Edit `config.py` and add your Metron API credentials:
```python
username = "your_username"
password = "your_password"
```

### Getting Metron API Credentials

1. Visit https://metron.cloud/
2. Create a free account
3. Use your username and password in `config.py`

## Hardware Requirements

For `comic.py` (Inky display):
- Raspberry Pi (any model with GPIO)
- Pimoroni Inky Impression e-ink display
- Proper GPIO connection between Pi and display

For `comic_download_test.py`:
- Any computer with Python 3.7+

## How It Works

1. The script connects to the Metron Comic Database API using your credentials
2. Searches for comics matching your search term (e.g., "batman")
3. Randomly selects one comic from the results
4. Downloads the cover image
5. (`comic.py` only) Processes the image:
   - Rotates portrait images to landscape
   - Resizes to match display resolution
   - Updates the Inky display

## Configuration

### Search Terms

You can search for any comic series in the Metron database:
- Single word: `batman`, `superman`, `spawn`
- Multiple words: `"spider-man"`, `"the walking dead"`, `"x-men"`

### Image Processing

`comic.py` automatically:
- Detects portrait vs landscape orientation
- Rotates portrait images 90° clockwise
- Resizes to match your Inky display resolution

## Troubleshooting

### "No module named 'config'"
Make sure you've created `config.py` from `config.py.example` and added your credentials.

### "No results found"
The search term may not match any series in the Metron database. Try variations or check https://metron.cloud/ to verify the series name.

### "No cover image URL found"
Some comics in the database may not have cover images available. Try a different comic or search term.

### Inky display not updating
- Verify GPIO connections
- Check that the `inky` library is properly installed
- Ensure you're running on a Raspberry Pi with GPIO support

## License

MIT License - see LICENSE file for details

## Credits

- Uses the [Mokkari](https://github.com/Metron-Project/mokkari) Python wrapper for the Metron API
- Comic data from [Metron Comic Database](https://metron.cloud/)
- Inky display support from [Pimoroni](https://shop.pimoroni.com/)
