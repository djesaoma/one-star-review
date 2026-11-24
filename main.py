import os

os.makedirs("/output", exist_ok=True)
review = "gravity: dependable for decades, then one bad step and it holds me down while the stairs finish the job."
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(review)
