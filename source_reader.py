import os

def get_sources():

    current_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(current_dir, "sources.txt")

    with open(file_path, "r", encoding="utf-8") as file:

        sources = [
            line.strip()
            for line in file
            if line.strip()
        ]

    return sources