from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "password123"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

query = '''
CREATE
(tesla:Company {name:'Tesla'}),
(bmw:Company {name:'BMW'}),
(toyota:Company {name:'Toyota'}),
(catl:Supplier {name:'CATL'}),
(tsmc:Supplier {name:'TSMC'}),
(bosch:Supplier {name:'Bosch'}),
(lithium:Resource {name:'Lithium'}),
(china:Country {name:'China'}),
(eu:Region {name:'European Union'}),

(tesla)-[:DEPENDS_ON]->(catl),
(catl)-[:USES]->(lithium),
(catl)-[:LOCATED_IN]->(china),

(bmw)-[:DEPENDS_ON]->(bosch),
(bmw)-[:DEPENDS_ON]->(tsmc),

(tsmc)-[:LOCATED_IN]->(china),

(toyota)-[:COMPETES_WITH]->(tesla),
(bmw)-[:AFFECTED_BY]->(eu)
'''

with driver.session() as session:
    session.run(query)

driver.close()

print("Graph loaded successfully.")