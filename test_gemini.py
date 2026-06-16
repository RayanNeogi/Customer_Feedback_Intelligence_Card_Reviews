from src.llm.gemini_service import ask_gemini

context = """
Total Feedback: 250
Negative Feedback: 42%
Top Category: Payment Issue
High Priority: 61
"""

print(
    ask_gemini(
        "What should management prioritize?",
        context
    )
)