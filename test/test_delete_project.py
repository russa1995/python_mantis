from model.project import Project
from random import randrange


def test_delete_project(app, orm):
    app.session.login("administrator", "root")
    project = Project(name="test", description="test")
    if len(orm.get_project_list()) == 0:
        app.project.add_project(project)
    old_projects = orm.get_project_list()
    index = randrange(len(old_projects))
    deleted_project = old_projects[index]
    app.project.delete_project_by_name(deleted_project.name)
    new_projects = orm.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects
    app.session.logout()