from model.project import Project


def test_add_project(app, orm):
    app.session.login("administrator", "root")
    project = Project(name="test", description="test")
    if Project(name=project.name) in orm.get_existing_project(Project(name=project.name)):
        app.project.delete_project_by_name(project.name)
    old_projects = orm.get_project_list()
    app.project.add_project(project)
    new_projects = orm.get_project_list()
    old_projects.append(project)
    assert old_projects == new_projects
    app.session.logout()