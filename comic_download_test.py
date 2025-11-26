import mokkari
import requests
import sys
import random
from pathlib import Path

# Your own config file to keep your credentials secret
from config import username, password

# Get search term from command line or use default
search_term = sys.argv[1] if len(sys.argv) > 1 else "batman"

# Initialize API
m = mokkari.api(username, password)

# Search for comics by series name
print(f"Searching for comics matching: {search_term}")
results = m.issues_list({"series_name": search_term})

# Display results
print(f"\nFound {len(results)} results:")
for idx, issue in enumerate(results, 1):
    print(f"{idx}. {issue.issue_name} (ID: {issue.id})")

# If results found, download a random cover
if results:
    random_issue = random.choice(results)
    print(f"\nFetching details for: {random_issue.issue_name}")

    # Get full issue details
    issue_detail = m.issue(random_issue.id)

    # Try to get the cover image URL
    # Common attributes: image, cover, cover_image, image_url, etc.
    cover_url = None
    for attr in ['image', 'cover', 'cover_image', 'cover_url', 'image_url']:
        if hasattr(issue_detail, attr):
            cover_url = getattr(issue_detail, attr)
            if cover_url:
                print(f"Found cover URL in '{attr}' attribute: {cover_url}")
                break

    if cover_url:
        # Download the cover image
        try:
            response = requests.get(cover_url)
            response.raise_for_status()

            # Create filename from issue name
            filename = f"{search_term}_{random_issue.id}_cover.jpg"
            filepath = Path(filename)

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"\nCover image downloaded successfully: {filepath}")
        except Exception as e:
            print(f"\nError downloading cover: {e}")
    else:
        print("\nNo cover image URL found. Available attributes:")
        # Print all available attributes for debugging
        for attr in dir(issue_detail):
            if not attr.startswith('_'):
                print(f"  - {attr}: {getattr(issue_detail, attr, 'N/A')}")
else:
    print(f"\nNo results found for '{search_term}'")