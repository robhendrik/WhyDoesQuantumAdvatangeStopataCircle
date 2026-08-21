## Figures

### Figure 1 — Classical, Quantum, and Post-Quantum Regions
**Caption:**  
*Figure 1: The 2→1 RAC advantage space. Classical one-bit strategies fill the diamond \(|c_1|+|c_2|\le 1\). Quantum-assisted strategies reach the circle \(c_1^2+c_2^2\le 1\). Hypothetical stronger-than-quantum resources could extend further, up to the square \(|c_1|\le 1,\ |c_2|\le 1\). The central question of this post is: why does Nature stop at the circle?*

**Alt text:**  
*Plot in \(c_1,c_2\) space showing three nested regions: a classical diamond, a quantum circle, and an outer square for logically possible or no-signalling correlations. The symmetric quantum point and a stronger-than-quantum point outside the circle are marked.*

---

### Figure 2 — Bob Can Ask Different Questions
**Caption:**  
*Figure 2: The same message can support different questions. The two panels show Bob’s posterior distribution over Alice’s four possible bit strings when he chooses the measurement optimized for the first bit or for the second bit. The message is the same, but Bob’s measurement changes what he learns. Quantum advantage is not just about “more success”; it is about a richer menu of questions Bob can ask.*

**Alt text:**  
*Two bar charts showing Bob’s posterior probabilities over Alice’s strings 00, 01, 10, and 11. In the left panel Bob measures to recover the first bit; in the right panel he measures to recover the second bit. The posterior shifts depending on Bob’s choice of measurement.*

---

### Figure 3 — Preserve the Resource, or Break It with a Classical Cut
**Caption:**  
*Figure 3: Two kinds of composition. Top: a nonclassical resource is preserved through an intermediate operation, as in entanglement swapping or teleportation. Bottom: the resource is destroyed at the intermediate node. Charlie extracts two ordinary classical bits and sends only those across the Charlie–David cut; no entanglement, nonlocal box, or other nonclassical resource crosses that boundary. David and Bob then use a fresh downstream resource. This distinction is the starting point of our thought experiment.*

**Alt text:**  
*Conceptual network diagram with two branches. In the top branch, a nonclassical connection is preserved across an intermediate step. In the bottom branch, Alice and Charlie use two upstream resources, Charlie extracts two classical bits, those bits cross a hard classical cut to David, and David and Bob use a fresh downstream resource. The cut is highlighted as carrying only classical information.*

---

### Figure 4 — A Telephone-Line Analogy for the Classical Cut
**Caption:**  
*Figure 4: A telephone-line analogy. In entanglement swapping, two links can be coupled into one longer link, so the middle station disappears from the final connection. Our classical-cut construction is different: the middle station does not pass the line through. It only writes down ordinary classical information and forwards that onward. The point of the cut is precisely that the nonclassical link does not survive it.*

**Alt text:**  
*Simple analogy diagram using telephone lines between cities or stations. One panel shows two links being coupled into a single end-to-end link. A contrasting panel shows a break in the line, with only a classical message passed across the middle instead of a continuous connection.*

---

### Figure 5 — Squaring Maps the Quantum Circle to the Classical Edge
**Caption:**  
*Figure 5: The key geometric step. If the upstream and downstream resources have the same biases, then composing them through the classical cut multiplies the biases, so \(d_i=c_i^2\). Under this map, the positive quarter of the quantum circle \(c_1^2+c_2^2=1\) is sent exactly to the classical edge \(d_1+d_2=1\). For example, \((1/\sqrt{2},1/\sqrt{2})\) maps to \((1/2,1/2)\). The circle becomes the unique boundary that lands precisely on the classical one-bit limit.*

**Alt text:**  
*Two-panel geometric figure. The left panel shows the positive quarter of the quantum circle in \(c\)-space. The right panel shows the classical line segment \(d_1+d_2=1\) in \(d\)-space. Arrows indicate the squaring map \(d_1=c_1^2,\ d_2=c_2^2\), including the mapping of notable points such as \((1,0)\), \((1/\sqrt2,1/\sqrt2)\), and \((0,1)\).*

---

### Figure 6 — What Goes Wrong Beyond the Circle
**Caption:**  
*Figure 6: A stronger-than-quantum point fails the classical-cut test. A point such as \((c_1,c_2)=(0.8,0.8)\), which lies outside the quantum circle, maps to \((d_1,d_2)=(0.64,0.64)\). But this lies outside the classical one-bit boundary, since \(0.64+0.64>1\). In this sense, stronger-than-quantum correlations would survive the cut too well.*

**Alt text:**  
*Geometric illustration of a point outside the quantum circle being squared coordinate-wise and landing outside the classical diamond or outside the classical positive edge. The mapped point is labeled and the violation of the classical bound is shown numerically.*

---

## Minimal Figure Set

If we want to keep the post visually lean, I would use these four:

1. **Figure 1** — Classical / quantum / post-quantum regions  
2. **Figure 3** — Preserve vs classical cut  
3. **Figure 5** — Circle maps to classical edge under squaring  
4. **Figure 6** — Post-quantum point fails the test  

<!-- Optional: Figure 2 is pedagogically helpful, and Figure 4 is a nice intuition figure if we want a more blog-friendly tone. -->