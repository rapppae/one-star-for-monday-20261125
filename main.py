"""Entry for make.fun bounty: One Star for Monday
Slug: u-clever-harbor-75-one-star-for-monday-9ead4a61
Entry text (122 characters, 24 words (limit 25 words), gate max 180). Written to /output/entry.txt with no trailing newline.
"""
import os

ENTRY = """One star. The coffee was cold, the Wi-Fi was down, and the manager — Monday itself — smiled and said, 'Same time next week.'"""

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
