# Project Scope: Computer-Assisted Qualitative Data Analysis System

## Overview
This project aims to design and build a custom **computer-assisted qualitative data analysis system (CAQDAS)** that integrates **Reflexive Thematic Analysis (TA)** with the **Working as Learning Framework (WALF)**. The system will enable a single researcher to ingest raw qualitative data (transcripts, field notes, reports), analyze it with the assistance of a large language model (LLM), and produce rigorous, transparent, and reusable outputs.  

The system is explicitly designed for **doctoral research in vocational education and workplace learning**, with WALF as the guiding interpretive lens and TA providing the analytic method. It will scaffold the researcher’s work, functioning as a “more knowledgeable other” by surfacing patterns, supporting iterative coding, and ensuring systematic rigor.

---

## Analytic Foundations
- **Reflexive Thematic Analysis (Braun & Clarke, 2021):**
  - Provides the analytic process: familiarization, coding, theme construction, review, definition, reporting.
  - Emphasizes reflexivity, iteration, and researcher subjectivity as resources.

- **Working as Learning Framework (Felstead et al., 2009):**
  - Provides the conceptual lens.
  - Focus on macro, meso, and micro levels of workplace learning.
  - Uses the expansive–restrictive continuum to interpret learning environments.

- **Separation of Source-of-Truth Documents:**
  - WALF documentation and TA methodological guide will be stored as separate reference documents within the repo.
  - The system will reference these documents directly instead of relying on the LLM’s assumed knowledge.

---

## Objectives
1. **Data Ingestion**
   - Accept textual data in structured/unstructured formats (e.g., `.txt`, `.md`, `.docx`, `.pdf`).
   - Audio/video will not be supported; all recordings must be transcribed to text prior to ingestion.
   - Future consideration: support for images, photos, and diagrams.

2. **Assisted Coding**
   - LLM proposes candidate codes and themes across the dataset.
   - Codes/themes aligned with WALF dimensions (macro/meso/micro + expansive–restrictive).
   - Researcher reviews and refines to maintain interpretive control.

3. **Human-in-the-Loop**
   - Researcher oversight required at each stage.
   - LLM functions as a support and pattern-recognition assistant, not a replacement for analytic judgment.

4. **Iterative Analysis**
   - Multiple rounds of coding and theme refinement supported.
   - Version control of codebooks, schemas, and analytic memos.
   - Change logs for transparency and reproducibility.

5. **Outputs**
   - **Markdown Reports:** Structured narratives with YAML front matter, embedded tags, wiki style links for Obsidian,annotations, and verbatim quotes.
   - **JSON Exports:** Machine-readable representations of segments, codes, themes, and memos, suitable for querying and reuse.
   - Traceability links across data → codes → themes → research questions.

---

## Technical Priorities
- **LLM Integration**
  - **API-first:** Primary use via OpenAI API.
  - Local experimentation possible later (e.g., open-source models).
  - API key stored securely outside the public repo.

- **Single-Researcher Application**
  - Designed for personal use in doctoral research.
  - No immediate support for multi-user collaboration or inter-coder reliability.

- **Neurodiversity-Informed Design**
  - Scaffolded prompts and outputs that reduce cognitive load.
  - Clear, structured feedback loops.
  - Emphasis on transparency, traceability, and iteration.

---

## Resources Required
- **Methodological References:**
  - Braun & Clarke (2021) _Thematic Analysis: A Practical Guide_.
  - Felstead, Fuller, Jewson & Unwin (2009) _Improving Working as Learning_ (WALF).
- **Researcher’s Data:**
  - Interview transcripts, field notes, research reports.
- **Supporting Documents:**
  - Spec Constitution.
  - Spec, Plan, and Task templates.
  - Methods-to-System Map.

---

## Expected Outcomes
- **Analytic Rigour:**  
  Systematic, transparent application of TA with WALF as the interpretive guide.
  
- **Efficiency and Support:**  
  Automation of repetitive coding tasks while maintaining researcher judgment.
  
- **Researcher Development:**  
  Provides scaffolding and expertise to support a novice researcher in advanced analytic tasks.
  
- **Reusable Outputs:**  
  Interoperable Markdown + JSON exports that can support further analysis, querying, or integration with other tools.

---

## Boundaries and Future Directions
- **Initial Scope:** Textual data only; single researcher; API-first with local experimentation secondary.
- **Future Extensions:**
  - Image/diagram ingestion.
  - Multi-user collaboration.
  - Advanced visualization of codes/themes (networks, heatmaps).