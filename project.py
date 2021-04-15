import neptune_lib as Neptune


Neptune.Name.proj_name = "My ADDON"
Project = Neptune.createProject("1.16.210")
Project.Beh(True)
Project.Res(True)