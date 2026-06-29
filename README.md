# 1. 数据基础学习项目

```markdown
## 📌 项目简介

本项目为数据分析基础学习过程中的实验记录与练习合集。
包含数据处理、可视化、统计分析等基础内容。

---

## 📂 内容

- 数据清洗实验
- Pandas 基础操作
- 可视化练习
- 数据探索分析

---

## ⚙️ 技术栈

- Python
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 🚀 使用方式

直接打开 notebook 运行即可：

```bash


---


#  2. 数据分析智能体（Data Analysis Agent）

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

---


#  3. Car Sales Data Analysis App（汽车销售分析）

```markdown
# 🚗 Car Sales Data Analysis App

## 📌 项目简介

一个基于 Streamlit + Pandas Agent 的汽车销售数据分析工具。
支持用户上传销售数据并进行智能分析。

---

## 🧠 功能

- 上传 CSV 数据
- 数据预览
- 自动统计信息
- 自然语言提问分析
- LLM 驱动数据推理

---

## ⚙️ 技术栈

- Streamlit
- Pandas
- LangChain Agent
- OpenAI GPT-4o-mini

---

## 🧩 工作流程

上传数据
→ 展示数据
→ 用户提问
→ AI 调用 Pandas Agent
→ 返回分析结果

---

## 🚀 运行方式

```bash
streamlit run app(1).py

---

# 4. Trip Planner Agent｜智能旅行规划系统

## 📌 项目简介

本项目是一个基于大语言模型（LLM）与多智能体系统（Multi-Agent）的智能旅行规划助手。
系统能够根据用户输入（城市、日期、偏好等），自动生成完整旅行方案，包括景点、酒店、天气与每日行程安排。

---

## 🧠 核心能力

- 自动生成旅行计划（多天行程）
- 景点推荐（调用高德地图 API）
- 天气信息查询
- 酒店推荐
- 结构化 JSON 旅行方案生成
- 多 Agent 协作（Planner / Weather / Hotel / Attraction）

---

## ⚙️ 技术架构

- Python
- LangChain / LLM
- MCP Tool（高德地图 API）
- 多智能体系统（Multi-Agent）
- JSON Schema 结构化输出

---

## 🧩 系统流程

用户输入
→ 景点 Agent（调用高德 API）
→ 天气 Agent
→ 酒店 Agent
→ Planner Agent（整合信息）
→ 输出 JSON 行程

---

## 📌 核心设计

- 使用 **Tool Calling（工具调用机制）**
- 使用 **多Agent分工**
- Planner 负责最终整合输出
- 所有输出强制 JSON 结构化

---

## 🚀 运行方式

```bash

