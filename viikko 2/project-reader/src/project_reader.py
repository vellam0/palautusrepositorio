from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(data['tool']['poetry']['name'], 
                       data['tool']['poetry']['description'],
                       data['tool']['poetry']['license'],
                       ", ".join(data['tool']['poetry']['authors']),
                       data['tool']['poetry']['dependencies'].keys(), 
                       data['tool']['poetry']['group']['dev']['dependencies'].keys())