# Tasks: Computer-Assisted Qualitative Data Analysis System

**Input**: Design documents from `/specs/001-computer-assisted-qualitative/`
**Prerequisites**: plan.md, research.md, data-model.md, contracts/

## Phase 3.1: Setup
- [ ] T001 Create project structure with `src` and `tests` directories.
- [ ] T002 Initialize Python project and install dependencies: `pytest`, `openai`, `python-docx`, `PyPDF2`, `markdown`.
- [ ] T003 [P] Configure linting and formatting tools (e.g., `black`, `ruff`).

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T004 [P] Contract test for `qta ingest` in `tests/contract/test_ingest.py`.
- [ ] T005 [P] Contract test for `qta analyze` in `tests/contract/test_analyze.py`.
- [ ] T006 [P] Contract test for `qta review` in `tests/contract/test_review.py`.
- [ ] T007 [P] Contract test for `qta report` in `tests/contract/test_report.py`.
- [ ] T008 [P] Integration test for the main user workflow in `tests/integration/test_workflow.py`.

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T009 [P] Implement data models in `src/models.py`.
- [ ] T010 Implement `ingest` command logic in `src/cli/ingest.py`.
- [ ] T011 Implement `analyze` command logic in `src/services/analysis.py`.
- [ ] T012 Implement `review` command logic in `src/cli/review.py`.
- [ ] T013 Implement `report` command logic in `src/services/reporting.py`.
- [ ] T014 Implement main CLI entry point in `src/main.py`.

## Phase 3.4: Integration
- [ ] T015 Integrate `ingest` command with data models.
- [ ] T016 Integrate `analyze` command with data models and LLM service.
- [ ] T017 Integrate `review` command with data models.
- [ ] T018 Integrate `report` command with data models.

## Phase 3.5: Polish
- [ ] T019 [P] Unit tests for file parsing in `tests/unit/test_parsing.py`.
- [ ] T020 [P] Unit tests for reporting logic in `tests/unit/test_reporting.py`.
- [ ] T021 [P] Update `README.md` with usage instructions.

## Dependencies
- Tests (T004-T008) before implementation (T009-T014).
- T009 blocks T015, T016, T017, T018.
- Implementation before polish (T019-T021).

## Parallel Example
```
# Launch T004-T008 together:
Task: "Contract test for `qta ingest` in `tests/contract/test_ingest.py`"
Task: "Contract test for `qta analyze` in `tests/contract/test_analyze.py`"
Task: "Contract test for `qta review` in `tests/contract/test_review.py`"
Task: "Contract test for `qta report` in `tests/contract/test_report.py`"
Task: "Integration test for the main user workflow in `tests/integration/test_workflow.py`"
```

---
*Based on Constitution v1.0.0 - See `/memory/constitution.md`*
