# Skeleton: 0.1-architecture.md

> **⛔ Copy the template content below VERBATIM (excluding the outer code fence). Replace `[FILL]` placeholders. Do NOT add/rename/reorder sections.**
> **⛔ Key Components table columns are EXACTLY: `Component | Type | Description`. DO NOT rename to `Role`, `Change`, `Function`.**
> **⛔ Technology Stack table columns are EXACTLY: `Layer | Technologies` (2 columns). DO NOT add `Version` column or rename `Layer` to `Category`.**
> **⛔ Security Infrastructure Inventory and Repository Structure sections are MANDATORY — do NOT omit them.**

---

````markdown
# Architecture Overview

## System Purpose

[FILL-PROSE: 2-4 sentences — what is this system, what problem does it solve, who are the users]

## Key Components

| Component | Type | Description |
|-----------|------|-------------|
[REPEAT: one row per component]
| [FILL: PascalCase name] | [FILL: Process / Data Store / External Service / External Interactor] | [FILL: one-line description] |
[END-REPEAT]

## Component Diagram

```mermaid
[FILL: Architecture diagram using service/external/datastore styles — NOT DFD circles]
```

## Top Scenarios

[REPEAT: 3-5 scenarios. First 3 MUST include sequence diagrams.]

### Scenario [FILL: N]: [FILL: Title]

[FILL-PROSE: 2-3 sentence description]

```mermaid
sequenceDiagram
    [FILL: participants, messages, alt/opt blocks]
```

[END-REPEAT]

## Technology Stack

| Layer | Technologies |
|-------|--------------|
| Languages | [FILL] |
| Frameworks | [FILL] |
| Data Stores | [FILL] |
| Infrastructure | [FILL] |
| Security | [FILL] |

## Deployment Model

[FILL-PROSE: deployment description — ports, protocols, bind addresses, network exposure, topology (single machine / cluster / multi-tier)]

**Deployment Classification:** `[FILL: one of LOCALHOST_DESKTOP | LOCALHOST_SERVICE | AIRGAPPED | K8S_SERVICE | NETWORK_SERVICE]`

### Component Exposure Table

| Component | Listens On | Auth Required | Reachability | Min Prerequisite | Derived Tier |
|-----------|------------|---------------|--------------|------------------|-------------|
[REPEAT: one row per component from Key Components table]
| [FILL: component name] | [FILL: port/address or "N/A — no listener"] | [FILL: Yes (mechanism) / No] | [FILL: one of: External / Internal Only / Localhost Only / No Listener] | [FILL: one of closed enum — see rules below] | [FILL: T1 / T2 / T3] |
[END-REPEAT]

## Security Infrastructure Inventory

| Component | Security Role | Configuration | Notes |
|-----------|---------------|---------------|-------|
[REPEAT: one row per security-relevant component found in code]
| [FILL] | [FILL] | [FILL] | [FILL] |
[END-REPEAT]

## Repository Structure

| Directory | Purpose |
|-----------|---------|
[REPEAT: one row per key directory]
| [FILL: path/] | [FILL] |
[END-REPEAT]
````
