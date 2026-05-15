# make_data.py
import os
from pathlib import Path

# 建立 data 資料夾
Path("data").mkdir(exist_ok=True)

# 寫入一個簡單的文字檔當作模擬資料 (因為產生真實 PDF 需要額外套件，我們先產生 text 確保 ingest 能動)
with open("data/specs.txt", "w", encoding="utf-8") as f:
    f.write("Raydium AI Team Specification: High-performance inference engine for Display drivers.")

with open("data/presentation.txt", "w", encoding="utf-8") as f:
    f.write("Future AI Roadmap: Integrating LLM with hardware acceleration.")

print("✅ Data folder and test files created!")