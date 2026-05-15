# Data Preprocessing as Claude Skills

這個專案展示了如何將非結構化數據（PDF、PPTX、TXT）處理能力封裝為 **Claude Code Skills**。透過建立安全執行邊界（Virtual Environment）與結構化輸出，使 AI Agent 能夠自動化執行複雜的數據提取與清洗任務。

## 🌟 核心功能
- **多格式解析**：支援從 PDF、PPTX 與純文字檔中提取內容。
- **數據結構化**：將雜亂的原始數據轉化為 AI 可讀的 JSON 格式。
- **Claude Skill 整合**：透過 `skill.json` 定義，讓 Claude Code 具備自動調用此工具的能力。
- **安全執行邊界**：所有操作侷限於虛擬環境與特定的輸出目錄。

## 📂 專案結構
```text
CLAUDE_SKILLS/
├── .venv/               # 安全執行邊界 (虛擬環境)
├── data/                # 原始數據存放區 ( specs.txt )
├── processed_output/    # Skill 執行後的結構化產出
├── ingest.py            # 數據攝取與清洗邏輯
├── processor_skill.py   # Claude Skill 入口點
├── skill.json           # Claude Skill 定義文件
└── requirements.txt     # 環境依賴定義
```

## 🛠️ 安裝與設置指南

### 1. 建立並啟動虛擬環境
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```
### 2. 安裝必要依賴
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```
### 3. 初始化數據與執行處理
```powershell
# 生成模擬測試數據 (specs.txt, presentation.txt)
python make_data.py

# 執行數據提取管道，將原始檔案轉化為結構化知識庫
python ingest.py
```

## ✅ 執行日誌與驗證 (Run Logs)

透過以下測試指令，可以驗證 Claude 是否能成功調用封裝好的 Skill 邏輯。這行指令模擬了 AI Agent 在獲取文件路徑後，呼叫工具進行結構化處理的完整過程：

```powershell
python -c "from processor_skill import run_skill; print(run_skill('specs.txt'))"
```

**預期輸出結果 (Success JSON)：**
```json
{
    "status": "success",
    "file": "processed_output\\specs.txt_structured.json"
}
```

**執行成功截圖：**
<img width="1942" height="74" alt="image" src="https://github.com/user-attachments/assets/11661b13-e367-438d-a7e3-f003e89d26dc" />

