# Automotive Industry Graph

Mini-project for exploring automotive company dependencies using:
- Docker
- Neo4j
- Python

## Start

Open terminal inside project folder and run:

```bash
docker compose up -d
```

Neo4j Browser:
http://localhost:7474

Login:
- username: neo4j
- password: password123

## Install Python packages

```bash
pip install -r requirements.txt
```

## Load demo graph

```bash
python scripts/load_data.py
```

# Automotive Industry Intelligence Graph

## Overview

Automotive Industry Intelligence Graph is a graph-based analytical platform designed to explore relationships, dependencies, and geopolitical risks inside the global automotive ecosystem.

The project combines:

* graph databases,
* financial analytics,
* supply chain intelligence,
* geopolitics,
* energy markets,
* and automotive industry data.

The system models the automotive world as a connected network instead of isolated tables.

---

# Core Idea

Modern automotive companies are deeply interconnected.

A single event such as:

* semiconductor shortages,
* lithium price spikes,
* trade sanctions,
* energy crises,
* geopolitical conflicts,
* or new environmental regulations

can affect dozens of manufacturers simultaneously.

Traditional relational databases struggle to represent multi-level dependency chains efficiently.

This project uses Neo4j to build an interactive knowledge graph capable of modeling:

* automotive manufacturers,
* suppliers,
* battery producers,
* semiconductor companies,
* raw material dependencies,
* geopolitical events,
* logistics risks,
* partnerships,
* competition,
* and market influence.

---

# Example Relationships

Tesla

* DEPENDS_ON → CATL
* USES → Lithium
* AFFECTED_BY → US-China Tariffs

BMW

* SUPPLIED_BY → Bosch
* EXPOSED_TO → Energy Prices

TSMC

* LOCATED_IN → Taiwan

---

# Technologies

## Backend

* Python
* Neo4j
* Docker

## Data Sources

* Financial APIs
* Commodity APIs
* News APIs
* Public datasets
* SEC filings
* Wikipedia parsing

## Future Stack

* React
* D3.js
* Graph Data Science
* NLP pipelines
* AI summarization systems

---

# Main Goals

## 1. Supply Chain Visualization

Explore multi-level supplier dependencies across the automotive industry.

## 2. Risk Propagation Analysis

Simulate how geopolitical or economic disruptions spread through the network.

## 3. Influence Mapping

Identify critical suppliers, bottlenecks, and highly connected companies.

## 4. Historical Transformation Tracking

Analyze how manufacturers evolve:

* EV transition,
* battery strategies,
* energy exposure,
* supplier diversification.

## 5. News-to-Graph Intelligence

Automatically extract relationships from financial and geopolitical news articles.

---

# Example Use Cases

* Which manufacturers are most exposed to lithium shortages?
* What companies indirectly depend on Taiwan semiconductor production?
* Which suppliers are central to EV manufacturing?
* How could energy price increases impact German automakers?
* Which companies are structurally connected through shared suppliers?

---

# Architecture

Python Data Pipelines
↓
API / News Collection
↓
Neo4j Knowledge Graph
↓
Graph Analytics
↓
Interactive Dashboard

---

# Future Development

* Real-time market monitoring
* Automated news ingestion
* Graph machine learning
* Risk scoring systems
* Temporal graph analysis
* AI-generated industry summaries
* Interactive geopolitical simulation

---

# Vision

The long-term vision is to create an industrial-scale automotive intelligence platform capable of combining:

* engineering relationships,
* financial dependencies,
* supply chain structures,
* and geopolitical dynamics

inside one connected graph system.


## Example Cypher query

```cypher
MATCH (n)
RETURN n
```
