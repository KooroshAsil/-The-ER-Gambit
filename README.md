
# 💉 *The ER Gambit 🎲* 
## Queueing Analysis of a Hospital Emergency Room

> *A fun, friendly, and impactful take on how queueing theory & simulation can improve hospital ER efficiency* 🚑📉

---

## 🌟 What’s This About?

Ever wondered what happens behind the scenes in an Emergency Room (ER) when people wait too long? 🤔  
This project dives into that question using the **power of math & simulation!** We model the ER as a **queueing system** to:

- Understand how long patients wait 🧍‍♂️⏳
- Explore how staff (doctors 🩺) impact delays
- Balance **cost vs care** for better decision-making

🎯 *It’s math for real-life impact!*

---

## 🎯 Project Goals

1. ✍️ **Derive** steady-state queue metrics like utilization (ρ), average queue length (Lq), and waiting time (Wq).
2. 🧪 **Simulate** real-world ER dynamics using **Discrete-Event Simulation (DES)**.
3. 🔍 **Validate** analytical models using simulation results.
4. 🎚 **Analyze sensitivity** of system under different λ (arrival), μ (service), and c (server count).
5. ⚖️ **Optimize staffing**: Find the sweet spot between waiting time ⏱ and cost 💸.

---

## 💎 Core Values

- 🤝 *Clarity*: Tackle complexity with clean, readable models.
- 💡 *Curiosity*: Go beyond course theory — explore what’s possible.
- 🔬 *Accuracy*: Verify theory through simulation.
- 💙 *Impact*: Help improve healthcare systems in a measurable way.

---

## 🧰 Tools & Techniques

| Category              | Tools / Concepts                             |
|-----------------------|----------------------------------------------|
| 📐 Math/Modeling       | Queueing Theory (M/M/1, M/M/c), Erlang C     |
| 💻 Simulation          | Discrete-Event Simulation (Python)           |
| 📊 Analysis            | Sensitivity, Optimization, Cost Trade-offs   |
| 📘 References          | Kleinrock, Law & Kelton, Green et al.        |

---

## 📚 Theory in a Nutshell

### 🌀 Poisson Process
- Patients arrive randomly: **Poisson(λ)**
- Inter-arrival times ~ Exp(λ)

### ⚡ Exponential Service
- Service per patient ~ Exp(μ)
- Simple yet powerful assumption

### 🔁 M/M/1 and M/M/c Queues
- M/M/1: Single doctor, growing queues 😬
- M/M/c: Multiple doctors 🩺🩺🩺 — more realistic!
- Uses Erlang C for waiting time & probability 📈

---

## 🧪 How We Simulate It

- Events: **ARRIVAL** & **DEPARTURE**
- FIFO patient queue
- Time-driven tracking of system states
- Collect key stats:  
  - `L`, `Lq`, `W`, `Wq`, `ρ`, `P(wait)`
- Parameters:
  - `λ = 8, 10, 12`, `μ = 12`, `c = 1, 2, 3`
  - Horizon: 10,000 hours, 30 independent runs

---

## 📊 Results: Analytical vs Simulated

| λ | c | ρ  | L (theory) | L (sim)  | Wq (theory) | Wq (sim) |
|---|---|-----|------------|----------|-------------|----------|
|10 | 1 | 0.83| 4.83       | ~4.80    | 0.166       | ~0.168   |
|10 | 2 | 0.42| 1.45       | ~1.50    | 0.061       | ~0.063   |
|10 | 3 | 0.28| 0.39       | ~0.41    | 0.011       | ~0.012   |

✅ **Simulation confirms theory!**

---

## 🧠 Optimization: Cost vs. Care

We ask: _How many doctors do we need?_  
🎯 Goal: Keep `Wq ≤ 0.1 hr` with minimum cost.

**Example:**
```text
λ = 10, μ = 12
Staff cost = $100/hour
Patient wait penalty = $20/hour
Best c = 2
```

📉 Total Cost = Staffing + Wait Penalty  
Helps hospital admins make **smart staffing choices**!

---

## ⚠️ Assumptions & Limitations

- λ and μ are constant — no rush hours.
- No prioritization or patient abandonment.
- Infinite queue capacity.
- Exponential distributions may oversimplify.

---

## 🚀 What’s Next?

Want to make it even more realistic?

- ⏳ **M(t)/M/c**: Time-varying arrivals
- 🔀 **M/G/1**: General service distributions
- 🚨 **Priority queues**
- 🚪 **Reneging/abandonment**
- 🏥 **Multi-department queue networks**

---

## 📥 Inputs / 📤 Outputs

### Inputs
- λ (arrival rate), μ (service rate), c (server count)
- Costs: doctor/hr, patient-wait/hr
- Simulation horizon

### Outputs
- 📊 Performance metrics: `L, Lq, W, Wq, ρ, P(wait)`
- ✅ Comparisons: Theory vs. Simulation
- 💸 Optimal staffing decisions

---

## 💬 Why This Project Rocks

- 🎓 Learn queueing theory through applied simulation
- 🏥 Tackle real-world healthcare challenges
- 💻 Combine coding, modeling & decision science
- 📈 Make data-driven, cost-effective staffing suggestions

---

Made with 💙 by *Koorosh Asil Gharehbaghi*  
Instructor: Dr. Razieh Khodsiani  

K. N. Toosi University of Technology  
Department of Computer Science  
Faculty of Mathematics

