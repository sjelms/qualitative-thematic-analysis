# CLI Contracts: Computer-Assisted Qualitative Data Analysis System

## `qta ingest <file_path>`

- **Description**: Ingests a textual data file into the system.
- **Arguments**:
  - `file_path`: The absolute path to the file to ingest.
- **Success Output**: "Successfully ingested <file_path>."
- **Error Output**: "Error: <error_message>"

## `qta analyze`

- **Description**: Analyzes the ingested data and proposes initial codes and themes.
- **Success Output**: "Analysis complete. Run `qta review` to see the suggestions."
- **Error Output**: "Error: <error_message>"

## `qta review`

- **Description**: Opens an interactive session to review, accept, reject, or modify the AI-generated suggestions.
- **Details**: The exact implementation of the interactive session is to be defined, but it will be a command-line interface.

## `qta report`

- **Description**: Generates the final analysis report in Markdown and JSON formats.
- **Success Output**: "Report generated successfully. Check the `reports` directory."
- **Error Output**: "Error: <error_message>"
