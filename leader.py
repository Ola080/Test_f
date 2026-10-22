from datetime import datetime, timedelta
def initleaderboard() -> list[str, timedelta]:
    leaderboard = []
    return leaderboard

def add_player(leaderboard, player_name):
    if player_name not in leaderboard:
        return True
    else:
        return False

def add_run(leaderboard, player_name, time):
    if time < 0 :
        return 1
    elif player_name not in leaderboard:
        return 2
    else:
        oldtime = leaderboard[player_name]
        if oldtime == None or oldtime > time:
            leaderboard[player_name] = time
            return 0

def clear_score(leaderboard, player_name):
    if player_name in leaderboard:
        leaderboard[player_name] = None
        return True
    else:
        return False


def display_leaderboard(leaderboard: dict[str, timedelta | None], n: int = 3) -> None:

    times = {name: t for name, t in leaderboard.items() if t is not None}

    if not times:
        print("Leaderboard is empty")
        return

    ranked = sorted(times.items(), key=lambda item: item[1])

    print("Rank\tName\tTime")
    for rank, (name, t) in enumerate(ranked[:n], start=1):
        print(f"{rank}\t{name}\t{t.strftime('%H:%M:%S')}")

def calculate_averahe_time (leaderboard: dict[str,timedelta | None]) -> dict[bool, timedelta | None]:
    times = [t for t in leaderboard.values() if t is not None]
    if times == []:
        return (False, None)
    average_time = sum(times, timedelta()) / len(times)
    return (True, average_time)