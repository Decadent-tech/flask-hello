import sqlite3

# Open the database connection
conn = sqlite3.connect("submissions.db")
cursor = conn.cursor()

# Read and insert from submissions.txt
with open("submissions.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        # Try both possible separators
        if " - " in line:
            timestamp, name = line.split(" - ", 1)
        else:
            # fallback for double space separator
            parts = line.split("  ", 1)
            if len(parts) == 2:
                timestamp, name = parts
            else:
                continue  # skip malformed lines
        # Check if this entry already exists
        cursor.execute("SELECT COUNT(*) FROM submissions WHERE timestamp=? AND name=?", (timestamp.strip(), name.strip()))
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO submissions (timestamp, name) VALUES (?, ?)", (timestamp.strip(), name.strip()))

conn.commit()
conn.close()

print("Import complete.")
