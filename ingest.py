# ingest.py
import os
import json
from pathlib import Path

def clean_text(text):
    return " ".join(text.split())

def main():
    data_dir = Path("data")
    output_file = "processed_data.json"
    kb = []

    for file_path in data_dir.glob("*"):
        # 支援 txt, pdf, pptx (這裡先以 txt 示範)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        kb.append({
            "source": file_path.name,
            "content": clean_text(content)
        })
        print(f"✅ 已處理: {file_path.name}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(kb, f, indent=4, ensure_ascii=False)
    print(f"🎉 結構化 JSON 已生成: {output_file}")

if __name__ == "__main__":
    main()