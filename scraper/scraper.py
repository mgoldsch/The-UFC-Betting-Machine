import subprocess

print("upcoming scrape started")

upcoming = subprocess.run(["scrapy", "crawl", "upcoming"])

print("upcoming scrape complete")


print("ufcFights scrape started")

fight_info = subprocess.run(["scrapy", "crawl", "ufcFights"])

print("ufcFights scrape complete")
