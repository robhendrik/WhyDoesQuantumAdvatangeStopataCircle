Why Does Quantum Advantage Stop at a Circle?

We know exactly where the quantum boundary is. The harder question is why Nature stops there.

<!--
BLOG 5 — RAC SERIES FINALE

ROLE IN SERIES
1. Classical RAC: what is the best Alice can do with one classical bit?
2. Quantum advantage: a quantum resource beats the classical strategy.
3. Geometry: classical polytopes versus the quantum circle / hypersphere.
4. Information Causality: a serious attempt to explain the quantum limit.
5. This post: step back and ask what we actually understand about WHY the circle/sphere is the boundary.
6. Next post: try to construct stronger-than-quantum "superphotons" and ask what else breaks.

CENTRAL DISCIPLINE
This post is deliberately more reflective than Blogs 1–3.

Do not claim that the relay construction derives quantum mechanics or proves that Nature must obey the quantum circle.

Distinguish throughout:
1. established results from the literature;
2. exact mathematics of the 2→1 RAC;
3. our own interpretation and open questions.
-->

One-Sentence Spine

After four posts we know the quantum sphere remarkably well, but understanding its mathematical boundary is not the same as understanding why Nature chooses it.

We Keep Finding the Same Circle

<!--
GOAL:
Reconnect the series in ~150–200 words.
The reader should not need to remember the previous posts.
Introduce c₁ and c₂ in one sentence and immediately put the three geometries on screen.
-->

Alice has two bits. Bob receives one classical bit from her and later chooses which of Alice's bits he wants to guess.

Write

[
c_i = 2P_i-1,
]

so (c_i=0) means Bob is guessing randomly and (c_i=1) means he recovers bit (i) perfectly.

The same little game gives us three strikingly different geometries:

classical one-bit strategies fill a diamond;

quantum-assisted strategies reach a circle;

no-signalling alone permits the surrounding square.

For the two-question game,

[
|c_1|+|c_2|\le1
]

classically, while quantum mechanics reaches

[
c_1^2+c_2^2\le1.
]

We know that Nature stops at the circle.

But do we know why?

That is a surprisingly different question.

We understand the quantum circle mathematically much better than we understand why Nature chooses it.

Figure 1 — The Three RAC Worlds



Caption: Three boundaries for the same 2→1 guessing game. Classical one-bit strategies fill the diamond, quantum mechanics reaches the circle, while no-signalling alone permits the surrounding square.

Alt text: Two-dimensional RAC advantage space with horizontal axis c₁ and vertical axis c₂. A blue diamond marks the classical region |c₁|+|c₂|≤1, an orange circle marks the quantum boundary c₁²+c₂²=1, and a dashed grey square marks the no-signalling region |c₁|≤1, |c₂|≤1. The positive diagonal shows the symmetric quantum point and the PR-box corner.

No-Signalling Is Not Enough

<!--
GOAL:
Dispose of the first tempting explanation quickly.
Use Popescu–Rohrlich as the established result.
-->

Popescu and Rohrlich showed that correlations can be stronger than quantum correlations while still preventing faster-than-light signalling [2].

So relativity alone does not give us the circle.

A hypothetical resource can reach all the way to

[
(c_1,c_2)=(1,1),
]

allowing Bob to recover whichever bit he asks for perfectly, while the shared resource by itself still cannot be used to signal from Alice to Bob.

The first conclusion is therefore quite sharp:

The quantum boundary is not simply the boundary of no-signalling.

There remains an entire region between the quantum circle and the no-signalling square that is mathematically conceivable but apparently unused by Nature.

Information Causality Gets Remarkably Close

<!--
GOAL:
Summarize Blog 4 rather than repeat it.
Treat IC as serious established science, then state exactly what remains unsatisfying.
-->

Information Causality provides perhaps the best-known attempt to explain why Nature refuses stronger correlations [3].

Alice may send Bob a limited amount of classical information. Even if they share arbitrary no-signalling correlations beforehand, the total information Bob can gain about Alice's independent data should not exceed that communication budget.

For concatenated random-access codes, something remarkable happens. If an isotropic correlation is even slightly stronger than the quantum value, repeated concatenation eventually violates Information Causality. The critical strength is exactly the Tsirelson value.

That is difficult to dismiss as coincidence.

But it also leaves questions.

At finite (n), the direct mutual-information boundary is not simply the quantum circle or hypersphere. The familiar quantum threshold emerges through concatenation and scaling as the game becomes larger.

And the quantity being bounded is a sum of mutual informations about alternative questions — pieces of information Bob does not simultaneously extract in a single run.

So Information Causality gives us an important clue. Whether it gives us the physical reason for the sphere is less obvious.

<!--
OPTIONAL SHORT TRANSITION:
Blog 4 can be linked here rather than summarized in more detail.
-->

From Correlations to Theories

<!--
GOAL:
Introduce GPTs verbally, before our relay construction.
The reader should understand why the scientific discussion moves beyond a correlation boundary,
without having to learn GPT formalism.
-->

There is a broader way physicists now study this question.

Instead of asking only which correlation tables are mathematically possible, generalized probabilistic theories (GPTs) ask what a complete operational theory would have to contain: which states can be prepared, which measurements can be performed, which transformations are allowed, and how separate systems can be combined [5].

Quantum mechanics is one such theory. Classical probability theory is another. Boxworld and other hypothetical post-quantum theories provide comparison cases.

That changes the question slightly.

It is no longer only:

How far can the point ((c_1,c_2)) move?

It becomes:

What else must a world allow if it contains correlations beyond the quantum circle?

This distinction matters because a set of correlations does not live in isolation. The states, measurements, transformations and rules for combining systems have to work together consistently.

We will keep the discussion operational here rather than develop the GPT machinery. But this broader viewpoint will become important again at the end of the post — because this is also where the contemporary scientific debate is taking place.

Another Curious Property of the Circle

<!--
GOAL:
Introduce the relay/classicalization construction as an observation, not as a principle.
This is the mathematical and visual centre of Blog 5.
-->

There is another little experiment we can perform on the geometry.

First consider what quantum mechanics normally allows in a relay. If two neighbouring pairs share entanglement, a suitable joint measurement at the middle station can perform entanglement swapping: the two original links are consumed and a new nonclassical connection is established between the outer parties.

That is useful as a contrast, because our thought experiment deliberately does the opposite.

Instead of preserving the nonclassical connection, we terminate it in the middle, materialize ordinary classical records, and then start again with an independent downstream resource.

Figure 2 — Keeping the Connection Alive



Caption: Entanglement swapping can preserve a nonclassical connection across a relay: Charlie couples two links and Alice and Bob become connected. Our thought experiment below deliberately does the opposite — it terminates the upstream resource and lets only ordinary classical records cross the middle.

Alt text: Two-row telephone analogy. In the top row, Alice has one telephone connection to Charlie and Charlie has a separate connection to Bob, with Charlie's two endpoints enclosed by a dashed box. In the bottom row, Alice and Bob share one continuous telephone line while Charlie is crossed out inside the dashed box.

Now suppose a 2→1 RAC resource has advantages

[
(c_1,c_2).
]

To turn both possible answers into classical records, we use independent copies. We then feed the resulting noisy classical records through another independent RAC resource.

For independent binary errors, the biases multiply. If the same bias is used at both stages,

[
d_i=c_i^2.
]

So the map in advantage space is simply

[
(c_1,c_2)\longrightarrow(c_1^2,c_2^2).
]

And something rather beautiful happens.

Take any point on the quantum circle,

[
c_1^2+c_2^2=1.
]

After the relay,

[
d_1+d_2=c_1^2+c_2^2=1.
]

The entire quantum quarter-circle therefore maps exactly onto the positive edge of the classical one-bit RAC diamond.

Not approximately. Not asymptotically.

Exactly.

The quantum circle has a curious property: square its two advantages and it becomes the classical boundary.

Squaring the Circle

<!--
GOAL:
Let Figure 3 carry the main calculation.
The prose should explain the three regimes and resist overinterpreting them.
-->

The map

[
(c_1,c_2)\rightarrow(c_1^2,c_2^2)
]

has three simple regimes.

If we start inside the quantum circle,

[
c_1^2+c_2^2<1,
]

then

[
d_1+d_2<1,
]

and the image remains inside the classical one-bit boundary.

If we start exactly on the quantum circle,

[
c_1^2+c_2^2=1,
]

then

[
d_1+d_2=1,
]

and the image lands exactly on the classical boundary.

And if we start outside the quantum circle,

[
c_1^2+c_2^2>1,
]

then

[
d_1+d_2>1.
]

The image now lies outside that classical one-bit region.

Figure 3 — Squaring the Circle



Caption: Under the map (d_i=c_i^2), a point inside the quantum circle lands inside the classical one-bit region, every point on the circle lands exactly on its boundary, and a point even slightly outside the circle lands outside. The mapping is exact for the 2→1 RAC.

Alt text: Two side-by-side positive-quadrant RAC plots. The left panel shows the classical triangular region, the orange quantum quarter-circle, and three symmetric points: one inside the circle, one on it, and one outside. Grey arrows map the points to the right panel using dᵢ=cᵢ². On the right, the first image lies inside the classical triangle, the second lies on the line d₁+d₂=1, and the third lies outside it.

At first sight, this makes the quantum circle look tantalizingly special.

If we were searching for a boundary that survives this particular act of classicalization, we could hardly have drawn a better one.

But is that really an explanation?

Is That an Explanation?

<!--
GOAL:
This is where the article earns credibility.
Ask the objections explicitly instead of hiding them in footnotes.
The tone should be "I got excited by this too, then these questions appeared."
-->

I do not think we can say that yet.

The more closely we look at the relay construction, the more questions appear.

Charlie Cannot Obtain Both Answers From One System

The coordinates (c_1) and (c_2) describe the performance of alternative measurements.

Charlie cannot ask both questions of the same quantum system.

To materialize both possible answers,

[
(\hat x_1,\hat x_2),
]

he needs independent copies.

So the relay already uses more resources than the original RAC.

How Much Classical Information Crosses the Cut?

Once both possible guesses have been materialized, two ordinary classical bits may exist at the intermediate stage.

Why should the end-to-end process then be judged against the one-bit classical RAC diamond?

That does not follow automatically from ordinary communication theory.

It would be an additional consistency requirement — and one that needs an independent physical justification.

Why Use the Same Resource Again?

The square appears because we deliberately use identical biases upstream and downstream:

[
d_i=c_i c_i'=c_i^2.
]

With a different downstream resource,

[
d_i=c_i c_i',
]

and the same circle is no longer singled out by the algebra.

Again, the construction is interesting, but part of its beauty comes from a symmetry we chose.

What Happens for More Questions?

For the 2→1 RAC, the classical boundary in the positive quadrant is especially simple:

[
c_1+c_2=1.
]

For larger RACs, the classical body is richer. Majority strategies extend beyond the simple axis simplex.

So the exact

[
\text{quantum sphere}\longrightarrow\text{classical boundary}
]

coincidence does not continue in this simple form at higher (n).

That is a substantial warning against treating the two-dimensional observation as a general physical law.

<!--
OPTIONAL PULL QUOTE IF A THIRD ONE IS WANTED:
> **A beautiful geometric coincidence is not yet a physical principle.**
-->

Where Science Is Today

<!--
GOAL:
Make clear that the unresolved question is not merely the author's personal doubt.
The reader should finish the RAC series realizing that the simple guessing game has led directly
into an active 2026 foundations debate.
-->

After five posts, we can now separate several things that are known from one thing that is still being worked out.

No-signalling does not select the quantum sphere. It permits much stronger correlations [2].

Information Causality identifies the Tsirelson threshold in a remarkable way, but through concatenation and scaling rather than by simply reproducing the finite-(n) sphere [3].

And our relay experiment exposes another exact mathematical property of the smallest RAC: under

[
d_i=c_i^2,
]

the quantum circle maps onto the classical one-bit boundary.

None of these observations, by itself, is currently a generally accepted physical principle that uniquely explains why Nature chooses the quantum correlation set.

That is not where this story ends. It is where contemporary research begins.

The GPT programme introduced earlier asks precisely what additional structure — states, measurements, transformations, composition rules, symmetry or information-processing requirements — distinguishes quantum mechanics from other internally consistent probabilistic theories [5].

And this remains an active question in 2026.

Dmello and Gross recently classified probabilistic theories whose CHSH strength can survive arbitrarily many rounds of teleportation- or entanglement-swapping-type composition. Their results include theories that can remain stronger than quantum, showing that even demanding robust network composition does not by itself isolate the quantum value [7].

In another 2026 result, Umekawa and collaborators revisited the familiar Boxworld restriction on entangling dynamics. They showed that once reversibility is relaxed to pure-state preservation, transformations exist that can generate PR-box entanglement from initially uncorrelated states [8].

These results do not move the quantum circle. They show how difficult it is to explain why that particular circle is Nature's one.

We started with two bits and one guess. We have ended at a question that researchers are still actively trying to answer: which physical principles single out quantum theory from the larger space of possible theories?

That is perhaps the most useful conclusion of the RAC series.

The diamond, circle and square were not only geometrical curiosities. They gave us a small enough game to see, step by step, the same distinction that appears in modern foundations research: mathematically possible correlations are not the same thing as a complete physical theory.

And that suggests a natural next experiment.

What happens if we stop treating the region outside the circle as an abstract possibility and actually try to invent particles that live there?

In the next post, we will do exactly that with our hypothetical 'superphotons'.

<!--
FOR BLOG 6:
Return to the previously defined "superphotons".
Keep their stronger angular correlation law, try to retain ordinary local photon operations and a Bell-type joint measurement, and show where negative probabilities appear.
Short & Barrett (2010) becomes the rigorous Boxworld comparison.
-->

Closing line: A simple guessing game has taken us all the way to a question at the edge of current quantum-foundations research: not what quantum mechanics predicts, but why the space of physical possibilities seems to stop where quantum mechanics says it should.

References

[1] B. S. Tsirelson, “Quantum generalizations of Bell's inequality,” Letters in Mathematical Physics 4, 93–100 (1980). https://doi.org/10.1007/BF00417500

[2] S. Popescu and D. Rohrlich, “Quantum nonlocality as an axiom,” Foundations of Physics 24, 379–385 (1994). https://doi.org/10.1007/BF02058098

[3] M. Pawłowski, T. Paterek, D. Kaszlikowski, V. Scarani, A. Winter and M. Żukowski, “Information causality as a physical principle,” Nature 461, 1101–1104 (2009). https://doi.org/10.1038/nature08400

[4] M. Pawłowski and M. Żukowski, “Entanglement assisted random access codes,” Physical Review A 81, 042326 (2010). https://doi.org/10.1103/PhysRevA.81.042326

[5] J. Barrett, “Information processing in generalized probabilistic theories,” Physical Review A 75, 032304 (2007). https://doi.org/10.1103/PhysRevA.75.032304

[6] L. J. Dmello, L. T. Ligthart and D. Gross, “Entanglement-swapping in generalised probabilistic theories, and iterated CHSH games,” Physical Review A 110, 022225 (2024). https://doi.org/10.1103/PhysRevA.110.022225

[7] L. J. Dmello and D. Gross, “Probabilistic theories stable under teleportation,” arXiv:2603.21347 (2026).

[8] S. Umekawa, A. Hokkyo, H. Arai and K. Takasan, “Entanglement Generation Beyond Quantum Theory: From Product States to Popescu–Rohrlich Boxes,” arXiv:2608.02403 (2026).

<!--
REFERENCE NOTES

[1] Quantum / Tsirelson boundary.
[2] Stronger-than-quantum but no-signalling correlations.
[3] Information Causality and the concatenated-RAC route to the Tsirelson threshold.
[4] Background for concatenated entanglement-assisted RACs and classical intermediate variables.
[5] GPT framework: states, measurements, transformations and composite systems.
[6] Post-quantum entanglement swapping / iterated CHSH.
[7] 2026 classification of GPTs stable under repeated teleportation/swapping-type composition.
[8] 2026 result showing that Boxworld's reversible entangling no-go changes when reversibility is relaxed to pure-state preservation.

SAVE FOR BLOG 6:
A. J. Short and J. Barrett, “Strong nonlocality: A trade-off between states and measurements,”
New Journal of Physics 12, 033034 (2010).
https://doi.org/10.1088/1367-2630/12/3/033034
-->