# Tasks: Computer-Assisted Qualitative Data Analysis System (Jupyter Pivot)

**Input**: Updated design documents from `/specs/001-computer-assisted-qualitative/`
**Prerequisites**: plan.md (v2), constitution.md (v2)

## Phase 1: Environment Setup
- [ ] T001 Create `Dockerfile` for the Jupyter Scientific Python Stack.
- [ ] T002 Create `docker-compose.yml` to manage the containerized service.
- [ ] T003 Create a `.dockerignore` file to keep the container image lean.
- [ ] T004 Create the project directory structure: `notebooks/`, `data/raw`, `data/processed`, `src/`.

## Phase 2: Initial Notebook Development
- [ ] T005 Create the initial `analysis.ipynb` notebook in the `notebooks/` directory.
- [ ] T006 Add sections to the notebook for: Introduction, Setup, Data Ingestion, Analysis, and Reporting.
- [ ] T007 Implement the initial Python code in the notebook to import necessary libraries.

## Phase 3: Core Workflow Implementation
- [ ] T008 Implement data ingestion logic in the notebook to read files from `data/raw`.
- [ ] T009 Use Pandas to structure the ingested data into a DataFrame.
- [ ] T010 Implement the core analysis logic, integrating with the OpenAI API to suggest codes and themes.
- [ ] T011 Implement a review and refinement workflow for the researcher to interact with the suggested analysis.
- [ ] T012 Implement reporting logic to generate summaries and visualizations (e.g., using Matplotlib/Seaborn).

## Phase 4: Polish & Documentation
- [ ] T013 Create helper functions in the `src/` directory for any reusable code from the notebook.
- [ ] T014 Write unit tests for helper functions in `src/`.
- [ ] T015 Update `README.md` with detailed instructions on how to build and run the Jupyter environment using Docker.

---
*Based on Constitution v2.0.0 - See `/.specify/memory/constitution.md`*
