

def online_count(dic):
    count = 0
    for x, y in dic.items():
        if y == "online":
            count += 1
    return count


if __name__ == "__main__":
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    nom = online_count(statuses)
