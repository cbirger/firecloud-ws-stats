from firecloud import fiss

def list_workspaces(project=None):
    class MyInputParams:
        def __init__(self, project):
            self.project = project
    args=MyInputParams(project)
    return (fiss.space_list(args))

def get_workspace_info(project, workspace):
    class MyInputParams:
        def __init__(self, project, workspace):
            self.project = project
            self.workspace = workspace
    args = MyInputParams(project, workspace)
    return (fiss.space_info(args))

