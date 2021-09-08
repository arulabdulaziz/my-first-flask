schema_register = {
  "type": "object",
  "properties": {
    "name": { 
        "type": "string",
      "minLength": 1, 
    },
    "email": {
      "title": "Email",
      "type": "string",
      "format": "email",
      "pattern": "^\\S+@\\S+\\.\\S+$",
    },
    "password": {
      "title": "Password",
      "type": "string",
      "minLength": 8,
    },
  },
  "required": ["name", "email", "password"]
}
schema_login = {
  "type": "object",
  "properties": {
    "email": {
      "title": "Email",
      "type": "string",
      "format": "email",
      "pattern": "^\\S+@\\S+\\.\\S+$",
    },
    "password": {
      "title": "Password",
      "type": "string",
      "minLength": 8,
    },
  },
  "required": ["email", "password"]
}