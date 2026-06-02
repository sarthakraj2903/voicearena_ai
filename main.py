import pandas as pd

# Load data
df = pd.read_csv("approved_votes_en-US.csv")

print("Total rows:", len(df))
print("Columns:", df.columns)

# Combine comments
df["all_comments"] = df["comment_on_a"].fillna("") + " " + df["comment_on_b"].fillna("")

# Remove empty comments
df = df[df["all_comments"].str.strip() != ""]

print("Total comments:", len(df["all_comments"]))
print(df["all_comments"].head(10))


# 🔥 ADD THIS PART BELOW

# Categorization function
def categorize_comment(comment):
    comment = str(comment).lower()

    if any(word in comment for word in ["mispronounce", "mispronounced", "pronunciation", "نطق"]):
        return "Pronunciation Issue"

    elif any(word in comment for word in ["robot", "robotic", "unnatural", "آلية"]):
        return "Robotic Voice"

    elif any(word in comment for word in ["missing", "skipped", "no audio", "na", "ناقص"]):
        return "Missing / Audio Issue"

    elif any(word in comment for word in ["number", "digits", "رقم"]):
        return "Number Error"

    elif any(word in comment for word in ["fast", "slow", "awkward", "rhythm", "pacing"]):
        return "Fluency / Speed Issue"

    elif any(word in comment for word in ["breathing", "pause", "gap"]):
        return "Pauses / Breathing Issue"

    elif any(word in comment for word in ["good", "nice", "better", "no issues"]):
        return "Positive Feedback"

    else:
        return "Other"


# APPLY FUNCTION
df["issue_category"] = df["all_comments"].apply(categorize_comment)

# COUNT
issue_counts = df["issue_category"].value_counts()

# PRINT RESULT
print("\n===== FINAL ISSUE BREAKDOWN =====\n")
print(issue_counts)
import matplotlib.pyplot as plt

# Plot bar chart
issue_counts.plot(kind='bar')

plt.title("Top Issues in TTS Models")
plt.xlabel("Issue Category")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
print("\n===== MODEL A NAMES =====\n")
print(df[["model_a_id", "model_a_name"]].drop_duplicates().head(10))

print("\n===== MODEL B NAMES =====\n")
print(df[["model_b_id", "model_b_name"]].drop_duplicates().head(10))
# Group issues by Model A
model_a_issues = df.groupby(["model_a_name", "issue_category"]).size().unstack(fill_value=0)

print("\n===== MODEL A ISSUE BREAKDOWN =====\n")
print(model_a_issues)
# Group issues by Model B
model_b_issues = df.groupby(["model_b_name", "issue_category"]).size().unstack(fill_value=0)

print("\n===== MODEL B ISSUE BREAKDOWN =====\n")
print(model_b_issues)