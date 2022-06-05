import os

print("cleaner started")

path_upcoming = "/data/upcoming"
path_fight_info = "/data/fight_info"
path_fight_stats = "/data/fight_stats"

def delete_fight_stats():
    os.rmdir(path_fight_stats)

def delete_all_but_recent(path):
    files = os.listdir(path)
    files.sort()
    files_to_delete = files - files[0]
    for f in files_to_delete:
        os.remove(path + "/" + f)

print("deleting fight stats folder")
delete_fight_stats()
print("fight stats folder deleted")

print("deleting fight info old csv")
delete_all_but_recent(path_fight_info)
print("deleted fight info old csv")

print("deleting upcoming old csv")
delete_all_but_recent(path_upcoming)
print("deleted upcoming old csv")

print("cleaner finshed")