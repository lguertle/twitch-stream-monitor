# Twitch Stream Monitor 🎥📊

This project is a real-time data pipeline for monitoring Twitch streamers, leveraging the Twitch API and **Databricks** for data engineering and analytics. The pipeline collects, processes, and analyzes streamer profile and stream session data in a structured medallion architecture (bronze → silver → gold), enabling performance tracking and trend reporting.

---

## 🚀 Features

- 📥 **Data Ingestion**  
  Pulls live data from Twitch API endpoints for streamer profiles and current stream metadata.

- 🧼 **Data Cleaning & Enrichment**  
  Transforms and standardizes raw Twitch data, including deduplication and enrichment (e.g. follower change tracking).

- 📊 **Analytics & Reporting**  
  Aggregates metrics like average viewers, stream duration, and follower growth over time for trend analysis and dashboarding.

- 🔐 **OAuth Authentication**  
  Automatically handles Twitch OAuth2.0 client credential flow.

- 🔁 **Delta Lake + Databricks Integration**  
  Designed to run as a modular streaming pipeline within Databricks notebooks using Delta tables, with append-only logs for historical tracking.

- 📈 **Live Power BI Integration**  
  Delta tables are automatically connected to Power BI for dynamic dashboards, enabling real-time insights and visual exploration of stream performance.


---

## ⚡ Why Databricks?

This project uses **Databricks** as the central platform for managing the full lifecycle of the data pipeline:

- ✅ **Collaborative Development**: Interactive development and visualization in notebooks.
- 🔄 **Modular Pipeline**: The workflow is broken down into **bronze**, **silver**, and **gold** notebook stages.
- 🧱 **Delta Live Tables (DLT)**: Easily adaptable to Delta Live Tables for production-ready data workflows.
- 🧠 **ML-Ready Foundation**: Creates a clean and enriched dataset for downstream analytics, dashboarding, or machine learning models.
- 📊 **Seamless Power BI Integration**: Final gold-layer Delta tables are connected to Power BI for live, auto-refreshing reports.

---

## 📊 Example Use Cases

- 📈 **Track Growth Trends**  
  Monitor how streamers gain followers and viewers over time to identify rising stars.

- 🏆 **Generate Leaderboards**  
  Create daily or weekly leaderboards based on metrics like viewer count, duration, or follower change.

- 🎯 **Performance Monitoring**  
  Use trend data to track the impact of collaborations, events, or game choices on audience metrics.

- 🧪 **Data for A/B Testing**  
  Streamers or analysts can use the collected data to compare the effect of different streaming strategies.

- 🔍 **Discover High-Potential Streamers**  
  Identify newer streamers with fast follower/viewer growth to support marketing or community programs.

---

## 🧠 Future Enhancements

- 📊 **Add Interactive Dashboards**  
  Use Plotly Dash or Streamlit for real-time visualizations and custom analytics.

- 📦 **Delta Live Tables (DLT)**  
  Migrate to DLT for built-in orchestration, monitoring, and CI/CD in Databricks.

- 🗂️ **Multi-Stream Monitoring**  
  Track multiple streams across different categories or regions concurrently.

- 🧠 **Chat Sentiment Analysis**  
  Enrich stream data with real-time chat sentiment trends for context-aware analytics.

- 🔔 **Alerting System**  
  Trigger alerts for rapid drops/gains in viewership or follower count.

- 📤 **Data Export APIs**  
  Add endpoints or scheduled jobs to export daily summaries to Google Sheets or Slack.

---

## 🧑‍💻 Author

**Laurent Gürtler**  
Life Sciences Engineer & Data Enthusiast  
Specialized in real-time data pipelines, analytics, and applied machine learning for impactful research and product development.

- 🌐 [GitHub](https://github.com/lguertle)
- 📫 [LinkedIn](https://www.linkedin.com/in/laurent-gurtler-2z4/)

