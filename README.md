# Media System as a Victory Factor in Armed Conflict

> **Research:** «Медиасистема как фактор победы в современном военном конфликте: парадокс недооценки и инструментализация коммуникаций»
> 
> **Author:** Sergey V. Vodopetov, PhD (RUDN University, Moscow)
> 
> **ORCID:** [0000-0002-5237-4464](https://orcid.org/0000-0002-5237-4464) | **RSCI ID:** 835749 | **SPIN:** 5530-2581

[![Open Science](https://img.shields.io/badge/Open%20Science-FAIR-blue)](https://www.go-fair.org/fair-principles/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## 📖 About This Research

This study examines the role of modern media systems in armed conflicts (2023–2026). The central thesis: media communications have transformed from auxiliary information support into a **strategic factor** capable of influencing conflict outcomes on par with conventional weapons.

### Research Question

How does the media system function as an **objective actor** in armed conflicts — through structural characteristics (algorithms, platform architecture, network topology) rather than solely through agent intentions (propaganda, intentional information operations)?

### Three Conflicts Analyzed

| Conflict | Period | Key Media Events |
|----------|--------|-----------------|
| **Russia-Ukraine** | 2023–2026 | Battle of Avdiivka, Kursk raid, 2025 escalation |
| **Palestine-Israel** | Oct 2023–2026 | October 7 attack, Gaza coverage, global attention surge |
| **USA-Iran / Middle East** | Apr 2024–2026 | Damascus consulate strike, escalation cycle |

### Key Thesis

> The media system most often suffers defeat **not from the enemy, but from its own military command**, which continues to perceive media resources as a threat to operational security, a source of leaks, and a tool for revealing secrets.

In areas where media can bring maximum benefit — **humanitarian information, enemy disorientation, POW surrender channels, societal mobilization, international support formation** — full communication support is often either not provided at all or viewed as working against interests, because it requires special skills, tools, and thinking alien to classical military planning.

---

## 📊 KPI Framework / KPI-фреймворк влияния

Five categories of media system influence on armed conflicts:

| Category | Description | Mechanism |
|----------|-------------|-----------|
| **1. Humanitarian Information** | Informing about civilian casualties, infrastructure damage, refugee flows | Creates international pressure, influences humanitarian corridors |
| **2. Enemy Disorientation** | Information operations targeting opponent's decision-making | Degrades command and control, creates confusion |
| **3. POW/Surrender Channels** | Creating communication pathways for capitulation | Reduces resistance, saves lives |
| **4. Societal Mobilization** | Domestic audience engagement and morale | Affects recruitment, support for war effort |
| **5. International Support Formation** | Building coalition of external actors | Influences sanctions, arms supplies, diplomatic stance |

---

## 📁 Repository Structure

```
warandmedia/
├── README.md                          # This file
├── CITATION.cff                       # Citation metadata
├── LICENSE                            # CC BY 4.0
│
├── data/
│   ├── events_master.csv              # Master dataset of media events
│   ├── events_russia_ukraine.csv      # Russia-Ukraine conflict events
│   ├── events_palestine_israel.csv    # Palestine-Israel conflict events
│   ├── events_usa_iran.csv            # USA-Iran/Middle East events
│   └── sources.csv                    # Source registry
│
├── methodology/
│   ├── sampling_protocol.md           # Sampling design and unit of analysis
│   ├── kpi_framework.md               # Five-category influence framework
│   ├── inclusion_exclusion_criteria.md # PRISMA-style criteria
│   ├── codebook.md                    # Coding definitions
│   └── limitations.md                 # Limitations and ethical disclaimer
│
├── results/
│   ├── key_findings.md                # Summary of quantitative findings
│   ├── conflict_comparison.md         # Cross-conflict analysis
│   └── historiography.md            # Historical context (WWI, WWII)
│
└── metadata/
    ├── CITATION.cff
    └── dataset_metadata.json
```

---

## 🔬 Methodology at a Glance

### Unit of Analysis
**Discrete media event** with identifiable influence on military, political, or diplomatic outcome of armed conflict. Each unit records:
1. Media event — what happened in the media system
2. Conflict event — what happened in military/political/diplomatic sphere
3. Causal mechanism linking them
4. Evidence that influence occurs through **structural characteristics** of media system (objectivity), not agent intentions (subjectivity)

### Source Types
| Type | Examples |
|------|----------|
| Academic databases | Google Scholar, CyberLeninka, eLibrary, Scopus |
| Mass media | Reuters, BBC, Al Jazeera, NPR, CNN, NYT |
| Think tanks | CSIS, RAND, Atlantic Council, FDD, ISD, ISW |
| OSINT organizations | Bellingcat, CIT, DFR Lab |
| International organizations | UN, ICC, WHO, UNHCR |
| Press freedom monitors | CPJ, RSF, ECPMF |
| Social media analytics | Telegram channels, X/TikTok/Meta public reports |

### Period
**October 2023 – March 2026**

---

## 📊 Data Sample / Пример данных

See `data/events_master.csv` for full dataset. Sample record:

| Field | Example |
|-------|---------|
| event_id | RU_001 |
| conflict | Russia-Ukraine |
| date | 2024-02-17 |
| media_event | Telegram channels report Avdiivka encirclement in real time |
| conflict_event | Ukrainian forces withdraw from Avdiivka |
| kpi_category | Enemy Disorientation |
| mechanism | Real-time OSINT creates information vacuum for Ukrainian command |
| structural_feature | Platform architecture (Telegram) + personal channels + geolocation |
| source_url | [Source] |
| verification_status | Verified via multiple OSINT sources |

---

## 📜 License

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

---

## 📚 How to Cite

### APA 7
Vodopetov, S. V. (2025). *Media system as a victory factor in modern armed conflict: The paradox of underestimation and the instrumentalization of communications*. [Journal name]. https://github.com/MediaCod22/warandmedia

### ГОСТ
Водопетов С.В. Медиасистема как фактор победы в современном военном конфликте: парадокс недооценки и инструментализация коммуникаций // [Журнал]. — 2025. — № X. — С. XX–XX.

---

## ⚠️ Ethical Disclaimer

This repository documents **openly available information** about media events in armed conflicts. It does **not** contain:
- Classified military information
- Personal data of non-public individuals
- Content inciting violence or hatred
- Graphic materials

The research follows principles of **responsible data science** and **journalistic ethics**. All sources are publicly accessible without paid subscription.

---

*Repository created: 2026-05-14 | Open Science compliant | FAIR principles*