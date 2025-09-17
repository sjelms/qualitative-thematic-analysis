# GEMINI.md: AI Agent Instructions

## Project Overview

This project is a **Computer-Assisted Qualitative Data Analysis System (CAQDAS)**. It is designed to assist a single researcher in performing Reflexive Thematic Analysis (TA) guided by the Working as Learning Framework (WALF). The system is a CLI application that uses a Large Language Model (LLM) to propose codes and themes from qualitative data.

**Main Technologies:**
- **Workflow Automation**: Bash scripts located in `.specify/scripts/bash`.
- **Application Logic**: Python 3.11 (as specified in the implementation plan).
- **LLM Integration**: OpenAI API.

**Architecture:**
- The system is a command-line interface (CLI) application.
- It follows a structured workflow for feature development, from specification to implementation.

## Building and Running

This project is a collection of scripts and documents that manage a development workflow. There is no single build command. The workflow is executed by running the bash scripts in the `.specify/scripts/bash` directory.

**Key Scripts:**
- `.specify/scripts/bash/create-new-feature.sh`: Creates a new feature branch, directory, and specification file.
- `.specify/scripts/bash/setup-plan.sh`: Sets up the implementation plan for a feature.

## Development Conventions

This project follows a strict development workflow, which is codified in the project's constitution and templates.

**Development Workflow:**
1.  **Specification (`spec`)**: Create a detailed feature specification using the `.specify/templates/spec-template.md`.
2.  **Planning (`plan`)**: Create an implementation plan based on the specification using the `.specify/templates/plan-template.md`.
3.  **Tasking (`tasks`)**: Break down the work into smaller, actionable tasks using the `.specify/templates/tasks-template.md`.
4.  **Implementation**: Write the code, following the Test-First principle.

**Constitution:**
The project has a constitution located at `.specify/memory/constitution.md`. This document defines the core principles of the project, including:
- **CLI Interface**: All functionality is exposed through a CLI.
- **Test-First**: TDD is mandatory.
- **Simplicity**: The project follows the YAGNI principle.
- **LLM-Assisted Workflow**: The user maintains control over the LLM's suggestions.

**Templates:**
The project uses templates for creating new artifacts. These templates are located in the `.specify/templates` directory.
