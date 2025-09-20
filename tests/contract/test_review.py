import subprocess

def test_review_starts():
    """
    Tests that the review command starts an interactive session.
    """
    # Run the review command
    result = subprocess.run(
        ["qta", "review"],
        capture_output=True,
        text=True,
        input="exit\n",  # Immediately exit the interactive session
    )

    # Check the output
    assert result.returncode == 0
    assert "Starting review session..." in result.stdout
