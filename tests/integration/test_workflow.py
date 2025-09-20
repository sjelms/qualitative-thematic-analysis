import subprocess
import os
from pathlib import Path

def test_main_workflow():
    """
    Tests the main user workflow from ingestion to report generation.
    """
    # 1. Ingest a file
    dummy_file_path = Path("test_data_workflow.txt")
    with open(dummy_file_path, "w") as f:
        f.write("This is a test file for the main workflow.")

    ingest_result = subprocess.run(
        ["qta", "ingest", str(dummy_file_path)],
        capture_output=True,
        text=True,
    )
    assert ingest_result.returncode == 0

    # 2. Analyze the data
    analyze_result = subprocess.run(
        ["qta", "analyze"],
        capture_output=True,
        text=True,
    )
    assert analyze_result.returncode == 0

    # 3. Review the suggestions (simulating some user input)
    review_result = subprocess.run(
        ["qta", "review"],
        capture_output=True,
        text=True,
        input="accept all\nexit\n",
    )
    assert review_result.returncode == 0

    # 4. Generate the report
    report_result = subprocess.run(
        ["qta", "report"],
        capture_output=True,
        text=True,
    )
    assert report_result.returncode == 0
    assert "Report generated successfully." in report_result.stdout

    # Clean up
    os.remove(dummy_file_path)
    reports_dir = Path("reports")
    if reports_dir.exists():
        for f in reports_dir.glob("*"):
            os.remove(f)
        os.rmdir(reports_dir)
