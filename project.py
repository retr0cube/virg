import neptune_lib as Neptune

descr = "Hi! This is My Addon "
#
# Project = Neptune.createProject("myAddon","1.16.210", descr)
# Project.projectVersion(1,0,0)
# Project.Res(True)
# Project.Beh(True)
#
# Neptune.init("&","&").Item("dskd")

MAIN = Neptune.Init('NeptuneDummy')
MAIN.createDependencies(True, True)
MAIN.projectVersion(0,0,1)
MAIN.createManifest(True, True ,descr)
# Neptune.init.Res(True)
# Neptune.init.Beh(True)
