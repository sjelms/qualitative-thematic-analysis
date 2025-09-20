# Computer-Assisted Qualitative Data Analysis System Constitution

## Core Principles

### I. Jupyter Notebook Interface
The primary interaction with the system is through a Jupyter Notebook environment. The analysis workflow, from data ingestion to reporting, is managed within notebooks, allowing for an interactive and iterative research process.

### II. Test-First (NON-NEGOTIABLE)
TDD is mandatory for any helper functions or utility scripts created in the `src` directory. Tests are written before the implementation using `pytest`. The Red-Green-Refactor cycle is strictly enforced for all backend code. Notebooks should be runnable from top to bottom without errors.

### III. Simplicity
The project follows the YAGNI principle. We start with the simplest solution and only add complexity when it is justified. The project maintains a single-project structure.

### IV. LLM-Assisted Workflow
The system leverages Large Language Models (LLMs) to assist the user. The interaction with LLMs is designed to be transparent and auditable. The user always has the final say and can override the LLM's suggestions.

## Technology Stack

**Language**: Python 3.13

**Core Technologies**:
- Docker
- JupyterLab

**Primary Dependencies**:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `matplotlib` & `seaborn`: For data visualization.
- `nltk` & `spacy`: For natural language processing.
- `scikit-learn`: For machine learning tasks.
- `openai`: For interacting with LLMs.

## Development Workflow

The development workflow follows these steps:
1.  **Specification (`spec`)**: A detailed feature specification is created.
2.  **Planning (`plan`)**: An implementation plan is created based on the specification.
3.  **Tasking (`tasks`)**: The work is broken down into smaller, actionable tasks.
4.  **Implementation**: The code is written, following the Test-First principle where applicable.

## Governance
This constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All pull requests and code reviews must verify compliance with this constitution.

**Version**: 2.0.0 | **Ratified**: 2025-09-17 | **Last Amended**: 2025-09-20
