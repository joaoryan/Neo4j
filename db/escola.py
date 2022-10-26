from db.database import Graph


class EscolaDB:
    def __init__(self):
        self.db = Graph(uri='bolt://44.195.21.3:7687',
                        user='neo4j', password='task-floats-analysis')

    def create(self, teacher, classroom):
        self.db.execute_query('CREATE (n:Professor {name:$name, age:$age, area:$area}) return n',
                              {'name': teacher['name'], 'age': teacher['age'], 'area': teacher['area']})
        self.db.execute_query('CREATE (n:Materia  {matter:$matter, time:$time}) return n',
                              {'matter': classroom['matter'], 'time': classroom['time']})
        return self.db.execute_query(
            'MATCH (p:Professor {name:$name}), (m:Materia {matter:$matter}) CREATE (p)-[r:Desde {year: $year}]->(m) '
            'RETURN p, r, m',
            {'name': teacher['name'], 'matter': classroom['matter'], 'year': classroom['matterTime']})

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update(self, nameEdit, teacher):
        return self.db.execute_query(
            'MATCH (p:Professor {name:$nameEdit}) SET p.name = $name, p.age = $age, p.area = $area RETURN p',
            {'nameEdit': nameEdit, 'name': teacher['name'], 'age': teacher['age'], 'area': teacher['area']})

    def delete(self, person):
        return self.db.execute_query('MATCH (n:Professor {name:$name}) DELETE n',
                                     {'name': person['name']})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')
