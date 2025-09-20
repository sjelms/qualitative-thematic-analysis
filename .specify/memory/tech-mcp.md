# MPC Server Docker Container

Containerizing your CAQDAS + MCP server is the cleanest way to get reproducibility, isolation, and secure key management while keeping your data safely mounted. Below is a pragmatic approach that balances simplicity with rigor.

## Recommendation

Use Docker with Compose. Run the MCP server and the CAQDAS pipeline inside one container with separate writable volumes for outputs and caches. Keep your OpenAI API key outside the repo and inject it at runtime via Docker secrets or environment variables. If you later add a local model (Ollama/LM Studio), run it as a separate service and point the MCP to it.

## Minimal architecture (start here)

- **Service:** cqda-mcp (your MCP server + CAQDAS pipeline)
- **Mounts:**
  - `/data/input` → raw data files in multiple child directories such as `interviews`, `field-notes`, etc. All mounted read-only.
  - `/data/output` → rendered Markdown + JSON exports (read/write)
  - `/data/cache` → model/tool caches, temp files (read/write)
- **Secrets/Env:** OPENAI_API_KEY injected at runtime (never committed)
- **Networking:** expose only the local MCP port; no public ingress
- **User:** run as non-root; set file ownership for mounted volumes

## Why this works for you

- Isolation & safety: raw data stays in a mounted path; the container cannot write back to the vault unless you allow it.
- Reproducibility: pinned dependencies, identical runs across machines.
- Ergonomics: you can access the same MCP from LM Studio, Cursor, or VS Code without changing your data paths.
- Future-proofing: easy to split into multiple services later (e.g., add ollama and switch the LLM adapter).

## Compose skeleton (illustrative)

```yaml
version: "3.9"
services:
  cqda-mcp:
    image: your-registry/cqda-mcp:0.1.0
    # or build: .
    container_name: cqda-mcp
    environment:
      # Prefer Docker secrets for production
      OPENAI_API_KEY: ${OPENAI_API_KEY:?set_me_at_runtime}
      MCP_BIND: "0.0.0.0:8765"   # your MCP endpoint
      APP_MODE: "api-first"      # document this in your spec
    ports:
      - "8765:8765"              # keep localhost-only via firewall or 127.0.0.1 binding
    volumes:
      - type: bind                # (read-only)
        source: /absolute/path/to/data-source
        target: /data/input
        read_only: true
      - cqda_output:/data/output  # reports, json exports
      - cqda_cache:/data/cache    # temp/model caches
    user: "1000:1000"             # non-root; match host UID/GID if needed
    restart: unless-stopped
    # security_opt: ["no-new-privileges:true"]  # optional hardening
    # read_only: true                            # if you add tmpfs for /tmp and keep /data writable

  # Optional local model service (future)
  # ollama:
  #   image: ollama/ollama:latest
  #   volumes:
  #     - ollama_models:/root/.ollama
  #   ports: ["11434:11434"]
  #   restart: unless-stopped

volumes:
  cqda_output:
  cqda_cache:
  # ollama_models:
```

## Key operational choices

- Secrets: inject `OPENAI_API_KEY` via docker run -e `OPENAI_API_KEY=`… or Docker secrets; never commit keys or `.env` with secrets to the repo.
- Read vs. write paths: treat /data/input as read-only. Write only to /data/output and /data/cache.
- Logs & audit trail: log to stdout (captured by Docker) and write a structured audit JSON into /data/output/run-logs/… for traceability (model, prompts, checksums).
- Schema validation: run validators inside the container before writing final outputs. Fail fast; do not emit partials.
- Upgrades: version the image (0.1.0, 0.2.0…), keep migrations for codebook/schema in the output folder alongside reports.
- Local models: if/when you use Ollama, switch an env flag (e.g., `LLM_BACKEND=ollama`) and hit `http://ollama:11434` from cqda-mcp via Compose networking.

## MCP vs. CLI in practice

- Keep a minimal CLI entry point in the image (e.g., cqda run …) for batch or scripted runs.
- Do your daily work through MCP from Cursor/LM Studio for scaffolded, low-friction interaction (better for attention and structure).

## Lightweight checklist (pre-build)

- Container runs as non-root, writes only to mounted output/cache.
- API keys injected at runtime; repo contains no secrets.
- Vault is mounted read-only; outputs are separate and backed up.
- MCP endpoint bound to localhost or firewalled; no public exposure.
- Validation and anonymization steps enforced before export.
- Image tagged and reproducible; migrations documented.

If you want, I can draft a service contract for your MCP (endpoints, input/output schemas) next, so you can plug it straight into LM Studio or Cursor without refactoring later.