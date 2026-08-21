Based on a comprehensive search of the scholarly literature through August 2026, including arXiv preprints, peer-reviewed journals, and citation chains from foundational papers on random access codes (RACs), nonlocal box wirings, Information Causality, and generalized probabilistic theories (GPTs), I can now provide a novelty assessment.

## Verdict

**Likely novel** — with high confidence that the *specific operational construction* you describe has not appeared in the literature in this form.

**Confidence level:** ~85–90%

The individual mathematical ingredients (bias multiplication, quadratic bounds, closure under wirings, concatenation of RACs) are well known, but I have not found any paper that combines **all** of the following in the way you propose:

- A 2→1 RAC (or operationally equivalent task) with separate retrieval biases \(c_1, c_2\);
- Two independent uses of the same resource;
- An **explicit classical cut** between the two uses (no coherent quantum or post-quantum system crosses the intermediate interface);
- Multiplication of biases under this classical composition (\(d_i = c_i^2\));
- Reinterpretation of the composed object as a **classical one-bit RAC**;
- Application of the classical bound \(|d_1| + |d_2| \le 1\) **after** composition;
- Recovery of the quantum circle \(c_1^2 + c_2^2 \le 1\) as a **consistency/closure requirement** on admissible physical correlations.

No source implements this exact logical chain or presents the quantum RAC boundary as emerging from a "classicalization-and-recomposition" consistency argument.

***

## The 10–20 Closest Papers (Ranked by Threat to Novelty)

Below are the most relevant works, ordered from most to least threatening. Each entry includes full citation, DOI/arXiv ID, year, the exact relevant result, and a RED/ORANGE/YELLOW/GREEN rating.

### 1. Pawłowski & Żukowski, "Entanglement assisted random access codes" (2010)
- **Citation:** M. Pawłowski and M. Żukowski, *Phys. Rev. A* **81**, 042326 (2010).
- **DOI:** [10.1103/PhysRevA.81.042326](https://doi.org/10.1103/PhysRevA.81.042326); arXiv:0906.0524 [quant-ph].
- **Year:** 2010 (arXiv 2009).
- **Relevant result:** Introduces **Entanglement-Assisted RACs (EARACs)** and shows that via **concatenation** of primitive (2,1,p) EARACs, one can construct (n,1,p) EARACs for arbitrary n. The procedure uses classical inputs/outputs at every stage, so concatenation is possible.
- **Comparison:** Uses concatenation of RACs with classical interfaces, but:
  - Does **not** formulate retrieval biases \(c_i\) or their multiplication;
  - Does **not** derive \(c_1^2 + c_2^2 \le 1\) from a classical bound after composition;
  - Concatenation is used to **amplify** RAC performance, not to derive a consistency boundary.
- **Rating:** **YELLOW** — related mechanism (concatenation with classical interfaces), but different goal and no quadratic-bound derivation.

### 2. Allcock et al., "Closed sets of correlations" (2009)
- **Citation:** J. Allcock, N. Brunner, N. Linden, S. Popescu, P. Skrzypczyk, and T. Vértesi, *arXiv:0908.1496* [quant-ph] (2009).
- **DOI/arXiv:** arXiv:0908.1496v2.
- **Year:** 2009.
- **Relevant result:** Introduces the concept of **closure under wirings** for sets of nonlocal correlations. Shows that physically consistent sets must be closed under classical wirings of multiple boxes. Demonstrates that certain natural sets (e.g., Uffink's set) are **not closed**.
- **Comparison:** Central idea of closure under classical wirings is conceptually aligned, but:
  - No RAC formulation or retrieval biases;
  - No derivation of \(c_1^2 + c_2^2 \le 1\) from a classical communication bound;
  - Focus is on CHSH-type correlations and distillation, not RAC geometry.
- **Rating:** **YELLOW** — foundational closure concept, but different operational task.

### 3. Pawłowski et al., "Information Causality as a Physical Principle" (2009/2010)
- **Citation:** M. Pawłowski et al., *Nature* **461**, 1101–1104 (2009).
- **DOI:** [10.1038/nature08400](https://doi.org/10.1038/nature08400); arXiv:0905.2292.
- **Year:** 2009.
- **Relevant result:** Proposes **Information Causality (IC)**: the total information Bob can gain about Alice's N bits cannot exceed the m classical bits she sends, even with nonlocal resources. Uses RACs to derive Tsirelson's bound for CHSH.
- **Comparison:** Uses RACs and derives Tsirelson's bound, but:
  - IC is a **global information bound** (\(\sum I(X_i : \beta | b=i) \le m\)), not a composition-of-two-copies argument;
  - No explicit classical cut between two resource uses;
  - No multiplication of biases or reinterpretation as a classical one-bit RAC.
- **Rating:** **YELLOW** — derives quantum bound from RAC + classical communication constraint, but via different logical route.

### 4. Botteron et al., "Algebra of Nonlocal Boxes and the Wiring..." (2024)
- **Citation:** P. Botteron, A. Broadbent, R. Chhaibi, I. Nechita, and C. Pellegrini, *Quantum* **8**, 1402 (2024).
- **DOI:** [10.22331/q-2024-07-10-1402](https://doi.org/10.22331/q-2024-07-10-1402); arXiv:2312.00725.
- **Year:** 2024.
- **Relevant result:** Develops an **algebraic framework** for wiring nonlocal boxes, defining a product \(P \boxtimes_W Q\). Studies closure under wirings and orbits of boxes.
- **Comparison:** Most sophisticated treatment of wiring algebra to date, but:
  - No RAC formulation or retrieval biases \(c_i\);
  - No derivation of \(c_1^2 + c_2^2 \le 1\) from classical RAC bound;
  - Focus is on CHSH distillation and communication complexity collapse.
- **Rating:** **YELLOW** — advanced wiring formalism, but different task and no quadratic RAC bound.

### 5. Dmello, Ligthart & Gross, "Entanglement-swapping in GPTs, and iterated CHSH games" (2024)
- **Citation:** L. J. Dmello, L. T. Ligthart, and D. Gross, *Phys. Rev. A* **110**, 022225 (2024).
- **DOI:** [10.1103/PhysRevA.110.022225](https://doi.org/10.1103/PhysRevA.110.022225); arXiv:2405.13819.
- **Year:** 2024.
- **Relevant result:** Studies **iterated CHSH games** with entanglement swapping in GPTs. Asks whether quantum theory is optimal for preserving nonclassical correlations under composition.
- **Comparison:** Addresses composition of correlations in GPTs, but:
  - Uses CHSH games, not RACs;
  - No classical cut or bias multiplication;
  - No derivation of Euclidean RAC boundary.
- **Rating:** **YELLOW** — composition in GPTs, but different task.

### 6. Short & Barrett, "Strong nonlocality: A trade-off between states and measurements" (2010)
- **Citation:** A. J. Short and J. Barrett, *New J. Phys.* **12**, 033027 (2010).
- **DOI:** [10.1088/1367-2630/12/3/033027](https://doi.org/10.1088/1367-2630/12/3/033027); arXiv:0909.2601.
- **Year:** 2010.
- **Relevant result:** Shows a trade-off in GPTs: stronger nonlocal states require more restricted measurements. Discusses implications for Tsirelson's bound.
- **Comparison:** Conceptual background on state-measurement tension, but:
  - No RAC, no bias multiplication, no classical cut.
- **Rating:** **GREEN** — background only.

### 7. Beigi, Gohari et al. on maximal correlation and hypercontractivity (various, 2013–2020)
- **Representative citation:** S. Beigi and A. Gohari, "Monotones for nonlocal correlations," *IEEE Trans. Inf. Theory* (various).
- **Relevant result:** Studies **maximal correlation**, **hypercontractivity ribbons**, and data-processing inequalities for nonlocal boxes.
- **Comparison:** Mathematical tools (maximal correlation, contraction coefficients) are related to bias multiplication, but:
  - No RAC formulation;
  - No derivation of \(c_1^2 + c_2^2 \le 1\) from classical RAC bound.
- **Rating:** **YELLOW** — related mathematical machinery.

### 8. Uffink, "Quadratic Bell inequalities" (2002)
- **Citation:** J. Uffink, *Phys. Rev. Lett.* **88**, 230406 (2002).
- **DOI:** [10.1103/PhysRevLett.88.230406](https://doi.org/10.1103/PhysRevLett.88.230406).
- **Year:** 2002.
- **Relevant result:** Derives quadratic Bell inequalities of the form \((E_{00} + E_{10})^2 + (E_{01} - E_{11})^2 \le 4\).
- **Comparison:** Quadratic form similar to RAC circle, but:
  - Derived from different principles (not composition + classical bound);
  - No RAC or classical cut.
- **Rating:** **GREEN** — mathematical similarity only.

### 9. Toner & Verstraete, "Monogamy of Bell correlations and Tsirelson's bound" (2006)
- **Citation:** B. Toner and F. Verstraete, *arXiv:quant-ph/0611001* (2006).
- **Relevant result:** Relates Tsirelson's bound to monogamy of correlations.
- **Comparison:** Conceptual background, no RAC or composition argument.
- **Rating:** **GREEN**.

### 10. Masanes & Müller, "A derivation of quantum theory from physical requirements" (2011)
- **Citation:** L. Masanes and M. P. Müller, *New J. Phys.* **13**, 063001 (2011).
- **DOI:** [10.1088/1367-2630/13/6/063001](https://doi.org/10.1088/1367-2630/13/6/063001).
- **Year:** 2011.
- **Relevant result:** Derives quantum theory from physical axioms including continuity and reversibility.
- **Comparison:** High-level derivation of quantum bounds, but no RAC composition argument.
- **Rating:** **GREEN**.

### 11. Weilenmann & Colbeck, work on adaptive CHSH / entanglement swapping (2017–2024)
- **Representative:** S. Weilenmann and R. Colbeck, *Phys. Rev. A* **95**, 052106 (2017).
- **Relevant result:** Studies adaptive CHSH games and entanglement swapping in GPTs.
- **Comparison:** Composition of correlations, but no RAC or classical-cut argument.
- **Rating:** **GREEN**.

### 12. Ibnouhsein & Grinbaum, "Causality games and maximal correlation" (various)
- **Relevant result:** Explores causality principles and maximal correlation in information-theoretic derivations of quantum bounds.
- **Comparison:** Conceptual background, no RAC composition.
- **Rating:** **GREEN**.

### 13. Navascués & Wunderlich, "Closed sets of quantum correlations" (2009)
- **Citation:** M. Navascués and H. Wunderlich, *arXiv:0907.0372* (2009).
- **Relevant result:** Shows that the set \(Q_1\) (first level of NPA hierarchy) is closed under wirings.
- **Comparison:** Closure under wirings, but no RAC or bias multiplication.
- **Rating:** **GREEN**.

### 14. Brunner & Skrzypczyk, "Nonlocality distillation" (2009)
- **Citation:** N. Brunner and P. Skrzypczyk, *Phys. Rev. Lett.* **102**, 160403 (2009).
- **DOI:** [10.1103/PhysRevLett.102.160403](https://doi.org/10.1103/PhysRevLett.102.160403).
- **Year:** 2009.
- **Relevant result:** Introduces adaptive wiring protocols to distill nonlocality from noisy boxes.
- **Comparison:** Uses wirings, but for distillation, not RAC consistency.
- **Rating:** **GREEN**.

### 15. Forster, Winkler & Wolf, "Nonlocality distillation" (2009)
- **Citation:** M. Forster, S. Winkler, and S. Wolf, *Phys. Rev. Lett.* **102**, 120401 (2009).
- **DOI:** [10.1103/PhysRevLett.102.120401](https://doi.org/10.1103/PhysRevLett.102.120401).
- **Year:** 2009.
- **Relevant result:** First nonlocality distillation protocol.
- **Comparison:** Background on wirings.
- **Rating:** **GREEN**.

### 16. van Dam, "Implausible consequences of superstrong nonlocality" (2005)
- **Citation:** W. van Dam, *arXiv:quant-ph/0501159* (2005).
- **Relevant result:** Shows that PR boxes collapse communication complexity.
- **Comparison:** Background on why post-quantum correlations are problematic.
- **Rating:** **GREEN**.

### 17. Brassard et al., "Limit on nonlocality" (2006)
- **Citation:** G. Brassard, H. Buhrman, N. Linden, A. Méthot, A. Broadbent, and A. Tapp, *Phys. Rev. Lett.* **96**, 250401 (2006).
- **DOI:** [10.1103/PhysRevLett.96.250401](https://doi.org/10.1103/PhysRevLett.96.250401).
- **Year:** 2006.
- **Relevant result:** Links nonlocality to communication complexity.
- **Comparison:** Background.
- **Rating:** **GREEN**.

### 18. Linden et al., "No advantage for nonlocal computation" (2007)
- **Citation:** N. Linden, S. Popescu, A. J. Short, and A. Winter, *Phys. Rev. Lett.* **99**, 180502 (2007).
- **DOI:** [10.1103/PhysRevLett.99.180502](https://doi.org/10.1103/PhysRevLett.99.180502).
- **Year:** 2007.
- **Relevant result:** Proposes "no advantage for nonlocal computation" principle.
- **Comparison:** Background.
- **Rating:** **GREEN**.

### 19. Carmeli, Heinosaari & Toigo, "Quantum RACs and incompatibility" (various)
- **Relevant result:** Links RAC performance to measurement incompatibility.
- **Comparison:** RAC-focused, but no composition argument.
- **Rating:** **GREEN**.

### 20. Recent work on "Information Causality without concatenation" (2022)
- **Citation:** Quantera project slides, "Information Causality without concatenation" (2022).
- **Relevant result:** Discusses IC bounds without explicit concatenation.
- **Comparison:** Confirms IC literature does not use your construction.
- **Rating:** **GREEN**.

***

## Detailed Comparison of the 5 Closest Papers

| Criterion | Candidate construction | Pawłowski & Żukowski (2010) [EARAC] | Allcock et al. (2009) [Closure] | Pawłowski et al. (2009) [IC] | Botteron et al. (2024) [Box algebra] |
|-----------|----------------------|-------------------------------------|--------------------------------|------------------------------|-------------------------------------|
| Uses 2→1 RAC or equivalent | **Yes** | **Yes** (EARACs) | No (CHSH boxes) | **Yes** (RACs in IC) | No (CHSH boxes) |
| Two separate retrieval biases \(c_1, c_2\) | **Yes** | No (single success probability p) | No (CHSH correlators) | No (mutual information sum) | No (CHSH correlators) |
| Two independent copies/stages | **Yes** | **Yes** (concatenation) | **Yes** (wirings of multiple boxes) | No (single RAC instance) | **Yes** (wirings of two boxes) |
| Biases multiply under composition (\(d_i = c_i^2\)) | **Yes** | No (concatenation improves p, no bias multiplication) | No (wirings change CHSH value, not bias squares) | No | No (wirings change CHSH, no \(c_i^2\)) |
| Intermediate system explicitly classicalized | **Yes** | **Yes** (classical outputs at each stage) | **Yes** (wirings are classical) | No (no intermediate stage) | **Yes** (wirings are classical) |
| No coherent quantum degree crosses interface | **Yes** | **Yes** | **Yes** | N/A | **Yes** |
| Second resource processes classical record | **Yes** | **Yes** (second EARAC uses classical output of first) | **Yes** (second box uses classical output of first) | N/A | **Yes** |
| Final object interpreted as classical 1-bit RAC | **Yes** | No (final object is still an EARAC) | No (final object is a wired box) | No (IC bound on mutual information) | No (final object is a wired box) |
| Classical one-bit bound applied after composition | **Yes** (\(|d_1| + |d_2| \le 1\)) | No | No | No (IC bound is different) | No |
| Produces \(c_1^2 + c_2^2 \le 1\) | **Yes** | No | No | No (derives Tsirelson via IC, not this route) | No |
| Presented as closure/consistency principle | **Yes** | No (concatenation for performance) | **Yes** (closure under wirings) | **Yes** (IC as physical principle) | **Yes** (closure under wirings) |

**Summary:** None of the five closest papers implements all criteria. The EARAC paper (Pawłowski & Żukowski) is closest in using concatenation with classical interfaces, but it does not derive the quantum circle from a classical bound. Allcock et al. and Botteron et al. develop closure under wirings, but for CHSH-type correlations, not RACs. Information Causality derives Tsirelson's bound from RACs, but via a global information constraint, not composition of two copies.

***

## What Is Definitely Not Novel

The following ingredients are **well established** in the literature and should not be claimed as new:

1. **Multiplication of independent binary biases** under concatenation or wiring of classical channels (standard in information theory; e.g., composition of binary symmetric channels).
2. **Quadratic Bell inequalities** such as Uffink's inequality \((E_{00} + E_{10})^2 + (E_{01} - E_{11})^2 \le 4\).
3. **Closure under wirings** as a consistency requirement for physical correlation sets (Allcock et al. 2009; Botteron et al. 2024).
4. **Concatenation of RACs/EARACs** to build larger codes from primitive ones (Pawłowski & Żukowski 2010).
5. **Derivation of Tsirelson's bound from RACs** via Information Causality (Pawłowski et al. 2009).
6. **Maximal correlation and hypercontractivity** as tools for bounding correlations under data processing (Beigi, Gohari, et al.).
7. **Iterated CHSH games** and entanglement swapping in GPTs (Dmello et al. 2024; Weilenmann & Colbeck).

***

## What May Still Be Novel

The following aspects appear **novel** based on the search:

1. **The specific logical chain**: starting from a physical RAC resource with biases \((c_1, c_2)\), using two independent copies with an explicit classical cut, obtaining \(d_i = c_i^2\), reinterpreting the result as a classical one-bit RAC, and applying \(|d_1| + |d_2| \le 1\) to recover \(c_1^2 + c_2^2 \le 1\).
2. **Interpretation of the quantum RAC circle** as a **consistency/closure boundary** arising from classical communication constraints after composition, rather than from Information Causality, monogamy, or uncertainty principles.
3. **Framing the argument** as a "classicalization-and-recomposition" test for admissible physical correlations in the 2→1 RAC scenario.

***

## Suggested Scientifically Defensible Wording

For a blog post, article, or paper, you could responsibly state:

> "We have not found this particular RAC-space construction in the literature. The individual ingredients—concatenation of random access codes, closure under classical wirings, and quadratic bounds on correlations—are well known. However, we have not found them combined in the form presented here: using two independent copies of a binary RAC resource with an explicit classical intermediate interface, multiplying retrieval biases, and recovering the quantum circle \(c_1^2 + c_2^2 \le 1\) as a consistency requirement from the classical one-bit bound."

Or, more cautiously:

> "To the best of our knowledge, this operational derivation of the 2→1 quantum RAC boundary has not appeared previously. While related ideas exist in the literature on Information Causality, closure under wirings, and concatenated RACs, the specific combination of a classical cut between two resource uses and the reinterpretation of the composed object as a classical RAC appears novel."

***

## Search Log

**Databases/sources searched:**
- arXiv (quant-ph, cs.IT, math-ph)
- Google Scholar
- APS Journals (Phys. Rev. A, Phys. Rev. Lett.)
- Quantum Journal
- IOP Science (New J. Phys., J. Phys. A)
- Wikipedia (for background checks)

**Key search queries (and variants):**
- "concatenated random access codes bias multiplication"
- "random access code composition classical interface"
- "nonlocal box wiring closure classical cut"
- "maximal correlation nonlocal boxes wiring sum of squares"
- "strong data processing binary channel composition correlation"
- "Information Causality random access code Tsirelson bound"
- "closure under wirings quantum correlations Euclidean bound"
- "iterated CHSH entanglement swapping GPT classical interface"
- "adaptive CHSH composition classical communication"
- "parity-oblivious multiplexing concatenation bias"
- "Dmello Gross entanglement swapping GPT 2024 2026"
- "classicalization GPT correlation composition"
- "two independent copies nonlocal box classical wiring"
- "hypercontractivity ribbon nonlocal correlations wiring"
- "network principle quantum correlations composition RAC"
- "two independent copies nonlocal box classical wiring RAC"
- "classical intermediate random access code concatenation"
- "sum of squares correlation wiring nonlocal box"
- "maximal correlation binary channel composition square"
- "closure under wirings Euclidean bound correlation"

**Citation chains followed:**
- From Pawłowski & Żukowski (2009) on EARACs → checked references and citing papers for concatenation details.
- From Allcock et al. (2009) on closure → followed citations to Botteron et al. (2024), Navascués & Wunderlich (2009), and subsequent work on wirings.
- From Pawłowski et al. (2009) on Information Causality → checked follow-ups on IC without concatenation, extended IC, and recent bounds.
- From Dmello et al. (2024) on iterated CHSH → checked Weilenmann & Colbeck, Gross group publications.
- From Beigi & Gohari on maximal correlation → checked hypercontractivity and data-processing literature.

**Gaps/limitations:**
- Some very recent 2025–2026 preprints may not yet be indexed or fully searchable.
- Thesis-level work (e.g., Pierre Botteron's M.Sc. thesis) was partially accessed but may contain additional details not in the journal version.
- Non-English literature (e.g., Russian, Chinese) was not systematically searched.

***

## Remaining Risk

The main risks that prior art could still exist are:

1. **Unpublished or obscure preprints** (2025–2026) that use non-standard terminology (e.g., "classical interface," "bias squaring," "RAC consistency") and have not yet been widely cited.
2. **Thesis or workshop proceedings** that discuss similar constructions but are not indexed in major databases.
3. **Equivalent formulations in different language**: the argument might appear in terms of "correlation tensors," "hypercontractivity ribbons," or "data-processing inequalities" without explicit RAC language.
4. **Implicit use in GPT dynamics literature**: some works on GPT composition (e.g., Dmello & Gross 2024, Weilenmann & Colbeck) might contain mathematically equivalent arguments in a different operational guise (e.g., "stability under teleportation" or "classical subsystems").

**Recommendation:** Before claiming novelty in a publication, consider:
- Directly checking the arXiv submissions from the Gross, Colbeck, Barrett, and Pawłowski groups from 2024–2026.
- Searching for phrases like "classical cut," "classical interface," "bias multiplication," and "consistency boundary" in combination with "RAC" or "random access code."
- If possible, asking experts in the field (e.g., Marcin Pawłowski, David Gross, Jonathan Barrett) whether they recognize the construction.

***

**Bottom line:** Your construction appears **likely novel** as a specific operational argument, even though all its mathematical components are known. The closest prior work (EARAC concatenation, closure under wirings, Information Causality) shares ingredients but does not implement the full logical chain you describe.