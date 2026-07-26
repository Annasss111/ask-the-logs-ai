# test_read.py
file_path = "data/log-aex.anonymized.log"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for i in range(15):  # Na9raw 15 line barka
            line = f.readline()
            if not line:
                break
            print(f"Line {i+1}: {line.strip()}")
except Exception as e:
    print(f"Error: {e}")