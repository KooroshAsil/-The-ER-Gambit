
# 🎲💉 *The ER Gambit* — Queueing Analysis of a Hospital Emergency Room

> *A fun, friendly, and meaningful take on how to model and improve hospital emergency room efficiency using queueing theory & simulation* 🚑⚙️📉

---

## ✨ Overview

This project explores how *queueing theory* (📚) and *discrete-event simulation* (🎲) can be used to **analyze**, **optimize**, and **simulate** the behavior of an **Emergency Room (ER)**.

💥 We model patient arrivals as a **Poisson process** and service times as **exponential**, applying both **M/M/1** and **M/M/c** systems to uncover insights on:

- 🧮 **Utilization** & **queue length**
- ⏱ **Waiting times**
- 📉 **Probability of waiting**
- 💵 **Cost trade-offs for staffing**
- 🧠 **Real-world hospital management insights**

---

## 🎯 Project Goals

1. ✍️ Derive analytical formulas for M/M/1 and M/M/c queueing models.
2. 💻 Implement a **discrete-event simulation (DES)** to mimic real-life ER dynamics.
3. 📊 Compare simulation results with theoretical calculations.
4. 🔍 Perform **sensitivity analysis** by tweaking arrival/service rates & number of servers.
5. ⚖️ Optimize ER staffing levels based on **cost vs. waiting time** trade-offs.

---

## 📚 Theory in a Nutshell

### 🌀 Poisson Arrivals
- Patients arrive randomly following a **Poisson process** with rate λ.
- Inter-arrival times ~ **Exp(λ)**.

### ⚡ Exponential Service
- Service time per patient follows **Exp(μ)**.
- Memoryless property for simplicity.

### 📈 Queue Models

#### M/M/1 (1 server)
- Easy to analyze.
- Queue can get long when λ approaches μ.

#### M/M/c (Multiple servers)
- More flexible & realistic.
- Uses **Erlang C** formula to calculate waiting probabilities.

---

## 🧪 Simulation: Discrete-Event Style

We simulate ER activity with:
- ⏰ Timed events: ARRIVAL & DEPARTURE
- 🧾 FIFO queue for patients
- ⚙️ Event-driven updates to system state
- 📉 Statistics on: L, Lq, W, Wq, ρ, P(wait)

🎛 Parameters:
- `λ = 8, 10, 12`
- `μ = 12`
- `c = 1, 2, 3`
- 30 independent replications

---

## 🔬 Analytical vs. Simulated Results

| λ | c | ρ | L (theory) | L (sim) | Wq (theory) | Wq (sim) |
|---|---|----|-------------|-----------|----------------|-------------|
| 10 | 1 | 0.83 | 4.83 | ~4.80 | 0.166 | ~0.168 |
| 10 | 2 | 0.42 | 1.45 | ~1.50 | 0.061 | ~0.063 |
| 10 | 3 | 0.28 | 0.39 | ~0.41 | 0.011 | ~0.012 |

✅ Theory and simulation match well!

---

## 🧠 Optimization & Cost Trade-Offs

We want to find the *best number of doctors* to:

- Keep waiting times ⏳ under a **target**
- Minimize total cost 💵 = staffing cost + patient wait cost

🎯 Example:
```text
Target Wq = 0.1 hr
λ = 10, μ = 12

Best c = 2 (balances cost vs. performance)
```

---

## 🔍 Limitations

- Assumes constant λ and μ
- No patient prioritization
- No patient abandonment
- Real ERs may not have infinite waiting space!

---

## 🛠 Extensions & Future Ideas

- 📈 Time-varying arrivals: M(t)/M/c
- 🧪 General service times: M/G/1
- 🚨 Priority queues (critical vs. non-critical)
- 🚪 Patient abandonment models
- 🏥 Queue networks for full hospital systems

---

## 💾 Inputs & Outputs

### Inputs
- Arrival rate `λ`
- Service rate `μ`
- Number of doctors `c`
- Costs: staff, patient waiting
- Simulation horizon `Tmax`

### Outputs
- L, Lq, W, Wq, ρ, P(wait)
- Simulated vs. theoretical comparisons
- Optimal staffing/cost recommendations

---

## 💡 Why This Matters

✔️ Real-world value for hospital decision-makers  
✔️ Learn-by-doing approach to queueing theory  
✔️ Combines *math*, *simulation*, and *healthcare* into one meaningful project

---

Made with 💙 by *Koorosh Asil Gharehbaghi*  
Dept. of Computer Science, K. N. Toosi University of Technology  
Instructor: Dr. Razieh Khodsiani
