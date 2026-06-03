# This file is a part of WayneBots (github.com/irisXDR/WayneBots)

def get_version() -> str:
    MAJOR = "1"
    MINOR = "0"
    PATCH = "4"
    return f"v{MAJOR}.{MINOR}.{PATCH}"

if __name__ == "__main__":
    print(get_version())
