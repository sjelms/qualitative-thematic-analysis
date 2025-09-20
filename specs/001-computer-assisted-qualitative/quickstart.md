# Quickstart: Computer-Assisted Qualitative Data Analysis System

This guide will walk you through the basic workflow of using the Qualitative Thematic Analysis (QTA) tool.

## 1. Ingest Data

Start by ingesting your qualitative data files into the system. The supported formats are `.txt`, `.md`, `.docx`, and `.pdf`.

```bash
qta ingest /path/to/your/interview-transcript.txt
```

## 2. Analyze Data

Once you have ingested your data, you can start the analysis. The tool will use an LLM to propose initial codes and themes.

```bash
qta analyze
```

## 3. Review Suggestions

After the analysis is complete, you can review the suggestions in an interactive session.

```bash
qta review
```

In the review session, you can:
- Accept a suggestion.
- Reject a suggestion.
- Modify a suggestion.
- Add your own codes and themes.

## 4. Generate Report

Once you are satisfied with your analysis, you can generate the final report.

```bash
qta report
```

The report will be generated in both Markdown and JSON formats in the `reports` directory.
