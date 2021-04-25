import json
import neptune_lib
import uuid

mnifst = {
	"format_version": 2,
	"header": {
		"name": "pdf" ,
		"description": "fre",
		"uuid": str(uuid.uuid1),
		"version": [
			1,
			0,
			0
		],
		"min_engine_version": [
			1,
			13,
			0
		]
	},
	"modules": [
		{
			"type": "resources",
			"uuid": str(uuid.uuid3),
			"version": [
				1,
				0,
				0
			]
		}
	]
}
