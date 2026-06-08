from pydantic import BaseModel


class ProjectModel(BaseModel):
    title:str
    desc:str

