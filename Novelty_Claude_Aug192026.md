# Novelty Report: The RAC-Space Classicalization Construction

## Verdict

**Possibly novel, but closely related prior work exists.** The final inequality (c₁² + c₂² ≤ 1) and even a two-parameter generalization of it are already in the literature. What may still be narrowly novel is the specific *classical-cut-and-recompose* operational story used to motivate it. This is not a sweep of the full literature (that would need the 20–30 query campaign the original brief asks for); it is a focused pass through the highest-risk candidates, using your own project's citation list as the backbone.

**Confidence: medium.** High confidence that Pawłowski et al. (2009) is the single closest paper. Lower confidence on complete coverage of the "closure under wirings" and "maximal correlation" literatures, which are large and not exhaustively searched here.

---

## The single most threatening result

**Pawłowski, Paterek, Kaszlikowski, Scarani, Winter, Żukowski, "Information Causality as a Physical Principle," Nature 461, 1101 (2009); arXiv:0905.2292.**

The main text derives the familiar bound using a *symmetric* two-copy concatenation: a resource with bias E, used twice through a classical relay, must satisfy 2E² ≤ 1, i.e. E ≤ 1/√2 — the Tsirelson value falls out of a purely classical-relay argument. That much is well known and is not itself in question.

The line that matters more is this one, stated in their main text as a result proved in their Supplementary Information:

> "…the more general result is proved, that for any ½(E²_I + E²_II) > E²_Q where E_j = 2P_j − 1 … Information Causality is violated…"

Unpacking notation, E_I and E_II are exactly your c₁ and c₂ — two *separate* retrieval biases for a 2→1 RAC-like task — and the claimed boundary is

E²_I + E²_II ≤ 1 (in units where E_Q² = 1/2 is normalized away),

i.e. **your circle, with two independently-labeled biases, already appears as a named result** in this paper's supplementary material. The construction that produces it is a concatenation of the same box, with a classical bit crossing between layers (Alice's answer to a sub-block is a classical message fed into the next stage) — which is structurally very close to "classicalize the intermediate outcome, then reuse the resource."

What's *not* identical:
- Their derivation route is via the Information Causality inequality (a sum of mutual informations, ΣI(xᵢ:β) ≤ m), evaluated in the limit of an asymptotically deep concatenation tree, not via a one-shot appeal to the *classical RAC bound* |d₁| + |d₂| ≤ 1.
- Their construction is framed as "does information causality hold," not "does the recomposed object have to be an ordinary classical RAC."
- Whether their two-copy argument is, after unpacking, operationally identical to yours (independent copy → classical cut → reuse → reinterpret as classical RAC → apply classical bound) is a real open question that requires reading their Supplementary Information line by line, which was not directly retrievable in this pass — only the main-text description of the SI result was available. **This is the single highest-priority item to check before any novelty claim is made.**

Rating: **ORANGE, bordering RED** for the specific inequality; **YELLOW/ORANGE** for the specific operational route (classical cut vs. information-causality budget).

---

## Second most relevant: a mathematically identical circle, different setting

**Toner & Verstraete, "Monogamy of Bell correlations and Tsirelson's bound," arXiv:quant-ph/0611001 (2006).**

Their Theorem 1: for three parties A, B, C sharing a state, each choosing between two observables,

⟨B_AB⟩² + ⟨B_AC⟩² ≤ 8.

Dividing through by the algebraic max (2√2)² = 8, this is *exactly* your circle in normalized form: two correlation strengths, sharing a common resource/party, obey a sum-of-squares ≤ 1 bound, with Tsirelson's bound recovered as the single-correlator special case. But the operational setting is a **monogamy trade-off between two different bipartite correlations that share one party (A)** — not two independent uses of the same RAC resource joined by an explicit classical cut. There is no classicalization step and no reinterpretation as a classical RAC; the bound comes from a dimension-reduction + SDP-style geometric argument on tripartite quantum states.

Rating: **YELLOW** — same boundary shape, essentially unrelated derivation and operational story. Worth citing as "the circle recurs" evidence, not as prior art for the construction.

---

## Background/framework literature: closure under wirings

**Allcock, Brunner, Linden, Popescu, Skrzypczyk, Vértesi, "Closed sets of nonlocal correlations," Phys. Rev. A 80, 062107 (2009).**

This paper is the origin of the general framework your construction instantiates: the requirement that a physically admissible set of correlations be *closed under wirings* (arbitrary classical processing of independent copies of a box, including that intermediate results are ordinary classical bits). They show this is a nontrivial constraint that not every candidate set of correlations satisfies, and they study several closed sets (L, Q, NS, CHSH-cutoff sets). This is exactly the *general principle* your construction specializes to the 2→1 RAC scenario with squared composition.

What's missing from this paper specifically: it does not, as far as retrieved, single out the RAC 2→1 scenario, does not derive c₁² + c₂² ≤ 1 as a wiring-closure consequence, and does not use the "reinterpret the composed object as a classical RAC and reapply the classical bound" move — it works with CHSH-type correlators and general wirings, not biased-guessing tasks.

Rating: **GREEN/YELLOW** — establishes the correct general principle (closure under wirings as a physical requirement) that your construction is a special case of, but does not contain the specific construction.

Related, same lineage: **Dukarić & Wolf**, and the "Closed sets of correlations: answers from the zoo" line of follow-up work on the open conjecture about continuum families of wiring-closed sets — background only (GREEN), no RAC-specific instantiation found.

---

## Checked and ruled largely background (GREEN)

- **Popescu & Rohrlich (1994)** — origin of the PR-box/no-signaling axiom framing; no RAC composition argument.
- **Short & Barrett (2010)**, **Gross, Müller, Colbeck, Dahlsten (2010)**, **Al-Safi & Richens (2015)**, **Janotta (2011)** — Boxworld/GPT state-measurement trade-off and reversible-dynamics literature; relevant as background for *why* post-quantum theories might fail to compose the way quantum theory does, but none contains a two-bias RAC squaring argument with a classical cut.
- **Masanes & Müller (2011)** — GPT reconstruction via reversibility axioms; unrelated construction.
- **Carmeli, Heinosaari, Toigo (2019)** — connects QRAC advantage to measurement incompatibility; doesn't touch composition/classicalization.
- **Le, Meroni, Sturmfels et al. (2023)** — correlation-body/algebraic-geometry treatment of the CHSH polytope; relevant for vocabulary (quantum vs. classical correlation bodies) but not for the composition argument.
- **Dmello, Ligthart, Gross (2024)** and **Dmello & Gross (2026)** — entanglement swapping / iterated CHSH in GPTs; these ask whether CHSH strength *survives* composition (and show post-quantum GPTs *can* sustain CHSH = 4 indefinitely). This is a different question (stability of nonlocality under a coherent, not classicalized, relay) and does not contain your explicit classical-cut RAC argument. Useful as a counterpoint ("composition doesn't force collapse to quantum in general — the classical cut is doing the work in your argument, not composition per se").
- **Umekawa et al. (2026)** — Boxworld entanglement generation from product states; unrelated to RAC composition.

None of these are close enough to independently threaten novelty of the *specific* construction, though several (Short–Barrett, Gross et al.) are the right citations for framing why the classical cut matters.

---

## What is definitely not novel

- That independent binary biases multiply under composition (c₁c₂-type composition of binary symmetric channels) — standard, appears throughout the concatenated-RAC and Information Causality literature.
- That Σcᵢ² ≤ 1 is the quantum RAC/CHSH boundary and Σ|cᵢ| ≤ 1 is the classical one — standard.
- That a sum-of-squares circle is *a* natural boundary recurring in multiple quantum-correlation contexts (Toner–Verstraete monogamy, Pawłowski et al.'s IC bound) — well known, not novel.
- That physically admissible correlation sets should be closed under wirings/classical processing — the explicit, named subject of Allcock et al. (2009) and its successors.

## What may still be novel (narrow claim)

The narrowest defensible claim, pending direct verification of the Pawłowski et al. Supplementary Information text, is something like:

> "The two-bias circle c₁² + c₂² ≤ 1 is not new — it appears at least in the supplementary material of Pawłowski et al. (2009) and, in a different guise, as the Toner–Verstraete monogamy bound. What may be worth presenting is a *one-shot, closure-under-wirings framing specific to the 2→1 RAC task*: treating the squared-bias point as the output of an explicit classicalization-and-reuse wiring, then directly invoking the classical RAC polytope bound (rather than an asymptotic information-causality argument), as an illustration of the general wiring-closure principle of Allcock et al. applied concretely to this simplest RAC case."

This is a presentation/pedagogical novelty claim, not a "new inequality" claim — and it should not be asserted without first reading the Pawłowski SI directly.

---

## Suggested blog-safe wording

Given the audience and goals (Medium Science Spectrum piece, explain-don't-claim):

- Safe: *"This isn't a new inequality — the same circle shows up in Tsirelson's original bound, in a monogamy relation between three parties (Toner & Verstraete), and even inside the fine print of the paper that introduced Information Causality. What's fun here is a different, very concrete way to arrive at it: split the resource in two, force a classical bottleneck in the middle, and watch the circle fall out."*
- Avoid: any claim that the construction or the inequality is new, until the Pawłowski SI has actually been read.

---

## Search log (this pass)

**Project knowledge (already curated by you):** confirms your own outline file already flags Pawłowski's IC concatenation and the closure-under-wirings literature as the key risk; nothing in project knowledge overturns that assessment.

**Web searches run:**
1. closure under wirings nonlocal box binary correlations classical communication bound
2. "random access code" concatenation biases multiply classical interface Tsirelson circle
3. Pawlowski et al. information causality arXiv / supplementary material (fetch attempt on SI blocked by tool sandboxing — not independently re-read)
4. (project knowledge) Toner–Verstraete monogamy full text
5. (project knowledge) Dmello–Gross entanglement swapping / teleportation-stable GPTs

**Not yet run** (from your original, much larger query list): maximal correlation / Hirschfeld–Gebelein–Rényi / hypercontractivity-ribbon searches; Beigi–Gohari; Ibnouhsein & Grinbaum; Weilenmann & Colbeck adaptive CHSH in detail; "no advantage for nonlocal computation" / exclusivity-principle literature; systematic arXiv-listing sweep through 2026. These remain open risk areas.

## Remaining risk

- The Pawłowski et al. SI itself was not directly read in this pass — only its main-text summary. This is the single biggest gap; it should be read line-by-line before any novelty claim.
- The maximal-correlation / strong-data-processing / hypercontractivity literature (Beigi, Gohari, and others) was not searched in this pass and is exactly the kind of place where "biases multiply, sum-of-squares appears, closure under composition is imposed" could recur under completely different vocabulary.
- "Parity-oblivious RAC," "retrieval games," and communication-complexity/index-function framings were only lightly touched.
- A truly comprehensive check would need the full 20+ query sweep from your original brief; this report should be read as a fast triage, not a clearance.