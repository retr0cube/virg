import neptune_lib as Neptune


Project = Neptune.createProject("mih","1.16.210",["items","blocks","textures"])
Project.Res(True)
Project.Bes(True)
