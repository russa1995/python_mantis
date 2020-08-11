from model.project import Project


def test_add_project(app):
    project = Project(name="testname", description="desc")
    if project.name in app.soap.get_existing_project("administrator", "root"):
        app.project.delete_project_by_name(project.name)
    old_projects = app.soap.project_list("administrator", "root")
    app.project.add_project(project)
    new_projects = app.soap.project_list("administrator", "root")
    old_projects.append(project)
    assert old_projects == new_projects