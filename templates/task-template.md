# Task template

````markdown
---
id: "TSK-{DOMAIN}-####"
type: "{bugfix|feature|enhancement|refactor|documentation|maintenance|research|security|performance}"
domain: "{backend|frontend|desktop|documents|server|common}"
affects: "{[domain] for domain task | [domain1, domain2, ...] for common task}"
depends_on: [TSK-]
priority: "{low|medium|high}"
audit: "{../../audits/.../*.md | ../../backlog/...*.md}"
status: "{draft|in-progress|review|done}"
---

# {Title}

## Context

[Background and motivation for this task]

## Requirements

- [ ] Requirement 1
- [ ] Requirement 2

## Implementation Plan

[Steps or approach to implement]

## Testing

[How to test the changes]

## Acceptance Criteria

- [ ] Criteria 1
- [ ] Criteria 2

## Notes

- Rule: `bugfix` → link to audit (`../../audits/.../*.md`).
- Rule: `feature` → link to backlog (`../../backlog/...*.md`).
- For other types (`refactor`, `documentation`, `research`, etc.) use audit link.
- Rule: domain task → `affects` only own domain (e.g. `[frontend]`).
- Rule: common task → `affects` includes all impacted domains (2+).

[Any additional notes or considerations]

```
````
