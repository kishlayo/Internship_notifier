from datetime import date, datetime, timezone, timedelta
import feedparser

def scan(keywords,location):
    url = "https://hnrss.org/jobs"
    feed = feedparser.parse(url)
    flag = False
    links = []
    with open("result.txt","a") as r:
        
        for entry in feed.entries:
            title = entry.title.lower()
            if any(word in title for word in keywords and location):
                flag = True
                if(entry.link not in links):
                    r.write(f"{entry.title}\n")
                    r.write(f"{entry.link}\n")
                    links.append(entry.link)
                   
    return flag

print("HELLO THERE! LET'S A JOB FOR YOU")
keywords = []
location = []
print("ENTER THE KEYWORDS YOU ARE LOOKING FOR...(WHEN YOU ARE DONE JUST ENTER A SPACE)")

while True:
    key = input().strip().lower()
    if key == "" or key == " ":
        break
    else:
        keywords.append(key)

print("ENTER THE LOCATION IN WHICH YOU ARE LOOKING...(WHEN YOU ARE DONE JUST ENTER A SPACE)")

while True:
    key = input().strip().lower()
    if key == "" or key == " ":
        break
    else:
        location.append(key)
        
if(scan(keywords,location)):
    print("HERE ARE THE RESULT I FOUND......")
    with open("result.txt", "r") as r:
        while True:
            title = r.readline()
            link = r.readline()

            if not title or not link:
                break

            print("TITLE:", title.strip())
            print("LINK:", link.strip())
            print("----------------------------------")

        
else:
    print("NO MATCH FOUND")
    print("---------------------------------------------")