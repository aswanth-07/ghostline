---
title: Ghostline Project Log
updated: 2026-07-14
status: active
---

# Superhuman-agent and web-showcase pass

- Froze the current 384-unit GRU after two disjoint validation passes and consumed the one-way 8M audit exactly once. The 3,000 untouched contracts passed at `99.8/100.0/96.4/98.0/99.0/89.6%`; FP32 ONNX matched all 1,000 recurrent actions, while a five-mismatch INT8 candidate was rejected. The current checkpoint SHA-256 is `76baa30a...b2e47` and fingerprint is `521c449a...e129`.
- Fixed the live browser agent's permanent `HOLD` failure. Production WebGPU inference took about 60 ms, while the old adapter consumed one frame later, saw a busy bridge, discarded that generation, and queued another forever. The bridge now exposes versioned completion, Python retains unresolved generations, and prefetch runs five frames ahead. Chrome QA then measured threaded WASM as the faster backend for this compact model, so WASM is the release default and `?backend=webgpu` remains an explicit comparison path. High-DPI Pygbag sizing and WebAssembly presentation scaling now fill the complete 16:9 game frame.
- Replaced disappearing/stale operative ghosts with live facility-wide security telemetry shared identically by the human presentation and Env-v2 policy. Physical LOS and cones remain occlusion-correct. Standard/Interceptor/Elite chase speeds now reach 95/97/99% of normal player speed. Dash feedback is one 185 px noise wave per continuous dash with bounded particles and no decorative spoke burst.
- Replaced permissive packaging automation with a fail-closed portfolio release gate. The tracked source archive now contains locked dependencies, authored-art provenance, docs, scripts, static web sources, benchmark evidence, and the runnable Ghostline tests while consistently excluding only the retired `neon_arena` package/tests. The evaluator reconstructs cumulative reward components from the real terminal keys and rejects any mismatch with `reward_total`. The release verifier re-aggregates all 3,000 final episodes and binds their one-way slice hashes to the exact checkpoint, ONNX/parity evidence, current source fingerprint, measured 3,000 decisions/s release floor, and selected MP4. The earlier 5,000/s target remains an explicit optimization limitation rather than a published claim.
- Hardened the final web/package release boundary without changing simulation or the frozen neural fingerprint. Matched web cards now require identical tier and seed; live ONNX failure clears recurrent memory and stale action before restoring human control and labeling the run hybrid; Pygbag stages only twelve runtime modules plus the three manifest-declared atlases; BrowserFS and ONNX Runtime license/notices are checksum-locked release gates; and Windows packaging now requires the same v2 ONNX contract plus exact-byte, source-checkpoint-bound, 1,000-transition zero-mismatch parity evidence. Human-only builds remain explicitly diagnostic.
- Closed three final presentation-only contract gaps without changing the frozen training fingerprint: the terminal's outer link ring now matches the literal 40 px simulation radius; a hidden audible guard's current `STEPS <grade> / <status>` cue replaces its contradictory stale world/minimap ghost; and `RETURN` uses a calm patrol pose with no false question mark. Focused regressions cover all three display contracts.
- Qualified the final observation-only teacher at fingerprint `17d8617fd92015dc5a00b5314558fc7c0ff957685b12966efa5253806463739b`. Two disjoint 200-seed-per-tier validation gates reached `100/100/100/100/100/95%` and `100/99.5/99.5/100/100/94%`, clearing every teacher threshold twice without opening a final-test slice. The final contract audit replaced the teacher's last legacy 360 px entity decoder with the shared 390 px Env-v2 perception constant before these gates were opened; earlier A/B reports are explicitly superseded.
- Repaired the teacher's public-sensor semantics before qualification: projected footprint clearance now escapes safe wall-corner slides instead of idling forever; last-seen threat pressure expires at the `0.51` memory floor; quantized audio produces current coarse pressure without an invented facing cone; `RETURN` is decoded as recovery; and explicit guard grade scales threat. Tier-6 regressions `1,040,005`, `1,040,006`, and `1,040,011` all extract with zero damage.
- Enforced exact current-environment fingerprints on trajectory roots, neural checkpoints, and resumable optimizer state. Every pre-freeze corpus and BC/DAgger/PPO checkpoint is historical-only; fresh training begins from a new current-fingerprint teacher corpus.
- Completed the frozen-build gameplay readability audit for earned last-seen intel, quantized footsteps, dash noise, guard cause/state labels, trace thresholds, terminal timing, authored server fixtures, and actual debrief states. The only release defects found were generic wrapping that could split `EFFICIENT ROUTE` and positive badges appearing after a failed run. Successful debrief badges now occupy at most two explicit whole-badge lines; failed runs show their explicit reason instead, and the redundant body status row is gone because the screen title already owns that state.
- Replaced abrupt enemy deletion with deterministic player-earned security intel shared by simulation, Env-v2, renderer, and web takeover. Live state requires the shared 390 px LOS gate; guards/drones freeze at their last observed position after sight breaks, cameras remain mapped, and hidden audio uses quantized bearing/range rather than exact coordinates. The policy contract now has 13 entity features including explicit guard grade, unclipped zero-to-four pulse count, and map geometry matching the human minimap.
- Added intentional stealth feedback from the research pass: a literal 185 px dash-noise ring; observed `EYE/SOUND/RADIO` guard causes; deterministic grade-specific patrol scan pauses/search persistence; `SPOTTED -> LINE BROKEN -> SEARCHING -> CLEAR` recovery copy; trace threshold ticks; pre-deployment drone warning; terminal link-time labels; and Ghost/No Damage/Optional Data/Efficient Route debrief badges.
- Eliminated invisible furniture collision in server and specialist rooms. Atlas crops previously left three cells of a 1x4 server bank, two cells of a vertical sofa, and some locker/console bank cells visually empty while they still blocked movement. Generation now decomposes those modular banks into stable one-tile props without changing the blocked-tile union; a pixel-level regression audits every cell of every authored furniture footprint. The required 10,000-level procedural audit passed at 131.1 levels/second.
- Repaired the actual Pygbag 0.9.3 runtime contract: browser PEP-723 dependencies use WASM-repository keys, retired key art and the unused APK are absent, Vercel uses Chrome-compatible COEP `credentialless`, focus loss pauses active play, mixed controller runs are labeled hybrid, and the ONNX gate now rejects wrong dtypes/outputs/contract/fingerprint. The human-only static build is 3.17 MB locally with an estimated compressed cold transfer near 16.53 MB; final Chrome/agent QA waits for the champion ONNX.
- Replaced the pseudo-isometric opening illustration with the flat code-native facility schematic used across every menu state, removed the old art from all runtime package paths, and updated clean-install checks. The source/derivatives remain provenance-only under the MIT asset record.
- Removed square tile-fog compositing from gameplay so floors and furniture remain fully legible. Security now reads through smooth 65-ray, occlusion-correct camera/guard cones plus existing color-and-shape cues; exact entity positions remain visibility-gated.
- Added Standard, Interceptor, and Elite guard grades with restrained `1.04x/1.10x/1.16x` movement multipliers and readable `I/II/III` badges. Grades are introduced progressively across tiers and the fastest chase remains slower than the runner.
- Fixed permanently grey furniture: exploration now reveals an occluder's exposed face when player LOS reaches the nearer adjacent floor, but does not reveal floor behind it. Already explored tiles bypass future ray work; the focused regression passed and one-worker throughput improved from 370.3 to 448.6 decisions/second.
- Froze the post-visual mechanics distribution with guaranteed alternate-route loops, distinct-room open terminal sockets, specialist-room data values, wall-biased camera mounts, objective-aware camera orientation, four/five-tile security buffers, and camera-safe link pockets. The stricter 10,000-seed audit passed at 99.0 levels/second with zero unreachable or permanently scanned contracts.
- Rebuilt guard routing around radius-checked five-cell look-ahead, choke-aware separation, smooth recentring, and authored cross-room patrols. A directed 1,146-door traversal audit had zero jamb stalls. Partial sightings now produce a suspicious check, search guards scan their last-known point, and tackle impact disperses nearby chasers to prevent integrity dogpiles.
- Centralized camera/guard range and field-of-view constants so detection and rendered cones share one mechanics contract.
- Replaced the diagonal-animation shortcut with a dedicated alpha-clean 16-frame locomotion atlas: four-frame northeast/southeast loops for runner and guard, deterministic northwest/southwest mirroring, stable bottom pivots, nearest-neighbour scaling, Reduced Motion support, and a direction-preserving procedural fallback. The original chroma-key source and MIT provenance are documented but excluded from release payloads.
- Corrected displayed camera and guard cones to the exact simulation range/FOV, refined each fan against wall/prop occlusion, and reduced calm-cone opacity so the room remains readable. Added distinct dashed-camera and notched-guard patterns, segmented acquire badges, a top-centre detection meter, typed/labeled edge warnings, and a Field Manual legend; these cues remain color-plus-shape safe and expose no additional enemy state.
- Retired the immutable 3M teacher audit at `100.0/100.0/97.0/94.8/96.8/80.8` and the 4M audit at `100.0/100.0/96.6/95.2/97.2/83.8`; neither slice was reused for tuning or selection.
- Centralized validation seed allocation and selected the Tier-6 3.5x directional-inertia scale only on two disjoint 200-seed validation slices. The subsequent untouched 5M audit reached `100.0/100.0/97.6/93.6/97.4/85.6`, passing Tier 6 but exposing Countermeasure's non-monotonic integrity-loss spike.
- Smoothed Countermeasure from four to three guards while retaining its cameras, networked doors, guarded terminals, and three pulse charges.
- Passed the then-current untouched 6M teacher gate at `100.0/100.0/95.8/96.2/97.2/88.8` over 500 seeds per tier. No controller, mechanics, or generation setting changed while the slice was open; the later final mechanics freeze intentionally retired this report to historical status. Complete Wilson-interval evidence remains tracked in `benchmarks/teacher/`.
- Added an executable 12-frame 720p/1080p scale matrix that proves exact 2x/3x nearest-neighbour presentation with zero pixel mismatches, no crop, and no stretch. After the v2 cone/locomotion pass, the full render/present path measured 94.31 FPS at 720p and 81.32 FPS at 1080p in the hidden-surface QA run.
- Repaired two inspection-found menu defects: long dossier copy now wraps within the right panel, and Agent Lab keeps its deterministic-replay subtitle in the left column while explicitly identifying public sensors/no hidden state in the dossier. The Timer Assist row and disclosure now fit cleanly at both release resolutions.
- Added release-safe dynamic-INT8 ONNX export. FP32 remains canonical; both
  recurrent graphs receive independent deterministic action-parity audits, and
  INT8 can become the deployment copy only at zero mismatches. JSON evidence
  now includes byte sizes, SHA-256 hashes, reduction, rejection reason, and the
  selected fallback precision.
- Closed the distribution asset gap: wheels and source archives now carry the
  MIT license, asset manifest, and alpha-clean runtime visual atlases. The
  renderer resolves package resources, source assets, and PyInstaller assets
  through one path contract, and clean-install verification renders a hidden
  frame outside the checkout.
- Made portfolio web builds fail closed on the selected ONNX champion. The
  regular CI fallback is now explicitly named and invoked as a human-only
  diagnostic; Vercel and release workflows require the model, include the MIT
  license, and derive recurrent width from validated ONNX graph metadata.

- Added an opt-in 35% human timer-assistance accessibility mode and tagged assisted runs in telemetry so later human-versus-agent comparisons cannot mix them with standard contracts.
- Replaced asymmetrically clipped progress reward with discount-consistent geodesic potential shaping and added a closed-cycle exploit regression test before recovery training continued.
- Split release dependencies into base, lightweight `[agent]`, `[train]`,
  `[media]`, `[build]`, and `[web]` contracts; refreshed the lock to current
  PyPI releases including ONNX Runtime 1.27.0, pytest 9.1.1, and tqdm 4.68.4.
- Replaced the developer CLI PyInstaller entry with a player-only entry point,
  required the selected ONNX policy for release builds, excluded PyTorch and
  training/media modules, added executable/policy hashes, and added a packaged
  headless ONNX smoke gate.
- Added Python 3.12/3.14 base-compatibility CI, a genuinely isolated wheel
  install probe, locked CI installs, and current GitHub Actions release steps.
- Verified 10,000 freshly generated contracts with zero validation failures in 37.32 seconds (268 levels/second).
- Measured 5,168 aggregate tier-6 policy decisions/second across 22 Windows worker processes, clearing the 5,000 decisions/second training target; one-process throughput remains about 408 decisions/second.
- Verified the integrated Python suite at 113 passed and one intentional legacy skip after adding guard tackle-windup and localized-radio-alert regressions.
- Built the human-only Pygbag release at 1.59 MB local first-run payload / 2.87 MB deployment payload. With the current test model, the lazy agent path is about 23.95 MB; ONNX Runtime Web/WASM recurrent inference measured 1.11 ms median and 1.94 ms p95 in the non-interactive Node smoke test.
- Added the alpha-clean environment atlas v1 and integrated nearest-neighbour, bottom-pivot sprites for authored furniture, terminals, and cameras. High Contrast adds silhouette outlines; missing or unmapped art retains the procedural fallback. Source chroma-key drafts are excluded from Windows and web runtime payloads.
- Added the alpha-clean character/security atlas v1 with eight-direction runner/guard/drone mappings, dedicated action and alert-state sprites, nearest-neighbour scaling, bottom pivots, High Contrast outlines, and full procedural actor/device fallback.
- Reworked presentation into a cinematic pixel system with approved project-owned key art, procedural fallback, eight-direction animated actors, room-role materials, environmental decals, animated equipment, fog, local glow, and visibility-gated security drawing.
- Added player-readable terminal progress, directional danger arrows, color-plus-shape awareness cues, alert banners, pulse waves, damage recovery treatment, dash afterimages, captions, and a trace-responsive procedural music layer.
- Replaced the single settings list with persistent Audio, Accessibility, Controls, and Display pages. Added separate master/music/SFX levels, sound captions, high contrast, color-safe mode, reduced motion/flashes, HUD scale, timer warnings, tutorial hints, fullscreen, shake, and conflict-safe keyboard rebinding.
- Upgraded Agent Lab with deterministic seed stepping, ONNX-first player-runtime loading, live action/latency/recurrent-state telemetry, objective phase, and local human-versus-agent cards.
- Added human and agent JSONL telemetry at `%LOCALAPPDATA%/Ghostline/runs-v1.jsonl` plus compact recent-run history for matched-seed benchmarking.
- Added focused headless visual/accessibility/profile/telemetry tests and representative screenshot QA.
- Stabilized the shared acquire objective with terminal hysteresis and replaced one-tile route bearings with a visible six-tile look-ahead, eliminating objective flips and doorway steering oscillation without exposing hidden map state.
- Added separate guard/drone damage attribution to simulation terminal info and evaluation reports.
- Retained the reused 2M teacher tuning audit at 100.0%, 100.0%, 98.2%, 96.8%, 98.0%, and 87.6% as provenance only; it did not serve as the final comparison. Each later 3M/4M/5M audit was retired immediately after inspection before the untouched 6M pass.
- Iterated the 500-seed tier-5 curve from 92.0% through 92.6%, 93.4%, and 94.4% to 98.0%. The final run reduced mean damage to 0.402 (0.356 guard, 0.046 drone) and median maximum trace to 62.31.
- Kept the learning pipeline framework-light: behavior cloning, DAgger, RND, recurrent PPO/GAE, selection, and resume state are pure in-project PyTorch. The selected 384-unit GRU BC+DAgger champion passed the one-time 3,000-episode final evaluation at `98.0/98.2/99.2/97.0/95.8/94.8%`; its matched-seed PPO pilot regressed and was rejected transparently.

- Registered `GhostlineEnv-v2` with an explicit player-equivalent objective vector while retaining the v1 baseline.
- Added seven training-only reverse-curriculum lessons and terminal telemetry for matched-seed evaluation.
- Preserved the 2.98M-decision, zero-success pure-PPO run as failure-analysis evidence and moved to a fair teacher → BC/DAgger → RND-PPO pipeline.
- Split training dependencies from the player runtime and added lightweight ONNX inference.
- Added cooperative async game-loop and static Pygbag/Vercel build foundations; interactive web QA is Chrome-only.

# Playability and fairness pass

- Made hacking mobile within a larger visible interaction zone and reduced link duration.
- Added gradual awareness, shorter chase memory, damage invulnerability, and persistent partial hack progress.
- Added telegraphed guard/drone strike wind-ups plus post-impact search/recoil windows so a single contact cannot become an unavoidable integrity cascade.
- Fixed patrol doorway oscillation with sliding movement, waypoint invalidation, and deterministic stuck recovery.
- Added objective security exclusion zones, more route loops and mission time, rebalanced security counts, and additional pulse charges.
- Added interaction and camera-awareness cues plus regression tests and procedural fairness fuzzing.

# 2026-07-11 — Ghostline clean break

- Replaced the public product identity with Ghostline while preserving `neon_arena` as legacy reference code.
- Added deterministic 60 Hz simulation, modular furnished room generation, quota hacking, extraction, trace floor/escalation, integrity, timer, dash, pulse, cameras, guards, response drones, and event-driven presentation.
- Registered `GhostlineEnv-v1` with a maskable 36-action space and player-equivalent structured dictionary observations.
- Added a 640×360 scrolling pixel presentation, menus, stage selection, briefings, pause, settings, how-to-play, credits, HUD, minimap, debrief, progression, Agent Lab, particles, lighting, and procedural audio.
- Added the initial entity-aware recurrent policy, PPO trainer, curriculum state, evaluation, recording, and Windows packaging commands.
- Migrated off the stale Sample Factory dependency ceiling to current Gymnasium, NumPy, and PyTorch releases; the trainer now uses a native recurrent PPO implementation without an extra RL framework runtime.
- Verified 79 tests, Gymnasium environment checker, 10,000 valid procedural seeds, and roughly 342 tier-6 decisions/second in one Windows process.
- Scripted baseline smoke result: 100% on tiers 1–2 and 0% on tiers 3–6, demonstrating that higher tiers require learned stealth rather than path following.
