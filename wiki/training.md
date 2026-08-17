---
title: Ghostline Training and Evaluation
updated: 2026-07-29
status: active
---

# Training and evaluation

## The result

The shipped 384-unit recurrent runner passed a one-time held-out audit over 500
unseen contracts per tier, 3,000 episodes in total:

| Tier | Success | Wilson 95% |
|---|---:|---|
| 1 | 99.8% | 98.9 – 100.0 |
| 2 | 100.0% | 99.2 – 100.0 |
| 3 | 96.4% | 94.4 – 97.7 |
| 4 | 98.0% | 96.4 – 98.9 |
| 5 | 99.0% | 97.7 – 99.6 |
| 6 | 89.6% | 86.6 – 92.0 |

The checkpoint, ONNX graph, parity report, benchmark JSON/CSV, demo recording
and throughput report are all bound to environment fingerprint
`521c449a8bd9a540977a918f5b094dd3aeff44cc579a55f75e22a74bab20e129`.

## How it was trained

Behavior cloning from an observation-only teacher, then four DAgger recovery
rounds on policy-induced states, then low-rate consolidation replay.

| Stage | Corpus | Updates |
|---|---|---:|
| Initial clone | 1,800 episodes / 412,483 transitions | 5,000 |
| DAgger rounds 1–4 | +2,100 episodes / 529,401 transitions | 6,000 |
| Consolidation | low-rate replay | 2,000 |
| **Total** | **3,900 episodes / 941,884 transitions** | **13,000** |

The teacher sees the same public observation and the same action mask as the
learner. It is not privileged, and no human demonstrations were used.

**PPO was tried and rejected.** A pilot ran to 153,600 steps and scored a
worst-tier 84% against the matched rollback's 90%, with deterministic action
agreement of 0.85. It is published unmodified as
`benchmarks/neural/ppo-pilot-rejected.json` with
`status: rejected_and_not_resumed`. PPO, GAE and RND are implemented and tested;
the released checkpoint claims no PPO improvement.

## Seed namespaces

Three ranges that cannot collide by construction, enforced in `seeds.py`:

| Range | Purpose |
|---|---|
| 0 – 999,999 | training |
| 1,000,000 – 1,049,999 | validation and checkpoint selection |
| 2,000,000+ | final test only |

`final_test_seed` refuses any start below 2,000,000. Validation seeds are
derived per tier and cannot leave their reserved window.

## The one-way final-test ledger

`benchmarks/final-test-slices.json` is an append-only record with no reopen
path. The evaluator takes an exclusive lock before the first episode, and a
slice may only be opened from `reserved_unopened`. On completion it becomes
`consumed` and the byte count and SHA-256 of every output file are recorded. Any
exception retires the slice as `aborted_retired` instead — a crashed audit is
never rerun on the same seeds.

Before a single episode runs, the reservation's environment fingerprint,
policy kind, episode count and tier set must all match. Afterwards the
fingerprint and checkpoint hash are re-checked, and drift retires the slice.

The ledger's honest content matters as much as its mechanism. Of seven slices,
one is consumed by the shipped champion, one by a superseded 7M champion, and
five are retired: three failed teacher audits, one historical tuning slice, and
one that passed a since-replaced acceptance curve.

## Selection

Tier promotion requires two consecutive held-out passes. Checkpoint selection
orders by worst-tier validation success, then tier-6 success, then damage,
trace, path efficiency, completion time and inference cost.

No final-test slice takes part in architecture, reward, curriculum or
checkpoint selection.

The shipped champion's confirmation gates are
`benchmarks/neural/consolidated-fast-ops-validation-a-100.json` and
`-b-100.json`, at validation offsets 6700 and 6900, scoring
99/99/96/99/99/85% and 100/100/96/99/99/86%. Note that the similarly named
`champion-confirmation-a-offset7400-200` files belong to the **superseded 7M
champion** and a different fingerprint; they are retained as history and are not
evidence for the shipped policy.

## Acceptance

- at least 95% success on tiers 1–5 and 85% on tier 6;
- 500 unseen seeds per tier;
- Wilson 95% intervals;
- failure taxonomy, time, trace, damage, optional data and path efficiency;
- PyTorch/ONNX deterministic action parity over at least 1,000 recurrent
  transitions.

## Known limitations

Stated plainly because the numbers above are strong enough not to need help:

- **Success is not stealth.** Median maximum trace is saturated at 100.0 on
  tiers 3, 4 and 6. The policy routinely pins the trace meter and extracts
  anyway. It solves the contract; it does not play quietly.
- **Path efficiency is 0.58–0.79**, so routes are competent rather than optimal,
  and tier-6 optional-data collection is 0.258.
- **The training corpus figures are prose.** The transition counts above come
  from the model card and lineage CSV; the intermediate DAgger rounds have no
  per-episode artifact in the repository. The final result is fully reproducible
  from the shipped checkpoint; the *training* that produced it is not.
- **One validation window (offset 7100) was used for three selection
  decisions** — DAgger rounds 3 and 4 and the consolidated candidate. The
  confirmation windows at 6700/6900 and the 8M final test are disjoint from it,
  but it is a multiple-comparisons foothold.
- **A single held-out number per tier.** The slice is consumed, so there is no
  repeated-run variance and no seed-of-training variance. The Wilson intervals
  are episode-sampling intervals only.
- **No superhuman claim.** That would need a matched-seed human cohort under a
  locked protocol, which has not been collected.
