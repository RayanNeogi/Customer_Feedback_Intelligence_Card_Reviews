
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime


def generate_pdf_report(
    df,
    output_file="customer_feedback_report.pdf"
):

    doc = SimpleDocTemplate(
        output_file
    )

    styles = getSampleStyleSheet()

    content = []

    # =====================================
    # TITLE
    # =====================================

    content.append(
        Paragraph(
            "Customer Feedback Intelligence Report",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # KPI CALCULATIONS
    # =====================================

    total_feedback = len(df)

    negative_feedback = len(
        df[
            df["sentiment"]
            .astype(str)
            .str.lower()
            == "negative"
        ]
    )

    positive_feedback = len(
        df[
            df["sentiment"]
            .astype(str)
            .str.lower()
            == "positive"
        ]
    )

    high_priority = len(
        df[
            df["priority"]
            .astype(str)
            .str.lower()
            == "high"
        ]
    )

    negative_pct = (
        negative_feedback /
        total_feedback * 100
        if total_feedback > 0
        else 0
    )

    positive_pct = (
        positive_feedback /
        total_feedback * 100
        if total_feedback > 0
        else 0
    )

    top_category = (
        df["category"].mode()[0]
        if not df.empty
        else "N/A"
    )

    # =====================================
    # EXECUTIVE SUMMARY
    # =====================================

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    executive_summary = f"""
    Total Feedback Records: {total_feedback}<br/><br/>
    Negative Sentiment: {negative_pct:.1f}%<br/><br/>
    Positive Sentiment: {positive_pct:.1f}%<br/><br/>
    High Priority Issues: {high_priority}<br/><br/>
    Top Complaint Category: {top_category}
    """

    content.append(
        Paragraph(
            executive_summary,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================================
    # RISK SCORE
    # =====================================

    risk_score = min(
        100,
        (
            negative_feedback * 2
            +
            high_priority * 3
        )
    )

    content.append(
        Paragraph(
            "Risk Assessment",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Overall Risk Score: {risk_score}/100",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================================
    # BUSINESS KPIs
    # =====================================

    content.append(
        Paragraph(
            "Business KPIs",
            styles["Heading1"]
        )
    )

    kpis = f"""
    Total Feedback: {total_feedback}<br/>
    Positive Feedback: {positive_feedback}<br/>
    Negative Feedback: {negative_feedback}<br/>
    High Priority Issues: {high_priority}<br/>
    Most Common Category: {top_category}
    """

    content.append(
        Paragraph(
            kpis,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================================
    # EXECUTIVE INSIGHTS
    # =====================================

    content.append(
        Paragraph(
            "Executive Insights",
            styles["Heading1"]
        )
    )

    insights = f"""
    1. {top_category} is currently the most reported issue category.<br/><br/>

    2. Negative sentiment accounts for {negative_pct:.1f}% of all feedback.<br/><br/>

    3. There are {high_priority} high-priority cases requiring immediate attention.<br/><br/>

    4. Overall business risk score stands at {risk_score}/100.
    """

    content.append(
        Paragraph(
            insights,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # =====================================
    # RECOMMENDATIONS
    # =====================================

    content.append(
        Paragraph(
            "AI Recommendations",
            styles["Heading1"]
        )
    )

    recommendations = f"""
    • Prioritize investigation of {top_category} related complaints.<br/><br/>

    • Reduce high-priority incidents through proactive monitoring.<br/><br/>

    • Monitor negative sentiment trends weekly.<br/><br/>

    • Review operational workflows associated with recurring complaints.<br/><br/>

    • Continue collecting customer feedback to improve model accuracy.
    """

    content.append(
        Paragraph(
            recommendations,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # FOOTER
    # =====================================

    content.append(
        Paragraph(
            "Generated by Customer Feedback Intelligence Platform",
            styles["Italic"]
        )
    )

    doc.build(content)

    return output_file

