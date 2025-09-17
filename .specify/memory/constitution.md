# Computer-Assisted Qualitative Data Analysis System Constitution

## Core Principles

### I. CLI Interface
Every feature is exposed via a command-line interface. The primary interaction with the system is through the CLI. The CLI follows standard conventions for arguments, flags, and input/output streams.

### II. Test-First (NON-NEGOTIABLE)
TDD is mandatory. Tests are written before the implementation. The Red-Green-Refactor cycle is strictly enforced. All code must be tested with `pytest`.

### III. Simplicity
The project follows the YAGNI principle. We start with the simplest solution and only add complexity when it is justified. The project maintains a single-project structure.

### IV. LLM-Assisted Workflow
The system leverages Large Language Models (LLMs) to assist the user. The interaction with LLMs is designed to be transparent and auditable. The user always has the final say and can override the LLM's suggestions.

## Technology Stack

**Language**: Python 3.11

**Primary Dependencies**:
- `openai`: For interacting with LLMs.
- `python-docx`: For processing `.docx` files.
- `PyPDF2`: For processing `.pdf` files.
- `markdown`: For processing `.md` files.

## Development Workflow

The development workflow follows these steps:
1.  **Specification (`spec`)**: A detailed feature specification is created.
2.  **Planning (`plan`)**: An implementation plan is created based on the specification.
3.  **Tasking (`tasks`)**: The work is broken down into smaller, actionable tasks.
4.  **Implementation**: The code is written, following the Test-First principle.

## Governance
This constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All pull requests and code reviews must verify compliance with this constitution.

**Version**: 1.0.0 | **Ratified**: 2025-09-17 | **Last Amended**: 2025-09-17
