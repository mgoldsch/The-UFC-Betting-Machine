import subprocess

upcoming = subprocess.run(["scrapy", "crawl", "upcoming"])
print("upcoming scrape complete")