
import os
import pandas as pd

from evidently import Report
from evidently.presets import DataSummaryPreset


# File locations
DATA_FILE = "data/addition_data.csv"
REPORT_DIR = "reports"

os.makedirs(REPORT_DIR, exist_ok=True)


def generate_report():

    # Check whether CSV exists
    if not os.path.exists(DATA_FILE):
        print("No data found. First execute the Addition API.")
        return

    # Read CSV data
    df = pd.read_csv(DATA_FILE)

    if df.empty:
        print("No records available.")
        return

    print("Dataset:")
    print(df)

    # Create Evidently report
    report = Report([
        DataSummaryPreset()
    ])

    # Generate report
    snapshot = report.run(
        current_data=df,
        reference_data=None
    )

    # Save HTML report
    report_path = os.path.join(
        REPORT_DIR,
        "addition_report.html"
    )

    snapshot.save_html(report_path)

    print("Evidently report generated successfully!")
    print("Report saved at:", report_path)


if __name__ == "__main__":
    generate_report()
