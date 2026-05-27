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

## Example Cypher query

```cypher
MATCH (n)
RETURN n
```
