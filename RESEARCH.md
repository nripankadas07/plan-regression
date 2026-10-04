# User brief and comparison

**User:** Database engineer reviewing a query or index change using saved PostgreSQL EXPLAIN JSON.

**Pain:** A visual plan makes review possible but a deterministic offline CI decision still needs explicit metric and structural rules.

**Need:** Inferred need; comparable visualization tools do not establish absence of their own gates.

**Capability:** Compare operator identities at stable positional paths; report cost/row/time regressions separately from structural changes.

**Acceptance:** Threshold and minimum-delta boundaries, zero baseline, identity change, child paths and nonfinite input rejection.

**Discovery:** PostgreSQL EXPLAIN and query review checklists.

**Portfolio:** No existing SQL-plan product; traceweave analyzes agent trajectories, which is a different domain and data model.


## Search coverage

GitHub query `postgres explain in:description`, sorted by stars descending; observation 2026-10-04T12:43:43.178065+00:00. The top ten search results were screened for relevance. Search is not an exhaustive global ranking. Established comparables outside that query were also inspected; highest-star relevant comparable found among this researched set is identified below. Stars are research context, not technical performance.

Highest-star relevant comparable found: [dalibo/pev2](https://github.com/dalibo/pev2), 3602 stars.

| Comparable | Stars | Last push UTC | License | Workflow and tradeoff |
| --- | ---: | --- | --- | --- |
| [dalibo/pev2](https://github.com/dalibo/pev2) | 3602 | 2026-10-02T05:52:02Z | PostgreSQL | Current Vue visualizer with a downloadable offline HTML workflow; our positional JSON gate trades visualization for explicit review findings. |
| [AlexTatiyants/pev](https://github.com/AlexTatiyants/pev) | 2803 | 2020-07-15T20:27:50Z | MIT | Earlier Angular visualizer with npm/gulp setup; last observed push is dated 2020. |
| [mgartner/pg_flame](https://github.com/mgartner/pg_flame) | 1621 | 2020-01-13T23:28:06Z | Apache-2.0 | Go binary/Docker/Homebrew flamegraph workflow; last observed push is dated 2020. |

README installation and example workflows and available recent issues were inspected. Push time does not prove active support, and mature alternatives cover broader domains. No competitor installations or equivalent performance workloads were measured. Time to first result and runtime performance comparisons are unmeasured. Tests prove only this implementation. Demand is inferred unless an issue is linked explicitly; no users, adoption or results are fabricated.
