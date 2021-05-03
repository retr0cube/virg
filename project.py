import neptune_lib as Neptune

descr = "Hi! This is My Addon "

Project = Neptune.createProject("myAddon","1.16.210", descr)
Project.projectVersion(1,0,0)
Project.Res(True)
Project.Beh(True)

Neptune.init("adm","1.16.100")
Neptune.init.Item("fgfg")
