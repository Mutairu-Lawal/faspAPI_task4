import json
import os
from formatter import format_resume

OUTPUT_DIR = "output"

# FILE = os.path.("C:/Users/USER/Desktop/FastAPI/kc_Task5/resume.json")

# print(FILE)


def load_data(file="resume.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except Exception as e:
        print("❌ Failed to load resume data:", e)
        return None


def save_resume(data, format="txt"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    content = format_resume(data, format)
    with open(f"{OUTPUT_DIR}/resume.{format}", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Resume saved as output/resume.{format}")


def main():
    data = load_data()
    if data:
        save_resume(data, "txt")
        save_resume(data, "md")


if __name__ == "__main__":
    main()
