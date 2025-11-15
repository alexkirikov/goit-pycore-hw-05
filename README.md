# goit-pycore-hw-05# README 

# task1.py — Caching Fibonacci Numbers (Closure)

**Description:**  
Implements the function `caching_fibonacci()` which creates a closure with an internal cache and returns a recursive `fibonacci(n)` function.  
The function caches previously calculated Fibonacci numbers, significantly improving performance.

---

# task2.py — Number Generator in Text + Total Sum Calculation

**Description:**  
Implements the following functions:

- `generator_numbers(text)` — returns a generator that yields all numeric values found in the text  
- `sum_profit(text, func)` — calculates the total sum of all numbers returned by the generator  

Regular expressions and `yield` are used.

---

# task3.py — Log File Analysis

**Description:**  
A CLI script that reads a log file (`data/logfile.log`) and:

- parses each log entry  
- counts INFO, ERROR, DEBUG, WARNING entries  
- allows filtering logs by level  
- prints statistics in a table format  

Run commands:

```
python task3.py data/logfile.log
python task3.py data/logfile.log error
```

---

# Test Log File (`data/logfile.log`)

```
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
```

Expected statistics:

| Level   | Count |
|---------|-------|
| INFO    | 4     |
| DEBUG   | 3     |
| ERROR   | 2     |
| WARNING | 1     |

---

# Tests for task3.py

## Test 1 — Run Without Arguments

```
python task3.py
```

Expected:

```
Usage: python task3.py <logfile> [level]
```

---

## Test 2 — File Not Found

```
python task3.py data/notfound.log
```

Expected:

```
File not found: data/notfound.log
```

---

## Test 3 — Basic Execution

```
python task3.py data/logfile.log
```

Expected output:

```
Logging Level     | Count
------------------|-------
INFO              | 4
DEBUG             | 3
ERROR             | 2
WARNING           | 1
```

---

## Test 4 — ERROR Level Filtering

```
python task3.py data/logfile.log error
```

Expected:

```
Details for logs with level 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

---

## Test 5 — DEBUG Level Filtering

```
python task3.py data/logfile.log debug
```

Expected:

```
Details for logs with level 'DEBUG':
2024-01-22 08:45:23 - Attempting to connect to the database.
2024-01-22 11:05:00 - Starting data backup process.
2024-01-22 12:45:05 - Checking system health.
```

---

## Test 6 — WARNING Level Filtering

```
python task3.py data/logfile.log warning
```

Expected:

```
Details for logs with level 'WARNING':
2024-01-22 10:30:55 - Disk usage above 80%.
```

---

## Test 7 — Invalid/Corrupted Log Lines

Add this line to the end of `logfile.log`:

```
Broken line without structure
```

Run:

```
python task3.py data/logfile.log
```

Expected:

- script does not crash  
- corrupted line is skipped  
- statistics remain unchanged  

---

# Task 4: assistant/assistant.py 

**Description:**  
The assistant bot now uses a unified `input_error` decorator to handle
all user input mistakes without stopping the program.\
The decorator catches:

-   **KeyError** → returns `"Contact not found."`
-   **ValueError** → returns `"Give me name and phone please."`
-   **IndexError** → returns `"Enter the argument for the command."`

All command handler functions (`add`, `change`, `phone`, `all`) are
wrapped with this decorator.\
This ensures stable work of the bot and clear feedback for incorrect
input.

**Example:**

    Enter a command: add
    Enter the argument for the command
    Enter a command: add Bob 12345
    Contact added.
    Enter a command: phone Alice
    Contact not found.
