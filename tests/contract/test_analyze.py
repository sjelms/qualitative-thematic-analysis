import subprocess

def test_analyze_success():
    """
    Tests that the analyze command successfully analyzes the data.
    """
    # Run the analyze command
    result = subprocess.run(
        ["qta", "analyze"],
        capture_output=True,
        text=True,
    )

    # Check the output
    assert result.returncode == 0
    assert "Analysis complete. Run `qta review` to see the suggestions." in result.stdout
