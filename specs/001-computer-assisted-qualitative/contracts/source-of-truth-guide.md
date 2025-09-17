# Source-of-Truth Guide
## Reflexive Thematic Analysis (TA) and the Working as Learning Framework (WALF)

> **Purpose.** This document codifies the analytic method (Reflexive Thematic Analysis) and the interpretive lens (WALF) for this project. It is the normative reference for both human analysts and LLM-assisted steps. The LLM must **not** rely on assumed background knowledge; it must use the definitions, steps, and decision rules described here.

> **Scope.** Textual qualitative data (interview transcripts, field notes, documents). WALF is the primary interpretive lens; TA provides the analytic process. Grounded theory may appear in external sources but is **background only**.

---

## Part A — Reflexive Thematic Analysis (RTA): Method

### A1. Principles
- **Constructed themes.** Themes are **constructed** (not discovered) through engaged interpretation.
- **Researcher subjectivity.** Subjectivity is a resource; reflexivity is continuous.
- **Iterative rigor.** The process is cyclical; earlier decisions can be revised.
- **Coherence.** Methods, data, and interpretation must align with the research aims.
- **Transparency.** Decisions, rationales, and revisions are documented.

### A2. Units, Artifacts, and Traceability
- **Unit of analysis.** Default segment is a paragraph or speaker turn; time-stamped utterances may be used if available.
- **Artifacts by phase.** Reading notes, initial codes, candidate themes, theme definitions, memos, and an audit log.
- **Identifiers.** Every segment, code, theme, and memo must have a stable ID for cross-referencing.
- **Traceability rule.** Every code and theme must link to at least one verbatim data extract (quote) and a memo with rationale.

### A3. Phase-by-Phase Procedure (with Exit Criteria and Quality Gates)

**Phase 1 — Familiarization**
- *Tasks.* Read the entire dataset; annotate initial observations; record positionality/reflexivity memos.
- *LLM role.* Produce condensed summaries and highlight salient passages; **do not** assign codes yet.
- *Outputs.* Familiarization notes; reflexivity memo(s).
- *Exit criteria.* Each source has (i) a short synopsis, (ii) a list of salient ideas, (iii) at least one reflexive memo.
- *Quality gate.* Notes reference concrete extracts; no premature coding labels.

**Phase 2 — Generating Initial Codes**
- *Tasks.* Label meaningful segments related to the research aims; allow overlapping codes.
- *LLM role.* Propose candidate codes with short rationales and evidence snippets.
- *Outputs.* Codebook v0 (name, definition, inclusion/exclusion rules, exemplar quotes), coded segments.
- *Exit criteria.* Each code has a definition and ≥2 supporting extracts (where available).
- *Quality gate.* Check redundancy (merge synonyms); flag ambiguous codes for review.

**Phase 3 — Constructing Themes**
- *Tasks.* Cluster related codes to form candidate themes; sketch relationships (maps).
- *LLM role.* Suggest clusters based on semantic similarity and co-occurrence; propose candidate theme labels.
- *Outputs.* Theme map v0 (theme → linked codes → representative extracts) + integrative memos.
- *Exit criteria.* Each candidate theme aggregates conceptually coherent codes and is linked to research questions.
- *Quality gate.* Distinctiveness: no theme duplicates another; codes do not force-fit themes.

**Phase 4 — Reviewing Themes**
- *Tasks.* Test each theme against the coded data and full dataset; split/merge/discard as needed.
- *LLM role.* Stress-test themes: retrieve counterexamples and borderline cases.
- *Outputs.* Theme map v1; revision notes; decision log (kept/merged/retired).
- *Exit criteria.* Each theme is internally coherent and externally distinct, with adequate evidentiary coverage.
- *Quality gate.* Negative cases addressed; sampling of extracts represents breadth of the dataset.

**Phase 5 — Defining and Naming Themes**
- *Tasks.* Write concise definitions; delimit scope and subthemes; finalize names.
- *LLM role.* Draft definitional statements and name options; human refines for conceptual precision.
- *Outputs.* Final codebook & theme compendium (definitions, inclusion/exclusion, prototypical quotes).
- *Exit criteria.* Each theme has: purpose, boundaries, subthemes (if any), and exemplary evidence.
- *Quality gate.* Definitions are actionable for independent readers.

**Phase 6 — Writing the Report**
- *Tasks.* Synthesize themes into an analytic narrative with integrated extracts and theoretical interpretation.
- *LLM role.* Assist with structure and draft prose; ensure all claims are evidence-linked.
- *Outputs.* Markdown report with YAML front matter; machine-readable JSON export; appendices (memos, logs).
- *Exit criteria.* Narrative shows how themes answer the research aims; limitations and reflexivity are explicit.
- *Quality gate.* Consistency with prior artifacts; all quotes anonymized; references to WALF are accurate.

### A4. Codebook Structure (minimum fields)
- `id`, `name`, `definition`, `inclusion_criteria`, `exclusion_criteria`, `examples` (list of quotes + source IDs), `notes`, `walf_alignment` (see Part B), `version`, `status` (draft/active/retired).

### A5. Decision Rules and Heuristics
- Prefer **fewer, well-defined** codes over many overlapping ones.
- If two codes co-occur in >70% of instances without clear distinction, consider merge.
- If a code lacks supporting extracts after review, retire or redefine.
- For every theme, include at least one **counterexample** or limitation memo.
- Maintain a **changeset** (what changed, why, by whom, when) for every revision.

---

## Part B — Working as Learning Framework (WALF): Interpretive Lens

### B1. Core Constructs
- **Levels of analysis:**  
  - *Macro:* policy, industry, organization-wide structures.  
  - *Meso:* site, unit, project team, trade group.  
  - *Micro:* individual worker, role, dyads.
- **Expansive–Restrictive Continuum:** Conditions shaping learning opportunities.  
  - *Expansive* indicators (illustrative): participation breadth; task variety; boundary crossing; mentoring; time for learning; feedback culture; progression pathways; recognition of learning.  
  - *Restrictive* indicators: narrow task cycles; limited participation; siloing; minimal support; time pressure; punitive error climate; dead-end roles.
- **Supporting dimensions (project-specific shortlist):**  
  `task_variety`, `participation_scope`, `knowledge_flow`, `supervision_quality`, `time_for_learning`, `safety_and_risk`, `tooling_and_resources`, `peer_support`, `formal_training`, `informal_learning`, `progression`, `recognition`, `voice_and_agency`, `coordination_across_trades`.

### B2. WALF Annotation Schema (per segment or memo)
- `wal.level` ∈ {macro, meso, micro, mixed, unclear}  
- `wal.dimension` ∈ {expansive, restrictive, mixed, unclear}  
- `wal.indicators` ⟂ controlled vocabulary (subset of shortlist)  
- `wal.actor` (role, e.g., apprentice, supervisor)  
- `wal.site` (pseudonymized location or facility)  
- `wal.evidence` (quote IDs)  
- `wal.confidence` ∈ {low, medium, high} with rationale

### B3. Coding Rubric (alignment with TA)
- **During initial coding (TA Phase 2):**  
  Add WALF tags opportunistically; it is acceptable to defer uncertain tags.
- **During theme construction/review (TA Phases 3–4):**  
  Evaluate whether themes reflect **systemic patterns** at one or more WALF levels; specify the dominant level(s) and indicator(s).
- **During definition/naming (TA Phase 5):**  
  Names should imply WALF alignment where appropriate (e.g., “Restricted participation in cross-trade tasks (meso)”).

### B4. Comparative Analysis Patterns
- **Within-site comparison:** Workers at the same facility across roles (micro ↔ meso).  
- **Cross-site comparison:** Patterns that hold across facilities (meso ↔ macro).  
- **Trend memos:** Note shifts from restrictive → expansive (or vice versa) over time or across projects.

---

## Part C — Operating Procedure (TA × WALF × System)

### C1. End-to-End “Formula”
1. **Prepare inputs.** Normalize text; assign document IDs; create dataset manifest.  
2. **Familiarize (TA1).** Summarize each source; create reflexivity memos; no codes yet.  
3. **Initial coding (TA2).**  
   - LLM proposes codes + short rationales + evidence spans.  
   - Human curates: merge, rename, define; start **Codebook v0**.  
   - Add **provisional WALF tags** where clear.
4. **Theme construction (TA3).**  
   - Cluster codes; draft **Theme Map v0**.  
   - Check WALF coverage (levels, indicators).  
   - Write integrative memos.
5. **Review (TA4).**  
   - Seek counterexamples; adjust themes; retire weak codes.  
   - Confirm anonymization and traceability.
6. **Define & name (TA5).**  
   - Finalize definitions; indicate WALF alignment per theme.  
   - Freeze **Codebook v1** and **Theme Map v1**.
7. **Report (TA6).**  
   - Generate Markdown + YAML; export JSON (segments, codes, themes, WALF tags, memos, lineages).  
   - Validate against schema and Constitution principles.

### C2. Human–LLM Division of Labor
- **LLM excels at:** pattern surfacing, candidate labeling, clustering, retrieval of evidence, drafting definitional text.  
- **Human leads on:** theoretical fit, boundary-setting, naming, adjudicating conflicts, reflexivity, ethical judgment.

### C3. Quality, Reflexivity, and Ethics
- **Reflexivity cadence.** At minimum: after TA1, TA3, and pre-publication.  
- **Anonymization.** Remove/replace direct identifiers; maintain a separate, encrypted key file outside exports.  
- **Bias checks.** Review for role/status bias (e.g., supervisor accounts overweighted); include negative cases.  
- **Audit trail.** Log all changes: `who`, `what`, `why`, `when`.

---

## Part D — Outputs (Authoritative Formats)

### D1. Markdown + YAML (per analytic report)
```yaml
# YAML front matter (minimum)
title: ""
dataset_id: ""
analyst: ""
date: ""
llm_backend: {provider: "openai", model: "", mode: "api"} # key stored outside repo
walf_focus: {levels: ["meso","micro"], dimensions: ["expansive","restrictive"]}
codebook_version: "1.0.0"
schema_version: "1.0.0"
anonymization: {status: "complete", method: "pseudonymization"}
sources:
  - {doc_id: "", type: "transcript|notes|report", date: ""}
themes:
  - {id: "", name: "", summary: ""}
```

### D2. JSON Export (sketch of required fields)
```json
{
  "dataset": {"id": "", "title": "", "created": "", "codebook_version": "1.0.0", "schema_version": "1.0.0"},
  "segments": [
    {
      "id": "seg-001",
      "doc_id": "int-01",
      "text": "…",
      "span": {"start": 123, "end": 256},
      "codes": ["c-availability_of_time", "c-peer_support"],
      "walf": {
        "level": "meso",
        "dimension": "restrictive",
        "indicators": ["time_for_learning", "coordination_across_trades"],
        "confidence": "medium",
        "evidence": ["q-001","q-017"]
      },
      "memos": ["m-045"]
    }
  ],
  "codes": [
    {"id": "c-peer_support", "name": "Peer support", "definition": "", "inclusion": "", "exclusion": "", "examples": ["q-017"], "walf_alignment": ["micro"], "status": "active"}
  ],
  "themes": [
    {"id": "t-restricted_participation", "name": "Restricted participation in cross-trade tasks", "definition": "", "codes": ["c-…","c-…"], "walf_alignment": {"levels":["meso"], "dimension":"restrictive"}, "examples": ["q-031","q-072"]}
  ],
  "quotes": [
    {"id": "q-017", "segment_id": "seg-001", "text": "…", "speaker": "Worker A (pseud.)"}
  ],
  "memos": [
    {"id": "m-045", "type": "reflexive|analytic|decision", "text": "…", "links": ["seg-001","t-restricted_participation"], "created": ""}
  ],
  "lineage": [
    {"entity_id": "c-peer_support", "action": "merge", "from": ["c-help_from_colleagues"], "by": "analyst", "at": "", "rationale": "redundancy"}
  ]
}
```

## D3. Validation Checklist (pre-commit)
- [ ] Schema valid (JSON + YAML).
- [ ] All IDs unique and referenced entities exist.
- [ ] Every theme has ≥2 distinct supporting quotes (where available).
- [ ] WALF tags present where warranted; confidence documented when uncertain.
- [ ] Anonymization complete; no direct identifiers in outputs.
- [ ] Audit trail updated and stored with the run log.

---

## Part E — Required Project Resources (for the repo)
- **Method guides** (this document): TA method; WALF lens; operating procedure.
- **Codebook template:** Machine-readable (YAML/JSON) with the fields in A4.
- **Controlled vocabularies:** WALF indicators (B1 shortlist) in a dedicated file.
- **Prompt templates:** Phase-specific LLM prompts with placeholders for dataset and research question.
- **Validation scripts:** Schema validators, referential integrity checks, anonymization scanner.
- **Governance files:** Constitution; scope; spec; plan; tasks; change log.

---

## Part F — Versioning and Governance
- [ ] Increment `codebook_version` when altering definitions, merges, or splits; include migration notes.
- [ ] Increment `schema_version` when changing fields, types, or relationships in exports.
- [ ] Record amendments in the change log; each analytic run stores model/version, prompts, and checksums.

---

## Part G — Accessibility and Neurodiversity-Informed Practices
- [ ] Provide structured views (outlines, summaries, bullet lists) for every long output.
- [ ] Keep short, labeled sections and phase checklists to reduce cognitive load.
- [ ] Use consistent terminology and plain language definitions in the codebook.
- [ ] Allow focus modes (e.g., show only a single theme with its extracts and memos).