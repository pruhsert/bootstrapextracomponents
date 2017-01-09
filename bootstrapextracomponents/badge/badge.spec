{
	"name": "bootstrapextracomponents-badge",
	"displayName": "Badge",
	"version": 1,
	"definition": "bootstrapextracomponents/badge/badge.js",
	"libraries": [
		{"name":"badge.css", "version":"1.0.0", "url":"bootstrapextracomponents/badge/badge.css", "mimetype":"text/css"}
	],
	"model":
	{
		"enabled" 						: { "type": "enabled", "blockingOn": false, "default": true, "for": ["onAction", "onDoubleClick", "onRightClick"] },
		"displayType" 					: {"type": "string", "default":"BUTTON", "values": ["BUTTON", "LABEL"]},
		"text"							: {"type": "tagstring", "initialValue": "Badge", "tags": { "directEdit" : "true" }},
		"badgeText"						: {"type": "tagstring", "initialValue": "0"},
		"size" 							: {"type" :"dimension",  "default" : {"width":100, "height":40}}, 
    	"location" 						: "point",
    	"styleClass"					: {"type": "styleclass"}
	},
	"handlers": 
	{
		"onAction": 
		{
			"parameters": [
				{
					"name": "event",
					"type": "JSEvent"
				}
			]
		},
		"onDoubleClick": 
		{
			"parameters": [
				{
					"name": "event",
					"type": "JSEvent"
				}
			]
		},
		"onRightClick": 
		{
			"parameters": [
				{
					"name": "event",
					"type": "JSEvent"
				}
			]
		}
	}
}