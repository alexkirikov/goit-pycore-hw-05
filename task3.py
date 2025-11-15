import sys

# -----------------------------
# 1. Парсинг одного рядка лога
# -----------------------------
def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None  # некоректний рядок
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }


# -----------------------------
# 2. Завантаження всього файлу
# -----------------------------
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return logs


# -----------------------------
# 3. Фільтрація за рівнем
# -----------------------------
def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return list(filter(lambda log: log["level"] == level, logs))


# -----------------------------
# 4. Підрахунок логів за рівнями
# -----------------------------
def count_logs_by_level(logs: list) -> dict:
    levels = ["INFO", "ERROR", "DEBUG", "WARNING"]
    return {lvl: sum(1 for log in logs if log["level"] == lvl) for lvl in levels}


# -----------------------------
# 5. Виведення таблиці
# -----------------------------
def display_log_counts(counts: dict):
    print("Log Level       | Count")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


# -----------------------------
# 6. Основна логіка CLI
# -----------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile> [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if filter_level:
        level_logs = filter_logs_by_level(logs, filter_level)
        print(f"\nLog details for level '{filter_level.upper()}':")
        for entry in level_logs:
            print(f"{entry['date']} {entry['time']} - {entry['message']}")


# ======== Тести ========
# опис тест-кейсів в readme.md
#