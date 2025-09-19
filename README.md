# Computer-Assisted Qualitative Data Analysis System (CAQDAS)

## About the Project

This project is a command-line interface (CLI) application designed to assist a single researcher in performing Reflexive Thematic Analysis (TA) guided by the Working as Learning Framework (WALF). The system leverages a Large Language Model (LLM) to propose codes and themes from qualitative data, acting as a "more knowledgeable other" while ensuring the researcher maintains full interpretive control.

The primary goal of this tool is to provide a structured and supportive environment for qualitative data analysis, particularly for doctoral researchers in vocational education and workplace learning. By automating parts of the coding process, the system aims to reduce cognitive load and enhance analytic rigor.

### Key Features:
* **Data Ingestion**: Supports various text-based file formats, including `.txt`, `.md`, `.docx`, and `.pdf`.
* **AI-Assisted Analysis**: Utilizes an LLM to propose initial codes and themes based on the ingested data.
* **Interactive Review**: Provides an interactive session for the researcher to review, accept, reject, or modify the AI-generated suggestions.
* **Report Generation**: Generates comprehensive reports in both Markdown and JSON formats, ensuring traceability and reusability of the analysis.

---

## Getting Started

To get started with the CAQDAS tool, follow these simple steps.

### Prerequisites

Ensure you have Python 3.11 or higher installed on your system.

### Installation

1.  Clone the repository:
    ```sh
    git clone [https://github.com/your-username/qualitative-thematic-analysis.git](https://github.com/your-username/qualitative-thematic-analysis.git)
    ```
2.  Navigate to the project directory:
    ```sh
    cd qualitative-thematic-analysis
    ```
3.  Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

The tool is designed to be used from the command line and follows a straightforward workflow.

### 1. Ingest Data

Begin by ingesting your qualitative data files. The tool supports `.txt`, `.md`, `.docx`, and `.pdf` formats.

```bash
qta ingest /path/to/your/interview-transcript.txt
```

### 2. Analyze Data
After ingesting your data, you can start the analysis process. The tool will use an LLM to propose initial codes and themes.

```bash
qta analyze
```

### 3. Review Suggestions
Once the analysis is complete, you can review the AI-generated suggestions in an interactive session.
```bash
qta review
```

In the review session, you can:

- Accept a suggestion.
- Reject a suggestion.
- Modify a suggestion.
- Add your own codes and themes.

### 4. Generate Report
When you are satisfied with your analysis, you can generate the final report.
```bash
qta report
```

The report will be saved in the `reports` directory in both Markdown and JSON formats.

## Development Conventions
This project adheres to a strict set of development conventions to ensure consistency and quality.

### Workflow
The development process follows a structured workflow:

1. *Specification* (`spec`): Create a detailed feature specification.
2. *Planning* (`plan`): Develop an implementation plan based on the specification.
3. *Tasking* (`tasks`): Break down the work into actionable tasks.
4. *Implementation:* Write the code, following the Test-First principle.

## Constitution
The project is governed by a constitution that outlines its core principles:
- *CLI Interface:* All functionality must be exposed through a command-line interface.
- Test-First: Test-Driven Development (TDD) is mandatory. All tests are written before the implementation.
- *Simplicity:* The project follows the YAGNI (You Ain't Gonna Need It) principle, starting with the simplest solution and adding complexity only when necessary.
- *LLM-Assisted Workflow:* The user always has the final say and can override any suggestions made by the LLM.

---

## Scripts
The project includes several bash scripts to automate common development tasks. These scripts are located in the `.specify/scripts/bash` directory.
- `create-new-feature.sh:` Creates a new feature branch, directory, and specification file.
- `setup-plan.sh:` Sets up the implementation plan for a feature.
- `check-task-prerequisites.sh:` Checks if the prerequisites for generating tasks are met.
- `update-agent-context.sh:` Updates the AI agent's context with the latest project information.
