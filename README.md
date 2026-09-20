# 全球人口趨勢與地緣政治風險儀表板 (Global Population & Geopolitical Risk Dashboard)

本專案為 AI 工具應用能力實作考之交付作品，主要探討全球人口預測數據與伊朗地緣政治風險評估。

## 🌐 專案網址與檔案架構
* **GitHub Pages 網址**: https://danielhuang0801-droid.github.io/global-population-dashboard/
* **資料夾結構**:
  * `/data/raw.txt`: 人口原始數據
  * `/data/cleaned.json`: Python 計算後之 JSON 數據 (包含平均值、成長率、CAGR)
  * `/scripts/clean.py`: Python 資料清理與計算腳本
  * `index.html`: 前端 Dashboard 網頁

## 🤖 AI 使用聲明 (AI Disclosure)
本專案在開發過程中使用了生成式 AI 工具協助進行：
1. HTML/CSS 前端 Dashboard 基礎排版與 RWD 響應式設計生成。
2. Python 資料清理腳本 (`clean.py`) 邏輯與 CAGR 複合年均成長率計算公式撰寫。

### Prompt 提示詞範例
* **範例一 (前端網頁)**: "請幫我撰寫一個符合 RWD 響應式設計的 HTML 網頁，包含首頁標題、世界人口預測區塊、伊朗地緣政治風險矩陣表格，以及方法論說明。"
* **範例二 (Python 腳本)**: "請寫一個 Python 腳本讀取 raw.txt，計算人口數據的平均值、總成長率與 CAGR，並導出為 cleaned.json。"

## 🔍 資料驗證流程 (Verification Process)
1. **人口數據驗證**: 原始數據引用聯合國 World Population Prospects 報告。將 AI 提供之數據與 UN 官方數據對比，確認 2024、2030、2050 及 2100 年數據一致，避免 AI 幻覺。
2. **地緣政治風險驗證**: 風險矩陣中之事實（如霍爾木茲海峽為主要航運通道）均經過國際權威新聞與研調報告交叉比對。
