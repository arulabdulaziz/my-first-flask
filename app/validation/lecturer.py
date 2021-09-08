schema = {
    "type": "object",
  "properties": {
    "name": { "type": "string",
      "minLength": 1, 
    },
    "nidn": { "type": "string",
      "minLength": 5,
    }
  },
  "required": ["name", "nidn"]
}