# 数据分析智能体（Data Analysis Agent）

```markdown
# 📊 数据分析智能体系统

## 📌 项目简介

本项目是一个基于 LLM + Pandas Agent 的数据分析系统。
用户可以上传 CSV 文件并通过自然语言提问获取数据分析结果。

---

## 🧠 核心功能

- CSV 数据上传
- 自动数据概览
- 自然语言数据分析
- Pandas Agent 自动生成代码
- 分析日志记录

---

## ⚙️ 技术栈

- Streamlit
- Pandas
- LangChain Experimental Agent
- OpenAI API

---

## 🧩 系统流程

用户上传数据
→ 展示数据结构
→ 输入问题
→ Pandas Agent 自动分析
→ 返回结果

---

## 🚀 运行方式

```bash
streamlit run 数据分析智能体.ipynb
