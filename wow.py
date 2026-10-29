import csv

def find_common(file1: str, file2: str) -> list[str]:
    commonlist = []
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = {line.strip() for line in f1}
            lines2 = {line.strip() for line in f2}
            commonlist = list(set(lines1) & set(lines2))
    except FileNotFoundError:
        raise ValueError(f"One or both files not found: {file1}, {file2}")
    return commonlist

def uniq(f1:str, f2:str) -> int:
    linecount = 0
    previous = None
    try:
        with open(f1, 'r') as src, open(f2, 'w') as dest:
            for line in src:
                if line != previous:
                    dest.write(line)
                    linecount = linecount + 1
                previous = line
    except OSError as e:
        raise ValueError(f"Error processing files: {f1}, {f2}") from e
    return linecount


def calculate_running_total(src: str, dest: str) -> int:

    try:
        with open(src, 'r', newline='') as file:
            reader = csv.reader(file)
            og = [row for row in reader]

        with open(dest, 'w', newline='') as file:
            writer = csv.writer(file)
            total = 0
            writer.writerow(og[0] + ["Running Total"])
            for row in og[1:]:
                total = total + int(row[-1])
                writer.writerow(row + [total])

    except (OSError, csv.Error, IndexError, ValueError) as e:
        raise ValueError(f"Error processing files: {src}, {dest}") from e

    return total

def