import subprocess
import os
from pathlib import Path

def test_report_success():
    """
    Tests that the report command successfully generates the reports.
    """
    # Ensure the reports directory is clean before the test
    reports_dir = Path("reports")
    if reports_dir.exists():
        for f in reports_dir.glob("*"):
            os.remove(f)
        os.rmdir(reports_dir)

    # Run the report command
    result = subprocess.run(
        ["qta", "report"],
        capture_output=True,
        text=True,
    )

    # Check the output
    assert result.returncode == 0
    assert "Report generated successfully. Check the `reports` directory." in result.stdout

    # Check that the reports directory and files were created
    assert reports_dir.is_dir()
    assert (reports_dir / "report.md").is_file()
    assert (reports_dir / "report.json").is_file()

    # Clean up
    for f in reports_dir.glob("*"):
        os.remove(f)
    os.rmdir(reports_dir)
