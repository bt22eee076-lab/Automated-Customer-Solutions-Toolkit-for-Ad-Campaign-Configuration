# Automated Customer Solutions Toolkit for Ad Campaign Configuration

## Overview
This project is a self-initiated automation toolkit designed to validate advertising campaign configurations and identify common setup issues before they impact performance. The goal is to simulate how customer and partner solutions teams prevent misconfigurations at scale rather than fixing issues reactively.

The system applies rule-based validation to campaign configuration data and produces clear, prioritized insights that can be understood by both technical and non-technical stakeholders.

---

## Problem Statement
In large advertising platforms, campaigns are frequently misconfigured due to incorrect bidding strategies, insufficient budgets, or overly broad targeting. These issues often lead to poor performance, wasted spend, and increased support requests.

Manually reviewing campaign setups does not scale. This project demonstrates how automation can be used to proactively detect configuration issues and guide customers toward best practices.

---

## System Architecture

Campaign Configuration Data (CSV)
↓
Rule-Based Validation Engine
↓
Issue Detection & Severity Classification
↓
Readable Output for Stakeholders



---

## Key Features
- **Automated Configuration Validation:** Detects common campaign setup mistakes.
- **Severity-Based Prioritization:** Classifies issues as HIGH, MEDIUM, or LOW based on potential business impact.
- **Rule-Based Design:** Validation logic is modular and easy to extend.
- **Stakeholder-Friendly Output:** Results are presented in clear, readable language.
- **Scalable Approach:** Designed to handle multiple campaigns consistently.

---

## Technology Stack
- **Python 3** – Core automation and validation logic
- **CSV** – Simulated campaign configuration input
- **Git/GitHub** – Version control and collaboration

---


---

## Validation Rules & Severity
| Rule | Severity |
|-----|----------|
| Max conversions bidding without conversion tracking | HIGH |
| Very low campaign budget | MEDIUM |
| Broad targeting | LOW |

Severity levels help prioritize issues that directly impact conversion measurement and performance.

---

## How to Run

``bash
cd src
python validator.py

Campaign CAMP_002:
 [MEDIUM] Very low daily budget may severely limit performance
 [HIGH] Max conversions bidding without conversion tracking enabled
 [LOW] Broad targeting may reduce relevance


Design Considerations

Validation logic is separated from execution for maintainability.

Severity classification mirrors real-world issue triaging.

The system focuses on prevention rather than reactive troubleshooting.

