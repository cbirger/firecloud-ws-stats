from firecloud import fiss

def list_workspaces(project=project):
    class MyInputParams(object):
        project=project
    args=MyInputParams()
    return (fiss.space_list(args))

