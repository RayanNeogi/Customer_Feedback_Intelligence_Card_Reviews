class FeedbackCategorizer:

    def __init__(self):

        self.categories = {
            "Payment Issue": [
                "payment",
                "card",
                "charged",
                "refund",
                "billing",
                "transaction",
                "checkout"
            ],

            "Login Issue": [
                "login",
                "signin",
                "password",
                "otp",
                "authentication"
            ],

            "Performance Issue": [
                "slow",
                "lag",
                "freeze",
                "crash",
                "loading"
            ],

            "Feature Request": [
                "feature",
                "add",
                "improve",
                "enhancement",
                "request"
            ]
        }

    def categorize(self, text):

        text = text.lower()

        for category, keywords in self.categories.items():

            for keyword in keywords:

                if keyword in text:
                    return category

        return "Other"
    
if __name__ == "__main__":

    categorizer = FeedbackCategorizer()

    samples = [

        "My card payment failed",

        "I cannot login to the application",

        "The app crashes every day",

        "Please add dark mode"

    ]

    for text in samples:

        print(text)
        print(
            categorizer.categorize(text)
        )
        print("-" * 50)