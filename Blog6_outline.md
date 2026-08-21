# Feats and Failures of the Superphoton

### *What happens if we make photons more correlated than quantum mechanics allows, while trying to leave everything else unchanged?*

<!--
ROLE

This is the first post after the RAC sequence.

Blog 5 ended with:
"A correlation point is not yet a physical theory."

Now actually test that statement.

Use the author's previously defined 'superphotons' rather than abstract PR boxes wherever possible.

Scientific discipline:
- Our negative-probability calculation is a gedankenexperiment for ONE natural completion of the superphoton model.
- Short & Barrett is the rigorous Boxworld result.
- Dmello 2024/2026 prevents us from claiming that every post-quantum theory must fail in the same way.
-->

## One-Sentence Spine

**Turning up a pair's correlations is easy on paper; the trouble begins when we insist that the same particles should still support the joint measurements that ordinary quantum particles do.**

---

# Opening — We Invented Superphotons. Did We Invent a Theory?

<!-- Goal: reconnect to the old superphoton article in <200 words. -->

Previously, we imagined 'superphotons'.

Individually they behave like ordinary photons.

Alice can rotate her polarizer.

Bob can rotate his.

Each local result remains random.

The only thing we change is the correlation between the two photons: as the parameter (q) increases, their outcomes become more strongly coordinated than quantum mechanics permits.

At the quantum value we recover the familiar photon correlation curve.

Push (q) farther and we approach PR-box-like behaviour.

Nothing immediately goes wrong.

The probabilities seen by Alice and Bob remain between zero and one.

No faster-than-light signalling appears.

So perhaps we have invented a perfectly sensible photon that is simply *more quantum* than a quantum photon.

But have we?

A correlation curve tells us what happens when the particles are measured separately.

A physical theory must also tell us what happens when we bring systems together and measure them jointly.

That is where things become interesting.

**Pull quote**

> **A stronger correlation curve is not yet a stronger physical theory.**

### Figure 1 — The Superphoton Family

Use the existing probability-versus-angle plot.

Show several (q) values:

* ordinary quantum photon;
* modestly supraquantum;
* strongly supraquantum / PR-like limit.

This is the right home for the existing Superphotons.png image.

**Caption:**
*Our 'superphotons' change only the correlation law between the two particles. Locally, each photon is still supposed to behave normally.*

---

# 1. What Are We Keeping Fixed?

<!--
This section is vital.
The reader must know that the contradiction depends on assumptions.
-->

To turn the correlation model into a gedankenexperiment, make the smallest possible change to ordinary photon physics.

Assume:

1. **Local photon behaviour remains quantum-like.**
   A single superphoton can still be rotated through arbitrary polarization transformations.

2. **Separated measurements follow the stronger (q)-correlation law.**

3. **The strengthened correlation law extends consistently to the measurement directions needed in the experiment.**

Then ask whether we can also retain:

4. **The ordinary quantum Bell-state measurement on two photons.**

We are not assuming that Nature must satisfy all four.

We are testing whether they can coexist.

That distinction needs to remain explicit throughout the post.

---

# 2. The Measurement Ordinary Photons Can Perform

<!-- Goal: explain Bell measurement physically before algebra. -->

Take two ordinary photons and bring them into the same laboratory.

Quantum mechanics allows genuinely joint questions that cannot be reduced to asking each photon a separate question.

The Bell measurement is the canonical example.

One possible outcome asks whether the two photons occupy the Bell state

[
|\Phi^+\rangle.
]

For ordinary photons, the probability of this outcome can be written in terms of three familiar correlation measurements:

[
p_{\Phi^+}
==========

\frac14
\left(
1+E_{XX}-E_{YY}+E_{ZZ}
\right).
]

For every allowed quantum state,

[
0\le p_{\Phi^+}\le1.
]

So far, nothing surprising.

Now try the same detector on our superphotons.

### Figure 2 — The Bell Question

A simple schematic:

two incoming superphotons → Bell-measurement box → four possible Bell outcomes.

Do not introduce Boxworld yet.

**Caption:**
*Ordinary photons support a joint Bell measurement. We now ask whether the same measurement can still exist after we strengthen the pair correlations.*

---

# 3. Rotate One Photon Until Quantum Mechanics Sits on the Edge

<!-- Goal: construct the clean boundary case. -->

Choose an ordinary local polarization rotation for one photon such that the relevant quantum correlations become

[
E_{XX}=-\frac13,\qquad
E_{YY}=+\frac13,\qquad
E_{ZZ}=-\frac13.
]

For ordinary quantum photons,

[
p_{\Phi^+}
==========

\frac14
\left(
1-\frac13-\frac13-\frac13
\right)
=0.
]

So quantum mechanics sits exactly at the boundary.

The Bell outcome is possible in principle, but for this particular state it never occurs.

Nothing is negative.

Nothing is inconsistent.

Now increase the correlation strength.

---

# 4. Turn On the Superphoton

For the specific (q)-deformation used for our superphotons, the magnitude

[
\frac13
]

is strengthened to

[
a_q=\left(\frac13\right)^{1/q}.
]

For (q=1),

[
a_q=\frac13.
]

For every (q>1),

[
a_q>\frac13.
]

The same Bell measurement would therefore predict

[
p_{\Phi^+}
==========

\frac{1-3a_q}{4}.
]

At (q=1),

[
p_{\Phi^+}=0.
]

But as soon as

[
q>1,
]

we obtain

[
\boxed{p_{\Phi^+}<0.}
]

That is not a strange experimental outcome.

It means the proposed Bell measurement cannot be a valid measurement for this enlarged set of states.

### Figure 3 — Where the Probability Goes Negative

Prefer a simple graph over a probability table.

Horizontal axis: (q).

Vertical axis:

[
p_{\Phi^+}(q).
]

Mark:

* (q=1,\ p=0);
* negative region for (q>1).

A small inset can show the three strengthened correlations.

**Caption:**
*Quantum mechanics sits exactly at zero for this Bell outcome. Strengthen the correlations while keeping the same local rotations and Bell measurement, and the predicted probability immediately becomes negative.*

**Pull quote**

> **The first thing to break is not relativity. It is the measurement itself.**

---

# 5. So What Has Actually Failed?

This experiment does **not** prove that stronger-than-quantum particles cannot exist.

It proves something narrower.

We tried to retain simultaneously:

* stronger-than-quantum pair correlations;
* ordinary local polarization transformations;
* the ordinary quantum Bell measurement.

For this particular superphoton completion, those assumptions are inconsistent.

Something must change.

Perhaps the correlation law is impossible.

Perhaps some local transformations disappear.

Or perhaps the Bell measurement no longer exists.

That last possibility sounds peculiar from a quantum perspective.

But there is a well-studied theory where exactly this happens.

---

# 6. Boxworld — The Extreme Version of the Failure

<!--
Now introduce Short & Barrett.
Keep the formalism minimal but accurate.
-->

Boxworld permits the full set of no-signalling correlations, including PR boxes.

Its states can therefore be more strongly nonlocal than quantum states.

But Short and Barrett showed that its joint measurements are correspondingly restricted.

Every allowed Boxworld effect is separable.

There is no analogue of the quantum Bell measurement.

Consequently, standard Boxworld has:

* no entanglement swapping;
* no teleportation;
* no dense coding.

The intuitive reason is not that Boxworld probabilities become negative.

The opposite happens.

When effects are represented relative to local fiducial measurements, every allowed Boxworld effect can be written with non-negative coefficients and decomposed into a sum of product effects.

The negative coefficients needed to reconstruct genuinely entangled quantum effects are no longer available.

Our superphoton gedankenexperiment therefore resembles the Boxworld story:

> expand the allowed correlations far enough, and a familiar quantum joint measurement can cease to be compatible with the enlarged state space.

But our calculation is an illustration.

Short and Barrett's result is a theorem for standard Boxworld.

### Figure 4 — More States, Fewer Familiar Measurements

Keep this operational rather than formal.

Left:
ordinary quantum photons:

* Bell correlations;
* Bell measurement available.

Right:
Boxworld extreme:

* stronger PR correlations;
* Bell measurement crossed out.

Avoid saying universally “stronger correlations = fewer measurements.”

Caption it explicitly as **the Boxworld trade-off**.

**Caption:**
*Standard Boxworld admits stronger states than quantum mechanics, but not the Bell-like joint measurements needed for teleportation and entanglement swapping.*

---

# 7. Then 2024–2026 Complicated the Story

<!--
This is what prevents the article from simply repeating a 2010 narrative.
-->

At this point it is tempting to conclude:

> Nature stops at the quantum boundary because anything stronger would lose Bell measurements and useful dynamics.

That conclusion is too strong.

Recent generalized-probabilistic-theory results show that Boxworld is not the only way to build a post-quantum theory.

Dmello, Ligthart and Gross constructed a GPT that can sustain the algebraic maximum

[
\text{CHSH}=4
]

through arbitrarily many rounds of entanglement swapping.

Dmello and Gross subsequently classified GPTs with this kind of stability and found several possibilities.

So:

[
\text{stronger than quantum}
\not\Rightarrow
\text{no entangled measurements}.
]

And even standard Boxworld has acquired a new twist.

Umekawa and collaborators showed in 2026 that if we relax **reversibility**, pure-state-preserving transformations can generate PR-box entanglement from product states.

The old reversible no-go still stands.

But “Boxworld has no interesting entangling dynamics whatsoever” no longer does.

This makes the lesson more interesting, not less.

---

# 8. A Correlation Curve Is Not a Theory

<!-- Goal: broad conceptual conclusion, but leave question open. -->

Our superphotons started life as a very simple idea:

> keep the photons, change the correlation curve.

That is enough to define a Bell-type experiment between distant observers.

It is not enough to define a world.

Once we ask what happens when two superphotons meet, we also have to specify:

* their joint states;
* their allowed joint measurements;
* their local transformations;
* their reversible and irreversible dynamics;
* and how larger systems compose.

Change one part of the structure and the others may have to change with it.

Quantum mechanics is remarkable not simply because its correlations stop at

[
2\sqrt2.
]

It is remarkable because one mathematical structure simultaneously gives us those correlations, continuous local transformations, incompatible measurements, entangled measurements, teleportation, swapping, and a consistent theory of composite systems.

Could some other theory give us all of those features while going farther?

Recent work says the answer is not obviously no.

And that leaves the question open again.

### Closing line

**Perhaps the interesting question is no longer why superphotons are impossible, but what a complete and internally consistent superphoton theory would actually have to look like.**

---

# Suggested References

1. S. Popescu and D. Rohrlich, *Quantum Nonlocality as an Axiom* (1994).
2. V. Scarani, *Feats, Features and Failures of the PR-box* (2006).
3. J. Barrett, *Information processing in generalized probabilistic theories* (2006/2007).
4. A. J. Short and J. Barrett, *Strong nonlocality: A trade-off between states and measurements* (2010).
5. D. Gross et al., *All reversible dynamics in maximally non-local theories are trivial* (2010).
6. L. J. Dmello, L. T. Ligthart and D. Gross, *Entanglement-swapping in generalised probabilistic theories, and iterated CHSH games* (2024).
7. L. J. Dmello and D. Gross, *Probabilistic theories stable under teleportation* (2026).
8. S. Umekawa et al., *Entanglement Generation Beyond Quantum Theory: From Product States to Popescu–Rohrlich Boxes* (2026).

---

# Figure Set

1. **Existing superphoton angle curves.**
2. **Bell-measurement setup.**
3. **Negative Bell-outcome probability versus (q).**
4. **Quantum versus Boxworld joint-measurement capability.**

Optional fifth figure only if needed:
a small network diagram illustrating entanglement swapping before the 2024–26 twist.

---

# Important Scientific Caveat

Before publication, independently verify the negative-probability calculation against the precise superphoton correlation law used in the earlier article.

The article must say explicitly that the calculation assumes a particular extension of that correlation law to the set of measurement directions required by the Bell experiment.

Do not present the calculation as Short & Barrett's theorem.

Present the sequence as:

**our superphoton gedankenexperiment → negative probability for this completion → Short & Barrett as rigorous Boxworld analogue → recent GPT results as counterexample to any universal interpretation.**
