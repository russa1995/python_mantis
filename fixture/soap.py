from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl']+"api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def project_list(self, username, password):
        client = Client(self.app.config['web']['baseUrl']+"api/soap/mantisconnect.php?wsdl")
        list = []
        try:
            for project in client.service.mc_projects_get_user_accessible(username, password):
                name = project.name
                description = project.description
                list.append(Project(name=name, description=description))
            return list

        except WebFault:
            return False

    def get_existing_project(self, username, password):
        client = Client(self.app.config['web']['baseUrl']+"api/soap/mantisconnect.php?wsdl")
        list = []
        try:
            for project in client.service.mc_projects_get_user_accessible(username, password):
                name = project.name
                list.append(name)
            return list

        except WebFault:
            return False