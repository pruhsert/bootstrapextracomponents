{
	"name": "bootstrapextracomponents-input-group",
	"displayName": "Input Group",
	"version": 1,
	"definition": "bootstrapextracomponents/inputgroup/inputgroup.js",
	"serverscript": "bootstrapextracomponents/inputgroup/inputgroup_server.js",
	"libraries": [
		{"name":"inputgroup.css", "version":"1.0.0", "url":"bootstrapextracomponents/inputgroup/inputgroup.css", "mimetype":"text/css"}
	],
	"model": 
	{
		"dataProvider": 
		{
			"type": "dataprovider",
			"pushToServer": "allow",
			"tags": 
			{
				"scope": "design"
			},
			"ondatachange": 
			{
				"onchange": "onDataChange",
				"callback": "onDataChangeCallback"
			}
		},
		"enabled": 
		{
			"type": "enabled",
			"blockingOn": false,
			"default": true,
			"for": 
			[
				"dataProvider",
				"onAction",
				"onDataChange",
				"onFocusGained",
				"onFocusLost",
				"onRightClick"
			]
		},
		"format": 
		{
			"for": 
			[
				"dataProvider"
			],

			"type": "format"
		},
		"inputType": 
		{
			"type": "string",
			"tags": 
			{
				"scope": "design"
			},

			"default": "text",
			"values": 
			[
				"text",
				"password",
				"number"
			]
		},
		"readOnly": 
		{
			"type": "protected",
			"blockingOn": true,
			"default": false,
			"for": 
			[
				"dataProvider",
				"onDataChange"
			]
		},
		"placeholderText": "tagstring",
		"styleClass": 
		{
			"type": "styleclass",
			"tags": 
			{
				"scope": "design"
			}
		},
		"tabSeq": 
		{
			"type": "tabseq",
			"tags": 
			{
				"scope": "design"
			}
		},
		"visible": "visible",
		"addOns": 
		{
			"type": "AddOn[]"
		},
		"addOnButtons": 
		{
			"type": "AddOnButton[]"
		},
		"size": 
		{
			"type": "dimension",
			"default": 
			{
				"width": 300,
				"height": 40
			}
		}
	},
	"handlers": 
	{
		"onAction": 
		{
			"parameters": 
			[
				{
					"name": "event",
					"type": "JSEvent"
				}
			]
		},
		"onDataChange": 
		{
			"returns": "boolean",
			"parameters": 
			[
				{
					"name": "oldValue",
					"type": "${dataproviderType}"
				},

				{
					"name": "newValue",
					"type": "${dataproviderType}"
				},

				{
					"name": "event",
					"type": "JSEvent"
				}
			]
		},
		"onFocusGained": 
		{
			"parameters": 
			[
				{
					"name": "event",
					"type": "JSEvent"
				}
			]
		},
		"onFocusLost": 
		{
			"parameters": 
			[
				{
					"name": "event",
					"type": "JSEvent"
				}
			]
		},
		"onRightClick": 
		{
			"parameters": 
			[
				{
					"name": "event",
					"type": "JSEvent"
				}
			]
		}
	},
	"api": 
	{
		"requestFocus": 
		{
			"delayUntilFormLoads": true,
			"discardPreviouslyQueuedSimilarCalls": true
		},
		"addAddOn": 
		{
			"parameters": 
			[
				{
					"name": "addOn",
					"type": "bootstrapextracomponents-input-group.AddOn"
				}
			]
		},
		"setAddOns": 
		{
			"parameters": 
			[
				{
					"name": "addOns",
					"type": "bootstrapextracomponents-input-group.AddOn[]"
				}
			]
		},
		"clearAddOns": 
		{
		},
		"addAddOnButton": 
		{
			"parameters": 
			[
				{
					"name": "addOnButton",
					"type": "bootstrapextracomponents-input-group.AddOnButton"
				}
			]
		},
		"setAddOnButtons": 
		{
			"parameters": 
			[
				{
					"name": "addOnButtons",
					"type": "bootstrapextracomponents-input-group.AddOnButton[]"
				}
			]
		},
		"clearAddOnButtons": 
		{
		}
	},
	"types": 
	{
		"AddOn": 
		{
			"text": 
			{
				"type": "tagstring",
				"initialValue": "addOn"
			},
			"position": 
			{
				"type": "string",
				"default": "LEFT",
				"values": 
				[
					"LEFT",
					"RIGHT"
				]
			}
		},
		"AddOnButton": 
		{
			"text": 
			{
				"type": "tagstring",
				"initialValue": "addOn"
			},
			"name":
			{
				"type": "string",
				"initialValue": "btn"
			},
			"position": 
			{
				"type": "string",
				"default": "RIGHT",
				"values": 
				[
					"LEFT",
					"RIGHT"
				]
			},
			"onAction": 
			{
				"type": "function"
			},
			"onDoubleClick": 
			{
				"type": "function"
			},
			"onRightClick": 
			{
				"type": "function"
			},
			"styleClass": 
			{
				"type": "styleclass",
				"default": "btn-default"
			},
			"imageStyleClass": 
			{
				"type": "styleclass"
			}
		}
	}
}