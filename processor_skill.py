# processor_skill.py
import json
from pathlib import Path

def run_skill(file_name: str):
    # 模擬 Skill 執行的邏輯
    output_dir = Path("processed_output")
    output_dir.mkdir(exist_ok=True)
    
    # 讀取剛剛 ingest 產生的結果
    with open("processed_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 找尋對應的檔案內容
    result = next((item for item in data if item["source"] == file_name), None)
    
    if result:
        output_path = output_dir / f"{file_name}_structured.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)
        return {"status": "success", "file": str(output_path)}
    return {"status": "error", "msg": "File not found in database"}