import os


def find_file(filename):

    home = os.path.expanduser("~")

    matches = []

    for root, dirs, files in os.walk(home):
        for file in files:
            if filename.lower() in file.lower():
                matches.append(
                    os.path.join(root, file)
                )

    return matches


def open_file(path):
    os.system(f'open "{path}"')