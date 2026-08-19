# Blog 5 Working Outline — Why Does Quantum Advantage Stop at a Circle?

### *A classical bottleneck, richer quantum questions, and a surprisingly natural boundary in advantage space.*

<!--
STATUS: Concept/outline document, not publication-ready prose.

CENTRAL DISCIPLINE:
Stay in RAC advantage space. Do NOT claim that the argument derives quantum
mechanics, Hilbert space, the Born rule, or the full quantum correlation set.
The claim to explore is narrower:

For the 2→1 RAC, a simple classicalization-and-recomposition construction
naturally singles out c₁²+c₂²≤1 as a consistency boundary in RAC advantage
space. Quantum mechanics happens to reach/saturate this boundary.

Throughout, explicitly distinguish:
1. established literature;
2. exact RAC-space mathematics;
3. our interpretation/speculation.
-->

---

## One-Sentence Spine

**Why does Nature's RAC advantage stop at the quantum circle? Perhaps because the circle is exactly strong enough to survive rich quantum processing, yet weak enough that once its information is deliberately classicalized and recomposed, it falls back onto the classical one-bit RAC boundary.**

---

## Working Title

# Why Does Quantum Advantage Stop at a Circle?

### *A classical bottleneck, richer quantum questions, and a surprisingly natural boundary in advantage space.*

Alternative titles:

- **What Breaks Beyond the Quantum Circle?**
- **Why Can’t Quantum Advantage Go Any Further?**
- **The Strange Boundary of Quantum Advantage**
- **A Surprisingly Simple Reason for the Quantum Circle**
- **The Circle Between Too Classical and Too Powerful**

The first title is probably the best combination of curiosity, visual connection to the previous posts, and scientific caution.

---

# 1. Opening — We Know the Shape. But Why That Shape?

<!-- GOAL:
Reconnect to the geometry series in less than a page.
Do not start with GPT formalism or Information Causality.
Start with the reader's visual puzzle.
-->

The previous posts built an advantage space for a random-access guessing game. For two requested bits, write

\[
c_i = 2P_i-1,
\]

so \(c_i=0\) means Bob is guessing randomly and \(c_i=1\) means he recovers bit \(i\) perfectly.

Three geometries then appear naturally:

- classical one-bit strategies form a diamond;
- quantum-assisted strategies reach a circle;
- a hypothetical perfect random-access resource would fill the surrounding square.

In the positive quadrant,

\[
\text{classical:}\qquad c_1+c_2\le1,
\]

while the quantum construction reaches

\[
\text{quantum:}\qquad c_1^2+c_2^2\le1.
\]

The obvious question is no longer whether quantum mechanics beats the classical game. It does.

The question is:

> **Why does Nature stop at the circle? Why not allow correlations that bulge a little farther toward the square?**

A PR box shows that no-signalling alone does not force the quantum circle. Information Causality supplies one famous answer, but as discussed in Blog 4, its direct finite-\(n\) mutual-information shape is not the quantum sphere, and the Tsirelson threshold emerges through a scaling argument.

This post takes a different route. Instead of starting with entropy, start with **what a physical theory allows you to do with its correlations**.

---

# 2. Stronger Correlations Can Come With Weaker Dynamics

<!-- GOAL:
Introduce the "sweet spot" idea as established motivation from GPT literature,
but clearly say that the literature does NOT derive the RAC circle from this.
-->

There is a long-running foundational suspicion that quantum mechanics may occupy a kind of middle ground: its correlations are stronger than classical correlations, but not maximally nonlocal, while its measurements and reversible dynamics are extraordinarily rich.

Generalized probabilistic theories (GPTs) make this comparison concrete. A GPT does not begin by assuming Hilbert space. It specifies operational states, measurements/effects, transformations, and rules for composing systems.

Jonathan Barrett's GPT framework was explicitly motivated in part by the question of why quantum theory does not permit arbitrary no-signalling correlations. In the generalized non-signalling theory usually called **Boxworld**, supraquantum PR-box correlations are available, but much of the dynamics becomes severely restricted. Barrett describes this as a trade-off between the richness of the allowed states and the allowed dynamics [1].

Short and Barrett later made the state-measurement trade-off especially tangible. Boxworld admits stronger-than-quantum entangled states, but its measurements are comparatively poor: there is no analogue of the Bell measurement, and consequently no entanglement swapping, teleportation, or dense coding [2].

Gross, Müller, Colbeck and Dahlsten obtained an equally striking result for reversible dynamics. In maximally nonlocal Boxworld, reversible transformations are essentially only local relabellings and permutations of subsystems. In particular, reversible dynamics cannot generate nonlocal states from product states [3].

Al-Safi and Richens extended the connection between local state-space geometry, nonlocality, and reversible dynamics to broad classes of GPTs. Their results reinforce the idea that demanding rich reversible dynamics places nontrivial restrictions on theories with maximally nonlocal composites [4].

This motivates an attractive question:

> **Is quantum theory somehow an optimal balance between nonlocal correlation strength and dynamical richness?**

That idea is scientifically respectable. But it remains an idea rather than a generally accepted theorem selecting the quantum set.

Recent results make the caveat especially important. Dmello and Gross have classified GPTs whose CHSH strength can remain stable under repeated teleportation/entanglement-swapping-type composition; their classification includes theories that sustain stronger-than-quantum correlations. Thus “stronger than quantum” does **not** generically mean “no useful dynamics” [5]. Likewise, recent work by Umekawa *et al.* shows that even Boxworld's familiar reversible no-go can change substantially if reversibility is weakened to pure-state preservation [6].

So the scientifically safe statement is:

> Quantum theory achieves a remarkable combination of nonlocal correlations, continuous reversible transformations, incompatible measurements, entangled measurements, and network operations. Maximally nonlocal Boxworld sacrifices much of this richness. Whether one deeper principle uniquely selects the quantum balance remains open.

This post will not try to solve that GPT reconstruction problem.

Instead, we stay in **RAC advantage space** and ask what traces — or shadows — of this richer dynamical structure are already visible there.

---

# 3. Advantage Space Is a Shadow, Not the GPT State Space

<!-- GOAL:
Prevent later conceptual overclaiming.
Explain theory -> strategies -> RAC region.
-->

A GPT does not correspond to one point in RAC advantage space. A theory supplies a set of allowed states, measurements and transformations. A particular RAC **strategy** consists of choices such as

\[
(\omega_{AB},\;\text{Alice's measurements},\;\text{encoding rule},
\;\text{Bob's measurements},\;\text{decoding rule}),
\]

and that strategy maps to one advantage vector

\[
(c_1,c_2).
\]

Varying all allowed strategies generates an achievable RAC body,

\[
\text{GPT} \longrightarrow K_{\rm RAC}\subset\mathbb R^2.
\]

This map is highly many-to-one. Different physical states and different measurement implementations may lead to the same RAC point. Conversely, an extreme GPT state need not project to an extreme RAC point.

So the circle drawn in these posts is **not the Bloch sphere** and not the complete quantum state space.

A useful phrase for the series is:

> **The RAC body is the shadow that a physical theory casts onto this particular information-processing task.**

That viewpoint lets us ask a deliberately modest question:

> What properties of quantum dynamics are still visible in the shadow?

---

# 4. A First Shadow of Quantum Dynamics: Bob Can Ask Rotated Questions

<!-- GOAL:
Use the posterior-distribution experiment.
This is a concrete teaching section before the more abstract relay argument.
-->

Consider the standard two-bit quantum-assisted RAC. Alice's data remain an entirely classical string,

\[
x=(x_1,x_2)\in\{00,01,10,11\}.
\]

Alice and Bob share an entangled resource. Alice uses her usual XOR encoding. Bob normally chooses one of two retrieval measurements:

- \(B\): optimized to recover \(x_1\);
- \(B'\): optimized to recover \(x_2\).

At the symmetric quantum point,

\[
c_1=c_2=\frac1{\sqrt2},
\]

Bob recovers the selected bit with

\[
P_{\rm Q}
=
\frac12\left(1+\frac1{\sqrt2}\right)
\approx 85.4\%.
\]

Conditioned on Bob choosing \(B\), his posterior distribution over the four strings strongly separates the value of \(x_1\), while carrying essentially no useful bias about \(x_2\). Choosing \(B'\) rotates that role.

That is the usual RAC story.

But Bob is not forced to measure only \(B\) or \(B'\). Quantum mechanics allows a continuous family of measurement directions between them.

With another measurement direction, the posterior over the same four **classical** strings changes qualitatively. Instead of learning mostly one coordinate, Bob can acquire weaker information about both coordinates at once.

For example, a posterior of the form

\[
P(00,01,10,11)
=
(0.50,0.25,0.25,0)
\]

does not tell Bob either bit perfectly. Instead,

\[
P(x_1=0)=P(x_2=0)=0.75.
\]

It also tells him something about the **Hamming weight**

\[
W=x_1+x_2.
\]

The uniform prior has

\[
P(W=0,1,2)
=
\left(\frac14,\frac12,\frac14\right),
\]

with entropy

\[
H(W)=1.5\text{ bits}.
\]

For the posterior above,

\[
P(W=0,1,2)
=
\left(\frac12,\frac12,0\right),
\]

with entropy

\[
H(W)=1\text{ bit}.
\]

So this measurement has supplied \(0.5\) bits of information about the Hamming weight.

A physically suggestive equivalent variable is **magnetization**. Map

\[
0\mapsto +1,\qquad 1\mapsto -1,
\]

and define

\[
M=(-1)^{x_1}+(-1)^{x_2}.
\]

Then

- \(00\rightarrow M=+2\),
- \(01,10\rightarrow M=0\),
- \(11\rightarrow M=-2\).

Bob's rotated measurement has shifted information away from “which coordinate?” toward a more collective property such as the zero/one imbalance.

This should not be described as Bob literally measuring the classical observable \(x_1+x_2\). He measures a quantum observable, and the resulting outcome induces a posterior over the classical strings that happens to be more informative about their collective weight.

A good blog formulation is:

> **The data are classical, but the menu of questions Bob can ask of his uncertainty carries a shadow of the quantum measurement geometry.**

The standard RAC axes reveal \(x_1\) or \(x_2\). Rotated quantum measurements can redistribute the information toward combinations resembling

\[
z_1+z_2
\quad\text{or}\quad
z_1-z_2,
\qquad
z_i=(-1)^{x_i}.
\]

Parity is different:

\[
x_1\oplus x_2
\quad\leftrightarrow\quad
z_1z_2,
\]

and should not be conflated with magnetization or imbalance.

### Why bring Boxworld in here?

In full Boxworld, the allowed measurements are much more restricted. Short and Barrett show that Boxworld lacks the rich entangled measurement structure available in quantum theory [2]. Barrett and Gross *et al.* similarly show that its transformation structure is much poorer than the continuous quantum one [1,3].

So even though Boxworld has *stronger correlations*, its ability to interrogate and coherently manipulate those correlations is not simply “quantum, but more”.

This is the first hint that the outermost possible advantage region may not be the whole story.

---

# 5. The Circle Is Controlled by Relative Geometry, Not a Reference-Frame Rotation

<!-- GOAL:
Record an important distinction from the exploratory discussion.
Prevents an attractive but wrong angle-addition story.
-->

There is an easy trap here.

For a two-question quantum RAC, Alice may choose two Bloch directions \(a\) and \(a'\). Let their relative angle be \(\delta\). Bob's optimized retrieval biases satisfy

\[
c_1
=
\frac{\|a+a'\|}{2}
=
\cos\frac{\delta}{2},
\]

and

\[
c_2
=
\frac{\|a-a'\|}{2}
=
\sin\frac{\delta}{2}.
\]

Hence

\[
c_1^2+c_2^2=1.
\]

Moving around the RAC circle therefore corresponds to changing the **relative angle between Alice's two observables**.

A common coherent rotation

\[
a\mapsto Ra,\qquad
a'\mapsto Ra'
\]

does not change \(\delta\), because

\[
(Ra)\cdot(Ra')=a\cdot a'.
\]

So an intermediate agent can rotate a reference frame or permute Bob's retrieval axes, but that does not generically reshape Alice's RAC point.

If Alice chooses \(a=a'\), she is at

\[
(c_1,c_2)=(1,0).
\]

A common reversible rotation cannot turn that into

\[
\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
\]

because it cannot manufacture the missing difference \(a-a'\).

This is worth retaining because it sharpens what “dynamics on the RAC body” does and does not mean.

---

# 6. Two Ways Through a Relay

<!-- GOAL:
Bridge dynamics/GPT story to the novel RAC-space composition argument.
-->

Now introduce intermediate agents.

There are two qualitatively different things Charlie can do with a quantum resource.

## 6.1 Preserve the quantum resource

Suppose Alice–Charlie and Charlie–Bob share suitable entanglement. Charlie can use a Bell-type joint measurement to perform entanglement swapping. The quantum correlation is transferred onward rather than converted into a definite classical guess.

Up to classical Pauli-frame information, Alice and Bob can retain the same kind of entangled resource and hence the same RAC capability.

The key conceptual point is:

> Charlie has moved the quantum correlation without first materializing all of Alice's possible answers as ordinary classical bits.

This sort of network operation is available in quantum mechanics. It is not available in standard Boxworld [2], although, as noted above, more general post-quantum GPTs can have richer swapping/teleportation structures [5].

## 6.2 Destroy the quantum resource and keep only classical guesses

Now make Charlie do the opposite.

Instead of preserving the resource, Charlie deliberately **classicalizes** it.

This is where the central thought experiment begins.

---

# 7. The Classicalization Experiment

<!-- GOAL:
This is the central novel/exploratory construction.
Make resource accounting explicit.
Use Charlie and David to create an unambiguous fully classical middle cut.
-->

Let the original two-question RAC resource have advantage vector

\[
c=(c_1,c_2).
\]

We make no quantum assumptions about this resource. It could be classical, quantum, or hypothetical post-quantum.

All we assume is that, when used to retrieve index \(i\), it succeeds with probability

\[
P_i=\frac{1+c_i}{2}.
\]

## Step 1 — Charlie materializes both possible answers

Alice and Charlie use **two independent copies** of the resource.

On the first copy, Charlie chooses index \(1\), giving a classical guess

\[
\hat x_1=x_1\oplus e_1,
\]

with bias \(c_1\).

On the second copy, Charlie chooses index \(2\),

\[
\hat x_2=x_2\oplus e_2,
\]

with bias \(c_2\).

Charlie now holds the ordinary classical pair

\[
(\hat x_1,\hat x_2).
\]

The counterfactual quantum structure has been destroyed. There is no requirement that Charlie preserve a state, a phase, a measurement choice, or a quantum memory.

## Step 2 — Make the middle cut explicitly classical

Charlie sends both classical guesses perfectly to a new agent, David:

\[
(\hat x_1,\hat x_2)
\longrightarrow
\text{David}.
\]

This is deliberately **two bits of classical communication**.

The point of introducing David is conceptual cleanliness. Whatever physical resource Alice and Charlie used has ended. Across the Charlie–David cut there is nothing but the classical random variable

\[
(\hat x_1,\hat x_2).
\]

No entanglement, no quantum memory and no hidden choice of measurement needs to survive that cut.

## Step 3 — David RAC-encodes the noisy pair for Bob

David and Bob now use one fresh copy of the **same type of RAC resource**.

If Bob asks for index \(i\), the second stage retrieves Charlie's classical guess \(\hat x_i\) with the same bias \(c_i\).

So Bob is correct about Alice's original \(x_i\) if:

- Charlie was right and David–Bob was right; or
- Charlie was wrong and David–Bob was wrong.

For one index,

\[
P_i^{AB}
=
P_i^2+(1-P_i)^2.
\]

Using

\[
P_i=\frac{1+c_i}{2},
\]

this becomes

\[
P_i^{AB}
=
\frac12(1+c_i^2).
\]

Therefore the end-to-end advantage is

\[
\boxed{
d_i
=
c_i^{AB}
=
c_i^2.
}
\]

Nothing quantum entered this derivation.

It is simply the algebra of two independent binary errors: zero errors or two errors give the correct answer.

---

# 8. The Surprising Geometry: Squaring the Circle Gives the Classical Diamond

<!-- GOAL:
This is the "reveal".
-->

The coordinatewise composition map is

\[
(c_1,c_2)
\longmapsto
(d_1,d_2)
=
(c_1^2,c_2^2).
\]

Now apply it to the quantum circle,

\[
c_1^2+c_2^2=1.
\]

Immediately,

\[
d_1+d_2=1.
\]

But in the positive quadrant,

\[
d_1+d_2=1
\]

is exactly the classical \(2\to1\) RAC boundary.

So:

\[
\boxed{
\text{quantum circle}
\quad
\xrightarrow{\;c_i\mapsto c_i^2\;}
\quad
\text{classical diamond edge}.
}
\]

This has an elementary operational interpretation.

Any point satisfying

\[
d_1+d_2=1
\]

can be written as

\[
d=d_1(1,0)+d_2(0,1).
\]

It is therefore equivalent, in advantage space, to a stochastic mixture of the two primitive classical strategies:

- transmit bit \(1\) perfectly with probability \(d_1\);
- transmit bit \(2\) perfectly with probability \(d_2\).

The symmetric quantum point gives the simplest example:

\[
c_1=c_2=\frac1{\sqrt2}.
\]

After classicalization and recomposition,

\[
d_1=d_2=\frac12,
\]

so Bob's final success probabilities are

\[
P_1=P_2=\frac34.
\]

Exactly the symmetric classical limit.

At the axis point,

\[
(c_1,c_2)=(1,0),
\]

the map gives

\[
(d_1,d_2)=(1,0),
\]

which is again the corresponding classical axis strategy.

Every point on the positive quantum quarter-circle is transformed into the corresponding point on the positive classical diamond edge.

---

# 9. Now Push Slightly Beyond the Circle

<!-- GOAL:
Formulate the "logical boundary" idea with explicit caution.
-->

Suppose a hypothetical RAC resource allowed

\[
c_1^2+c_2^2>1.
\]

Use exactly the same classicalization experiment.

The end-to-end advantages are still

\[
d_i=c_i^2.
\]

Therefore,

\[
d_1+d_2
=
c_1^2+c_2^2
>
1.
\]

The resulting Alice–Bob point lies **outside the classical diamond**.

For example,

\[
(c_1,c_2)=(0.8,0.8)
\]

would give

\[
(d_1,d_2)=(0.64,0.64),
\]

and hence

\[
d_1+d_2=1.28.
\]

The provocative question is:

> **Should a RAC resource be considered physically reasonable if, after all upstream nonclassical information has been explicitly converted into an ordinary classical pair, recomposition with one fresh copy of the resource pushes the original Alice–Bob relation beyond the classical one-bit RAC boundary?**

The proposed intuition is:

> Once the information crossing the middle cut is entirely classical, the resulting end-to-end classical random-access relation should not exhibit more than the ordinary classical one-bit RAC capability.

If we impose that requirement, then

\[
d_1+d_2\le1
\]

implies

\[
\boxed{
c_1^2+c_2^2\le1.
}
\]

The circle has appeared without Hilbert space, amplitudes, the Born rule, qubits, cosine correlations, or Information Causality.

Only three ingredients were used:

1. two binary questions;
2. independent composition of binary errors;
3. a classicalization/recomposition consistency requirement.

That is the central conceptual result of the post.

---

# 10. What Exactly Are We Claiming?

<!-- GOAL:
Critical scientific hygiene.
This section should stay in the final article, perhaps condensed.
-->

The argument should be presented strongly enough to be interesting, but narrowly enough to remain scientifically defensible.

## We *are* claiming

Within two-dimensional RAC advantage space:

\[
(c_1,c_2)
\mapsto
(c_1^2,c_2^2)
\]

is the natural map produced by two independent uses of a binary guessing resource when the intermediate answers have been explicitly classicalized.

Demanding that the resulting point respect the classical two-question RAC boundary gives

\[
c_1^2+c_2^2\le1.
\]

Quantum mechanics reaches exactly this circle.

This makes the circle a natural **composition boundary**, **classicalization boundary**, or **logical consistency boundary** in RAC advantage space.

## We are *not* claiming

We are not deriving:

- Hilbert space;
- the Born rule;
- the quantum state space;
- Tsirelson's theorem in full generality;
- the complete set of quantum correlations;
- a unique GPT;
- or an explanation of why Nature must be quantum.

A post-quantum theory could conceivably project onto the same RAC circle while differing radically from quantum mechanics elsewhere.

Conversely, a GPT might have stronger-than-quantum behaviour in another operational scenario while still obeying this particular RAC-space constraint.

The appropriate claim is therefore:

> **The Euclidean circle is a natural boundary internal to the logic of this two-question RAC geometry, and quantum theory happens to saturate it.**

That is already interesting.

---

# 11. Why the Two-Bit Case Is Special

<!-- GOAL:
Preempt obvious higher-n objection.
-->

For a general \(n\)-question sphere,

\[
\sum_i c_i^2=1,
\]

the same coordinatewise square gives

\[
d_i=c_i^2
\]

and therefore

\[
\sum_i d_i=1.
\]

Geometrically, the sphere maps onto the simplex spanned by the axis strategies

\[
(1,0,\ldots,0),\;
(0,1,\ldots,0),\ldots.
\]

Operationally, this is the family of classical strategies obtained by stochastically choosing one index \(i\) with probability \(d_i\) and transmitting that bit perfectly.

For \(n=2\), that simplex edge **is the full positive classical RAC boundary**.

For higher \(n\), it is not.

Majority-type encodings exploit the structure of many bits and push the true classical RAC polytope beyond the axis simplex.

Thus the classicalization argument is beautifully sharp for \(n=2\), but increasingly conservative in higher dimensions:

\[
\text{squared sphere}
\rightarrow
\text{axis simplex}
\subset
\text{full classical RAC body}.
\]

That does not weaken the two-question result. It clarifies why two questions are the cleanest laboratory for the principle.

---

# 12. A Possible Principle: Stability Under Classicalization and Recomposition

<!-- GOAL:
Give a memorable name but label it explicitly as exploratory.
-->

A compact way to state the exploratory principle is:

> **Classicalization consistency:** If a nonclassical random-access resource is used to turn all of its possible answers into an ordinary classical random variable, then recomposing that variable with another copy of the resource should not create an effective classical RAC outside the classical communication boundary.

For the two-question binary RAC, this becomes

\[
\boxed{
\text{classicalization consistency}
\quad\Longrightarrow\quad
\|c\|_2\le1.
}
\]

Possible alternative names:

- **classical bottleneck consistency**
- **classicalization closure**
- **RAC composition consistency**
- **classical-cut stability**
- **measure-and-recompose principle**

Do not settle on a formal name before checking the literature for closely related concepts.

A particularly concise reader-facing formulation is:

> **If you destroy the quantum part in the middle, nothing stronger than a classical RAC should come out the other end.**

The mathematics says that this intuitive statement singles out the circle for two questions.

---

# 13. How This Complements Information Causality

<!-- GOAL:
Connect Blog 5 to Blog 4 without repeating it.
-->

Information Causality and the present argument attack the same visual mystery from almost opposite directions.

Information Causality constrains the sum of potentially accessible mutual informations,

\[
\sum_i I(x_i:\beta_i)\le m,
\]

and in the familiar concatenated RAC construction, any isotropic correlation strength beyond

\[
E=\frac1{\sqrt2}
\]

eventually violates the information budget.

Its strength is asymptotic amplification: an arbitrarily small excess beyond the Tsirelson value eventually matters at sufficiently large \(n\).

But the direct finite-\(n\) entropy boundary is not the quantum circle. Blog 4 therefore asks whether IC explains the global sphere or identifies its critical scaling threshold.

The classicalization argument has the complementary character:

- it is sharp already for \(n=2\);
- it uses no entropy;
- it produces the Euclidean circle directly in two-dimensional advantage space;
- but for larger \(n\) it lands only on the axis simplex, not on the full majority-enhanced classical boundary.

So one principle is strongest at the small end and the other becomes compelling through scaling.

A useful contrast box:

| | Classicalization/Recomposition | Information Causality |
|---|---|---|
| Natural setting | \(n=2\) | concatenated / large \(n\) |
| Core algebra | error biases multiply | information adds |
| Boundary mechanism | \(c_i^2\) maps to classical \(L_1\) | small-bias MI is quadratic |
| Sharpness | exact circle for two questions | Tsirelson threshold asymptotically |
| Main open issue | status as physical axiom | what part of global sphere IC explains |

Possible transition sentence:

> **Perhaps the circle can be seen from both ends: locally, through how errors compose when quantum information is destroyed; asymptotically, through how information accumulates when RACs are concatenated.**

This is suggestive, not a theorem connecting the two principles.

---

# 14. Return to Dynamics: Why the Quantum Case Feels Special

<!-- GOAL:
Bring the first GPT/dynamics thread back after the RAC result.
Do not imply the GPT literature proves the classicalization boundary.
-->

The argument above did not use quantum mechanics. That is precisely why it is interesting.

Quantum theory nevertheless sits at an appealing intersection of the two stories:

### When we preserve the quantum resource

Quantum mechanics supports continuous reversible dynamics, incompatible measurements, Bell measurements, teleportation and entanglement swapping. The resource can be manipulated and passed through a network without first turning every possible answer into a simultaneously existing classical record.

### When we destroy the quantum resource

Our RAC construction says that two independent errors square the coordinates,

\[
(c_1,c_2)\rightarrow(c_1^2,c_2^2).
\]

The quantum circle then lands exactly on the classical diamond.

This gives an evocative picture:

> **Quantum mechanics is rich enough to preserve and rotate genuinely quantum possibilities, yet its RAC advantage is restrained enough that deliberately classicalizing those possibilities drops us exactly back to the classical two-bit limit.**

This sounds like a “sweet spot”, but the article should be explicit:

- the GPT literature motivates the broader balance-between-correlation-and-dynamics question;
- our classicalization argument independently identifies the same circle in RAC advantage space;
- current science does **not** establish that these two observations are manifestations of one unique foundational principle.

That gap is a feature, not a defect. It is the open question.

---

# 15. A Better Meaning for “Why Isn’t Nature More Quantum?”

<!-- GOAL:
Tie back to series title/theme.
-->

“More quantum” is actually imprecise.

A PR box is not simply a qubit with stronger entanglement. A theory can have stronger nonlocal correlations while having poorer measurements or dynamics.

So by the end of the post, the original question can be reformulated:

> **Why does Nature allow exactly this amount of random-access advantage while retaining the rest of the operational structure we associate with quantum mechanics?**

The RAC geometry provides one partial answer:

> **Because the circle is a remarkably natural place for a compositional boundary to sit: preserve the quantum resource and the rich geometry remains available; classicalize it and the circle collapses exactly onto the classical two-question limit.**

Again, this is an answer **inside RAC advantage space**, not a derivation of the physical universe.

---

# 16. Suggested Figures

## Figure 1 — The familiar three shapes

**Content:** Two-dimensional advantage space with:

- classical diamond;
- quantum circle;
- outer no-signalling/perfect-RAC square.

Mark:

\[
(1,0),\quad
(0,1),\quad
\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
\quad
(1,1).
\]

**Purpose:** Re-establish the central mystery immediately.

**Caption idea:**  
*The two-question RAC has three natural scales: the classical diamond, the quantum circle, and the logically perfect square. Why does Nature stop at the middle curve?*

---

## Figure 2 — Different questions, same classical string

**Content:** Posterior bar charts over

\[
00,\;01,\;10,\;11.
\]

Three panels would be ideal:

1. Bob measures the \(x_1\)-optimized RAC axis;
2. Bob measures the \(x_2\)-optimized RAC axis;
3. Bob uses an oblique measurement producing a posterior such as
   \[
   (0.50,0.25,0.25,0).
   \]

Annotate:

- selected-coordinate success;
- Hamming-weight entropy;
- perhaps magnetization distribution.

**Purpose:** Show the “shadow of quantum dynamics” in an entirely classical posterior.

**Caption idea:**  
*Alice's bits remain classical, but Bob's quantum measurement choice changes what kind of classical information becomes visible: a coordinate, or a more collective property such as Hamming weight.*

---

## Figure 3 — Preserve versus classicalize

A fork diagram:

```text
                         ┌─ preserve quantum resource ──> swapping/teleportation
Alice ── quantum RAC ── Charlie
                         └─ measure both answers ───────> classical pair
```

For the lower branch, introduce David explicitly:

```text
Alice ──[two RAC copies]──> Charlie
                            |
                      (x̂₁, x̂₂)
                            |
                      2 classical bits
                            v
                          David ──[one RAC]──> Bob
```

**Purpose:** Make it visually undeniable where the classical cut occurs.

---

## Figure 4 — Squaring map: circle to diamond

This should probably be the key figure.

Left:

\[
(c_1,c_2)
\]

on the quantum quarter-circle.

Arrow labelled

\[
d_i=c_i^2.
\]

Right:

\[
(d_1,d_2)
\]

on the classical diamond edge

\[
d_1+d_2=1.
\]

Show several matched points:

\[
(1,0)\rightarrow(1,0),
\]

\[
\left(\frac1{\sqrt2},\frac1{\sqrt2}\right)
\rightarrow
\left(\frac12,\frac12\right),
\]

\[
(0,1)\rightarrow(0,1).
\]

**Caption idea:**  
*Coordinatewise error composition turns the quantum quarter-circle into the classical RAC edge. The Euclidean norm becomes the classical \(L_1\) budget after complete classicalization.*

---

## Figure 5 — What happens beyond the circle?

Take an illustrative post-quantum point such as

\[
(0.8,0.8).
\]

Show

\[
(0.8,0.8)\rightarrow(0.64,0.64),
\]

which lies outside

\[
d_1+d_2=1.
\]

**Purpose:** Make the proposed consistency question visceral.

Possible annotation:

> *The middle information is now completely classical. Should the final Alice–Bob relation still be allowed to lie beyond the classical RAC boundary?*

---

## Figure 6 — Higher dimensions

Show schematically:

\[
\sum_i c_i^2=1
\quad\xrightarrow{c_i^2}\quad
\sum_i d_i=1.
\]

For \(n=4\), overlay the axis simplex with the actual classical RAC cross-section/polytope to show that majority vertices extend beyond it.

**Purpose:** Explain immediately why the exact coincidence is special to \(n=2\).

---

# 17. Potential Pull Quotes

Use at most two or three.

> **The data are classical. The geometry of the questions is not.**

> **Destroy the quantum resource in the middle, and the quantum circle falls exactly onto the classical two-bit boundary.**

> **The circle may be more than a quantum prediction: in advantage space, it is also a remarkably natural composition boundary.**

The third is the boldest; use only if the surrounding caveat is nearby.

---

# 18. Possible Section Structure for the Published Post

A tighter publication structure than this research outline:

## Why Does Quantum Advantage Stop at a Circle?

### 1. The Shape Nature Refuses to Cross
Diamond → circle → square; pose the mystery.

### 2. Stronger Correlations, Poorer Physics?
GPT/Boxworld trade-off: correlations versus measurements/dynamics.

### 3. The Shadow of a Quantum Question
Posterior experiment: \(x_1\), \(x_2\), Hamming weight/magnetization.

### 4. Preserve It or Destroy It
Quantum swapping/teleportation versus full classicalization.

### 5. A Circle That Collapses Into a Diamond
Charlie–David construction; derive \(d_i=c_i^2\).

### 6. What Breaks Beyond the Circle?
Outside-circle point maps outside classical diamond; state the proposed consistency principle.

### 7. Why This Is Not a Derivation of Quantum Mechanics
RAC shadow versus GPT; higher-\(n\) caveat; relation to Information Causality.

### 8. A Different Answer to “Why Not More?”
End with the balance/dynamics question as genuinely open.

This is probably enough headings for Medium.

---

# 19. Possible Ending

A draft conceptual ending:

> I started this series by drawing the quantum boundary as a circle because that is what the quantum strategy gives us. The natural question was why Nature should stop there.
>
> Information theory gives one remarkable answer: push a correlation beyond the quantum threshold and sufficiently deep concatenation eventually makes the information accounting fail. But there is another way to look at the same circle.
>
> Take any two-question RAC point. Use independent copies to turn both possible answers into ordinary classical guesses. Hand those guesses across a deliberately classical cut. Then use the same kind of RAC resource once more. The error biases multiply, so the point \((c_1,c_2)\) becomes \((c_1^2,c_2^2)\).
>
> And the quantum circle does something almost suspiciously neat:
>
> \[
> c_1^2+c_2^2=1
> \quad\longrightarrow\quad
> d_1+d_2=1.
> \]
>
> Destroy the quantum part in the middle and what remains lands exactly on the classical two-bit RAC boundary.
>
> A stronger-than-quantum RAC would not. It would leave enough advantage after classicalization to push the final relation beyond the classical diamond.
>
> I do not want to claim that this derives quantum mechanics. It does not tell us what a state is, which measurements exist, or how Nature builds Hilbert space. Different physical theories could cast the same shadow in this game.
>
> But perhaps that is already the useful lesson. The quantum circle is not only a shape produced by quantum mechanics. In the geometry of this guessing game, it is also a very natural place for a compositional boundary to sit.
>
> Whether that coincidence is deep or accidental is a question I would like to understand better.

---

# 20. Claims to Verify Before Publication

These deserve explicit checking before converting the outline into finished prose.

1. **Classicalization principle status.**  
   Search literature on RAC concatenation, maximal correlation, strong data-processing inequalities, hypercontractivity, non-interactive simulation, wirings of nonlocal boxes, and GPT composition to see whether the exact \(c_i\mapsto c_i^2\) / classical-cut argument is already known under another language.

2. **Resource accounting.**  
   State clearly that Charlie uses two independent copies to extract \(\hat x_1,\hat x_2\), sends both bits classically to David, and David–Bob use a fresh RAC resource.

3. **Independence.**  
   The multiplication
   \[
   c_i^{AB}=c_i^{AC}c_i^{DB}
   \]
   assumes factorization of the error signs for the independent resource uses. Correlated uses require separate treatment.

4. **Meaning of “classical boundary”.**  
   The final comparison is to the \(2\to1\), one-classical-bit RAC advantage diamond. Explain why the proposed consistency principle demands that comparison rather than silently treating it as a theorem.

5. **No GPT reconstruction claim.**  
   A circular RAC shadow does not uniquely characterize a quantum GPT.

6. **Boxworld scope.**  
   The no-teleportation/no-swapping and trivial-reversible-dynamics statements apply to standard maximally nonlocal Boxworld/GNST, not to every post-quantum theory.

7. **Recent post-quantum network results.**  
   Include the Dmello–Gross result as a caution against saying post-quantum correlations generically forbid teleportation or stable network composition.

8. **Posterior/Hamming-weight example.**  
   Keep the exact posterior calculation and distinguish Hamming weight/magnetization from parity.

9. **Higher-\(n\) statement.**  
   Squaring the sphere gives the axis simplex
   \[
   \sum_i d_i=1,
   \]
   which is inside the full classical RAC body for \(n>2\) because majority strategies reach farther.

10. **Relationship to Information Causality.**  
    Present the two arguments as complementary viewpoints, not as mathematically equivalent principles unless such an equivalence is established.

---

# 21. Scientific References

## GPTs, state spaces and information processing

**[1] J. Barrett**, “Information processing in generalized probabilistic theories,” *Physical Review A* **75**, 032304 (2007).  
arXiv:quant-ph/0508211.  
Foundational GPT framework; discusses generalized no-signalling theories and explicitly emphasizes a trade-off between rich state spaces and allowed dynamics.

**[2] A. J. Short and J. Barrett**, “Strong nonlocality: A trade-off between states and measurements,” *New Journal of Physics* **12**, 033034 (2010).  
arXiv:0909.2601.  
Shows that standard Boxworld has stronger-than-quantum nonlocal states but restricted measurements; no teleportation, entanglement swapping or dense coding.

**[3] D. Gross, M. Müller, R. Colbeck and O. C. O. Dahlsten**, “All reversible dynamics in maximally non-local theories are trivial,” *Physical Review Letters* **104**, 080402 (2010).  
arXiv:0910.1840.  
Classifies reversible dynamics in maximally nonlocal Boxworld: essentially local relabellings and subsystem permutations; no reversible generation of nonlocal correlations from product states.

**[4] S. W. Al-Safi and J. Richens**, “Reversibility and the structure of the local state space,” *New Journal of Physics* **17**, 123001 (2015).  
arXiv:1508.03491.  
Studies the interplay between local geometry, maximally nonlocal composites and reversible transformations for broad GPT families.

**[5] L. J. Dmello and D. Gross**, “Probabilistic theories stable under teleportation,” arXiv:2603.21347 (2026).  
Classifies GPTs whose CHSH strength is stable under arbitrary rounds of entanglement swapping/teleportation-type composition; important counterweight to any generic “post-quantum means poor dynamics” claim.

**[6] S. Umekawa, A. Hokkyo, H. Arai and K. Takasan**, “Entanglement Generation Beyond Quantum Theory: From Product States to Popescu–Rohrlich Boxes,” arXiv:2608.02403 (2026).  
Shows that Boxworld's reversible entanglement-generation no-go changes when one asks only for pure-state-preserving transformations.

**[7] P. Janotta**, “Generalizations of Boxworld,” arXiv:1210.0618 (2012).  
Constructs modified Boxworld theories with entangled measurements and analyzes entanglement swapping; also provides continuous transitions between classical probability theory and Boxworld.

---

## Reconstruction / reversible symmetry

**[8] L. Masanes and M. P. Müller**, “A derivation of quantum theory from physical requirements,” *New Journal of Physics* **13**, 063001 (2011).  
arXiv:1004.1483.  
GPT reconstruction in which reversible equivalence of pure states is one of the central requirements; useful background for why continuous reversible symmetry is structurally important. Do not identify their generalized-bit state space with our RAC advantage body.

---

## Nonlocality and the quantum boundary

**[9] S. Popescu and D. Rohrlich**, “Quantum nonlocality as an axiom,” *Foundations of Physics* **24**, 379–385 (1994).  
Introduces the stronger-than-quantum/no-signalling perspective associated with PR-box correlations.

**[10] B. S. Tsirelson**, “Quantum generalizations of Bell's inequality,” *Letters in Mathematical Physics* **4**, 93–100 (1980).  
Original quantum CHSH bound.

**[11] M. Pawłowski, T. Paterek, D. Kaszlikowski, V. Scarani, A. Winter and M. Żukowski**, “Information causality as a physical principle,” *Nature* **461**, 1101–1104 (2009).  
Introduces Information Causality and derives the familiar Tsirelson threshold in the concatenated random-access setting.

---

## Measurement incompatibility and RACs

**[12] C. Carmeli, T. Heinosaari and A. Toigo**, “Quantum random access codes and incompatibility of measurements,” arXiv:1911.04360 (verify final journal citation before publication).  
Useful for the statement that quantum RAC advantage is intimately connected to incompatible decoding measurements.

---

# 22. Reference Use by Section

For efficient drafting:

- **Section 2, balance between correlations and dynamics:** [1]–[7]
- **Section 3, GPT/RAC shadow caution:** [1], [8]
- **Section 4, richer quantum questions:** [12], with [2] for Boxworld contrast
- **Section 6, swapping/teleportation:** [2], [5]
- **Sections 7–12, classicalization argument:** primarily our RAC-space derivation; literature search still required for precedence
- **Information Causality comparison:** [11]
- **Outer square / PR-box context:** [9]
- **Quantum circle / Tsirelson context:** [10], [11]

---

# 23. Novelty / Priority Note for Ourselves

<!-- INTERNAL NOTE — REMOVE BEFORE PUBLICATION -->

The potentially original insight is not the elementary identity

\[
(2P-1)_{\rm total}
=
(2P_1-1)(2P_2-1),
\]

which is standard composition of binary symmetric errors.

The potentially interesting formulation is the **advantage-space composition test**:

1. use independent copies of a two-question RAC resource to materialize all coordinates as classical noisy guesses;
2. insert an explicit classical cut;
3. reuse the same RAC resource downstream;
4. demand that the resulting effective classical RAC remain in the classical \(L_1\) body;
5. observe that this selects
   \[
   \|c\|_2\le1
   \]
   exactly for \(n=2\).

Before calling this novel, search literature under terms including:

- random access code concatenation;
- nonlocal box wirings;
- bias amplification / bias composition;
- maximal correlation;
- hypercontractivity ribbon;
- strong data processing;
- information causality without concatenation;
- classical bottleneck GPT;
- closure under wirings;
- non-interactive simulation;
- tensorization of correlation;
- RAC composition;
- operational probabilistic theories and classical interfaces.

The blog does not require a novelty claim. A safe line is:

> *Here is another way to look at the circle that emerged naturally from the advantage-space geometry.*

---

# 24. Final Tone

The post should feel curious rather than triumphant.

Good language:

- “suggests”
- “a natural consistency requirement”
- “in advantage space”
- “a surprisingly exact coincidence”
- “one way to read the circle”
- “quantum mechanics saturates this boundary”
- “this does not characterize quantum theory”
- “I do not know whether the coincidence is fundamental”

Avoid:

- “we proved why Nature is quantum”
- “post-quantum theories are impossible”
- “the circle follows from classical information alone”
- “Boxworld proves stronger correlations destroy dynamics”
- “teleportation singles out Tsirelson”
- “the RAC circle is the GPT state space”

A useful final stance:

> **The goal is not to explain the whole quantum world. It is to understand why, in this particular shadow of that world, the circle is such a natural boundary.**
