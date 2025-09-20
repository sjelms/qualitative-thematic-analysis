# Research: Computer-Assisted Qualitative Data Analysis System

## Performance Goals

**Decision**: For the initial prototype, we will not set specific performance goals in terms of requests per second or memory usage. The focus is on functionality and user experience for a single researcher.

**Rationale**: The application is a local, single-user tool, not a high-traffic server application. Performance can be optimized in later iterations if needed.

**Alternatives considered**: Setting specific performance targets was considered but deemed premature for the initial prototype.

## Handling Large Files

**Decision**: The system will process files up to 100MB. For files larger than this, the system will warn the user and may process the file in chunks.

**Rationale**: A 100MB limit is a reasonable starting point for text files. Chunking will prevent memory issues with very large files.

**Alternatives considered**: Rejecting large files outright was considered but providing a warning and attempting to process them is more user-friendly.

## LLM API Unavailability

**Decision**: If the LLM API is unavailable, the system will fall back to a manual-only mode. The user will be notified of the API unavailability.

**Rationale**: This ensures that the user can still work with the system even if the LLM is not available. It also aligns with the "human-in-the-loop" principle.

**Alternatives considered**: Preventing the use of the application altogether was rejected as it would make the tool useless in case of API outages.
m