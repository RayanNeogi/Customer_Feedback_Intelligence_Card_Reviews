import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))
import streamlit as st
import pandas as pd
from components.risk_engine import (
    calculate_risk
)
from components.alert_severity import (
    alert_severity
)
from components.customer_voice import (
    customer_voice
)

from components.root_cause_analysis import (
    root_cause_analysis
)
from components.pdf_report_generator import (
    generate_pdf_report
)
from components.wordcloud_view import (
    show_wordcloud
)
from components.executive_scorecard import (
    executive_scorecard
)
from components.csv_uploader import (
    upload_csv
)
from utils.data_loader import load_data
from components.executive_insights import (
    generate_insights
)
from components.heatmap import (
    sentiment_heatmap
)
from components.kpi_cards import render_kpis
from components.charts import (
    sentiment_chart,
    category_chart,
    priority_chart
)
from components.alerts import render_alerts


from components.executive_alert_engine import (
    run_alert_engine
)

from components.trend_analyzer import (
    show_trends
)

from components.recommendation_engine import (
    generate_recommendations
)

from components.database_stats import (
    database_stats
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Customer Feedback Intelligence",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# SYSTEM CONTROLS
# =====================================================

st.sidebar.subheader(
    "System Controls"
)

if st.sidebar.button(
    "🔄 Refresh Database"
):
    st.rerun()

# =====================================================
# LOAD DATA FROM SQLITE
# =====================================================

df = load_data()
upload_csv()

st.markdown("---")

# =====================================================
# DATABASE STATS
# =====================================================

database_stats(df)

st.markdown("---")
executive_scorecard(df)

st.markdown("---")
alert_severity(df)

st.markdown("---")
  
# =====================================================
# HEADER
# =====================================================

st.title(
    "📊 Customer Feedback Intelligence Platform"
)

st.markdown(
    """
Enterprise-grade NLP-powered customer feedback analytics platform.

### Features

- Sentiment Analysis
- Issue Categorization
- Priority Monitoring
- Executive Alert Engine
- Keyword Intelligence
- Trend Analytics
- AI Recommendations
- SQLite Database Integration
- Interactive Dashboard
"""
)

st.markdown("---")

# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("Filters")

selected_sentiment = st.sidebar.multiselect(
    "Sentiment",
    options=sorted(
        df["sentiment"]
        .dropna()
        .unique()
    ),
    default=sorted(
        df["sentiment"]
        .dropna()
        .unique()
    )
)

selected_category = st.sidebar.multiselect(
    "Category",
    options=sorted(
        df["category"]
        .dropna()
        .unique()
    ),
    default=sorted(
        df["category"]
        .dropna()
        .unique()
    )
)

selected_priority = st.sidebar.multiselect(
    "Priority",
    options=sorted(
        df["priority"]
        .dropna()
        .unique()
    ),
    default=sorted(
        df["priority"]
        .dropna()
        .unique()
    )
)

search_text = st.sidebar.text_input(
    "Search Feedback"
)

# =====================================================
# FILTER DATA
# =====================================================

filtered_df = df[
    (
        df["sentiment"]
        .isin(selected_sentiment)
    )
    &
    (
        df["category"]
        .isin(selected_category)
    )
    &
    (
        df["priority"]
        .isin(selected_priority)
    )
]

if search_text:

    filtered_df = filtered_df[
        filtered_df["feedback_text"]
        .astype(str)
        .str.contains(
            search_text,
            case=False,
            na=False
        )
    ]

# =====================================================
# KPI DASHBOARD
# =====================================================

st.header("📈 Executive KPIs")

render_kpis(filtered_df)

st.markdown("---")

# =====================================================
# ALERT CENTER
# =====================================================

run_alert_engine(
    filtered_df
)

st.markdown("---")

# =====================================================
# BUSINESS HEALTH SUMMARY
# =====================================================

st.header(
    "🏢 Business Health Summary"
)

total_feedback = len(
    filtered_df
)

negative_feedback = len(
    filtered_df[
        filtered_df["sentiment"]
        .astype(str)
        .str.lower() == "negative"
    ]
)

high_priority = len(
    filtered_df[
        filtered_df["priority"]
        .astype(str)
        .str.lower() == "high"
    ]
)

negative_pct = (
    negative_feedback
    / total_feedback * 100
    if total_feedback > 0
    else 0
)

top_category = (
    filtered_df["category"]
    .mode()[0]
    if not filtered_df.empty
    else "N/A"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Feedback",
        total_feedback
    )

with col2:

    st.metric(
        "Negative %",
        f"{negative_pct:.1f}%"
    )

with col3:

    st.metric(
        "High Priority",
        high_priority
    )

with col4:

    st.metric(
        "Top Category",
        top_category
    )

st.markdown("---")

# =====================================================
# ANALYTICS DASHBOARD
# =====================================================

st.header(
    "📊 Analytics Dashboard"
)

col1, col2 = st.columns(2)

with col1:

    sentiment_chart(
        filtered_df
    )

with col2:

    category_chart(
        filtered_df
    )

st.markdown("---")

priority_chart(
    filtered_df
)

st.markdown("---")

# =====================================================
# TREND ANALYSIS
# =====================================================

show_trends(
    filtered_df
)

st.markdown("---")

# =====================================================
# KEYWORD INTELLIGENCE
# =====================================================

st.header(
    "🔑 Keyword Intelligence"
)

if "keywords" in filtered_df.columns:

    all_keywords = []

    for row in filtered_df[
        "keywords"
    ].dropna():

        words = [
            word.strip()
            for word in str(row).split(",")
        ]

        all_keywords.extend(
            words
        )

    if len(all_keywords) > 0:

        keyword_df = (
            pd.Series(
                all_keywords
            )
            .value_counts()
            .head(20)
            .reset_index()
        )

        keyword_df.columns = [
            "Keyword",
            "Frequency"
        ]

        st.dataframe(
            keyword_df,
            use_container_width=True
        )

    else:

        st.info(
            "No keyword data available."
        )

st.markdown("---")

# =====================================================
# FEEDBACK EXPLORER
# =====================================================

st.header(
    "📄 Feedback Explorer"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# AI RECOMMENDATIONS
# =====================================================

generate_recommendations(
    filtered_df
)
st.markdown("---")

generate_insights(
    filtered_df
)
st.markdown("---")
customer_voice(
    filtered_df
)

st.markdown("---")

calculate_risk(
    filtered_df
)
st.markdown("---")

sentiment_heatmap(
    filtered_df
)
st.markdown("---")

show_wordcloud(
    filtered_df
)
st.markdown("---")

root_cause_analysis(
    filtered_df
)
st.markdown("---")
# =====================================================
# DOWNLOAD CENTER
# =====================================================

st.header(
    "⬇️ Download Center"
)

# CSV DOWNLOAD

csv = filtered_df.to_csv(
    index=False
)

st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="filtered_feedback.csv",
    mime="text/csv"
)

st.markdown("")

# PDF GENERATION

if st.button(
    "📄 Generate Executive PDF Report"
):

    pdf_file = generate_pdf_report(
        filtered_df
    )

    with open(
        pdf_file,
        "rb"
    ) as file:

        st.download_button(
            label="⬇️ Download PDF Report",
            data=file,
            file_name=pdf_file,
            mime="application/pdf"
        )

st.markdown("---")

# =====================================================
# FOOTER
# =====================================================

st.caption(
    """
Customer Feedback Intelligence Platform

Phase 7:
Database Integrated Executive Intelligence Platform

Features:
✓ SQLite Database
✓ NLP Analytics
✓ Alert Engine
✓ Trend Monitoring
✓ AI Recommendations
✓ Interactive Dashboard
"""
)