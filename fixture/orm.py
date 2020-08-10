from pony.orm import *
from model.project import Project


class ORMFixture:
    db = Database()

    class ORMProject(db.Entity):
        _table_ = 'mantis_project_table'
        name = Optional(str, column="name")
        description = Optional(str, column="description")

    def __init__(self, host, user, password, db):
        self.db.bind("mysql", host=host, user=user, password=password, db=db)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project(name=project.name, description=project.description)
        return list(map(convert, projects))

    @db_session
    def get_existing_project(self, project):
        return self.convert_projects_to_model(select(g for g in ORMFixture.ORMProject if g.name == project.name))

    @db_session
    def get_project_list(self):
        return self.convert_projects_to_model(select(c for c in ORMFixture.ORMProject))