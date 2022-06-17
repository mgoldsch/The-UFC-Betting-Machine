import os

print("cleaner started")

path_upcoming = "/data/upcoming"
path_fight_info = "/data/fight_info"
path_fight_stats = "/data/fight_stats"

def delete_all_files(path):
    try:    
        files = os.listdir(path)
        for f in files:
            os.remove(path + "/" + f)
    except:
        print("path does not exist")
    try:
        os.rmdir(path)
    except:
        print("directory could not be removed")

def delete_all_but_recent(path):
    files = os.listdir(path)
    files.sort(reverse=True)
    files.pop(0)
    for f in files:
        os.remove(path + "/" + f)

print("deleting fight stats folder")
delete_all_files(path_fight_stats)
print("fight stats folder deleted")

print("deleting fight info old csv")
delete_all_but_recent(path_fight_info)
print("deleted fight info old csv")

print("deleting upcoming old csv")
delete_all_but_recent(path_upcoming)
print("deleted upcoming old csv")

print("cleaner finshed")