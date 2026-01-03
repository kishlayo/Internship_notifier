import feedparser

SEEN_FILE = "seen_link.txt"
RESULT_FILE = "result.txt"

def load_seen_links():
    try:
        with open(SEEN_FILE, "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def save_seen_links(seen_links):
    with open(SEEN_FILE, "w") as f:
        for link in seen_links:
            f.write(link + "\n")

def scan(keywords, locations):
    url = "https://hnrss.org/jobs"
    feed = feedparser.parse(url)

    seen_links = load_seen_links()
    new_links = set()
    found = False
    
    open(RESULT_FILE, "w").close()

    with open(RESULT_FILE, "a") as r:
        for entry in feed.entries:
            title = entry.title.lower()

            key_match = any(word in title for word in keywords)
            loc_match = any(loc in title for loc in locations)

            if key_match and loc_match:
                if entry.link not in seen_links:
                    found = True
                    r.write(entry.title + "\n")
                    r.write(entry.link + "\n")
                    new_links.add(entry.link)

    save_seen_links(seen_links.union(new_links))
    return found


print("HELLO THERE! LET'S FIND A JOB FOR YOU")

keywords = []
locations = []

print("ENTER KEYWORDS (press ENTER to finish):")
while True:
    key = input().strip().lower()
    if key == "":
        break
    keywords.append(key)

print("ENTER LOCATIONS (press ENTER to finish):")
while True:
    loc = input().strip().lower()
    if loc == "":
        break
    locations.append(loc)

if scan(keywords, locations):
    print("HERE ARE THE RESULTS I FOUND:")
    with open(RESULT_FILE, "r") as r:
        lines = r.readlines()
        count = 0
        for i in range(0, len(lines) - 1, 2):
            title = lines[i].strip()
            link = lines[i + 1].strip()

            if title and link:
                print("TITLE:", title)
                print("LINK:", link)
                print("----------------------------------")
                count += 1

        print("Total matches found:", count)

else:
    print("NO NEW MATCH FOUND")
