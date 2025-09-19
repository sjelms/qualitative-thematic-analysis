import subprocess
import os
from pathlib import Path

def test_ingest_success():
    """
    Tests that the ingest command successfully ingests a file.
    """
    # Create a dummy file to ingest
    dummy_file_path = Path("test_data.txt")
    with open(dummy_file_path, "w") as f:
        f.write("This is a test file.")

    # Run the ingest command
    result = subprocess.run(
        ["qta", "ingest", str(dummy_file_path)],
        capture_output=True,
        text=True,
    )

    # Check the output
    assert result.returncode == 0
    assert f"Successfully ingested {dummy_file_path}" in result.stdout

    # Clean up the dummy file
    os.remove(dummy_file_path)

def test_ingest_file_not_found():
    """
    Tests that the ingest command fails when the file is not found.
    """
    # Run the ingest command with a non-existent file
    non_existent_file = "non_existent_file.txt"
    result = subprocess.run(
        ["qta", "ingest", non_existent_file],
        capture_output=True,
        text=True,
    )

    # Check the output
    assert result.returncode != 0
    assert "Error:" in result.stderr
