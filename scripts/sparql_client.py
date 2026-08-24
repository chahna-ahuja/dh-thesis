# scripts/sparql_client.py
#to build a sparql utility module to access the golem database for bts fanfiction published on archive of our own

from SPARQLWrapper import SPARQLWrapper, JSON


ENDPOINT = "http://194.171.203.17:8890/sparql"


class SPARQLClient:
    def __init__(self):
        self.sparql = SPARQLWrapper(ENDPOINT)
        self.sparql.setReturnFormat(JSON)

    def query(self, query: str):
        self.sparql.setQuery(query)
        return self.sparql.query().convert()

    def select(self, query: str):
        results = self.query(query)
        return results["results"]["bindings"]