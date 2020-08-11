from model.project import Project
from random import randrange

from model.project import Project
from random import randrange


def test_delete_project(app):
    project = Project(name="testname", description="desc")
    if len(app.soap.project_list(username="administrator", password="root")) == 0:
        app.project.add_project(project)
    old_projects = app.soap.project_list(username="administrator", password="root")
    index = randrange(len(old_projects))
    deleted_project = old_projects[index]
    app.project.delete_project_by_name(deleted_project.name)
    new_projects = app.soap.project_list(username="administrator", password="root")
    old_projects.remove(project)
    assert old_projects == new_projects