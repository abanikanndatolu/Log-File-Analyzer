import re

# Function to analyze log file
def analyze_logs(log_file):
    suspicious_patterns = [
        r"failed login attempt",
        r"error 404",
        r"unauthorized access",
        r"malware detected",
    ]

    with open(log_file, "r") as file:
        logs = file.readlines()

    flagged_entries = [line for line in logs if any(re.search(pattern, line, re.IGNORECASE) for pattern in suspicious_patterns)]

    return flagged_entries

# Example usage
if __name__ == "__main__":
    log_file_path = input("Enter log file path: ")
    flagged_logs = analyze_logs(log_file_path)

    if flagged_logs:
        print("\nSuspicious Log Entries Found:")
        for entry in flagged_logs:
            print(entry.strip())
    else:
        print("\nNo suspicious activity detected.")
