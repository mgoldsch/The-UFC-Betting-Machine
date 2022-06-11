import subprocess

print("starting predictions")
ratings = subprocess.run(["Rscript", "glicko_fight_prediction.R"])
print("predictions complete")