import subprocess

print("starting ratings generation")
ratings = subprocess.run(["Rscript", "glicko_rating_generation.R"])
print("ratings generation complete")