# Data Model: Computer-Assisted Qualitative Data Analysis System

## Raw Data

- **Description**: Represents the textual data ingested into the system.
- **Attributes**:
  - `id`: Unique identifier for the data source.
  - `name`: The name of the file.
  - `content`: The full text content of the file.
  - `format`: The file format (e.g., `.txt`, `.md`, `.docx`, `.pdf`).

## Code

- **Description**: A label assigned to a segment of text.
- **Attributes**:
  - `id`: Unique identifier for the code.
  - `text`: The text of the code (e.g., "workplace learning").
  - `description`: A detailed description of the code.

## Theme

- **Description**: A higher-level pattern of meaning, derived from codes.
- **Attributes**:
  - `id`: Unique identifier for the theme.
  - `name`: The name of the theme.
  - `description`: A detailed description of the theme.
- **Relationships**:
  - Has many Codes.

## Codebook

- **Description**: A document that defines the codes and their usage.
- **Attributes**:
  - `id`: Unique identifier for the codebook.
  - `version`: The version of the codebook.
  - `codes`: A list of all codes defined in the codebook.

## Analytic Memo

- **Description**: A researcher's reflective notes on the analysis.
- **Attributes**:
  - `id`: Unique identifier for the memo.
  - `title`: The title of the memo.
  - `content`: The content of the memo.
  - `date_created`: The date the memo was created.

## Report

- **Description**: The final output of the analysis.
- **Attributes**:
  - `id`: Unique identifier for the report.
  - `format`: The format of the report (Markdown or JSON).
  - `content`: The content of the report.
  - `date_generated`: The date the report was generated.
