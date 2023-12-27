
## Mockoon Locust Poetry
My first project with Locust | Meu primeiro Projeto com Locust

#### swagger public api doc
>[swagger](https://app.swaggerhub.com/apis/GUSTAVOCAMPOSANTUNES_1/locust-demo/1.0.0)

#### mockoon environment JSON example
```
{
  "openapi": "3.0.0",
  "info": {
    "title": "Locust poetry provadeconceito",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "http://localhost:3004/api/locust-demo"
    }
  ],
  "paths": {
    "/hello": {
      "get": {
        "description": "My first test with locust",
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "example": {}
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "schema": {
                  "type": "string"
                },
                "example": "*"
              },
              "Access-Control-Allow-Methods": {
                "schema": {
                  "type": "string"
                },
                "example": "GET"
              },
              "Access-Control-Allow-Headers": {
                "schema": {
                  "type": "string"
                },
                "example": "Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With"
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "example": "{\n  \"version\": \"1.1.0\",\n  \"data\": {\n    \"error\": {\n      \"code\": \"404\",\n      \"message\": \"Not Found\"\n    }\n  }\n}"
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "schema": {
                  "type": "string"
                },
                "example": "*"
              },
              "Access-Control-Allow-Methods": {
                "schema": {
                  "type": "string"
                },
                "example": "GET"
              },
              "Access-Control-Allow-Headers": {
                "schema": {
                  "type": "string"
                },
                "example": "Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With"
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "example": "{\n  \"version\": \"1.1.0\",\n  \"data\": {\n    \"error\": {\n      \"code\": \"500\",\n      \"message\": \"Internal Server Error\"\n    }\n  }\n}"
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "schema": {
                  "type": "string"
                },
                "example": "*"
              },
              "Access-Control-Allow-Methods": {
                "schema": {
                  "type": "string"
                },
                "example": "GET"
              },
              "Access-Control-Allow-Headers": {
                "schema": {
                  "type": "string"
                },
                "example": "Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With"
              }
            }
          },
          "502": {
            "description": "",
            "content": {
              "application/json": {
                "example": "{\n  \"version\": \"1.1.0\",\n  \"data\": {\n    \"error\": {\n      \"code\": \"502\",\n      \"message\": \"Bad Gateway\"\n    }\n  }\n}"
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "schema": {
                  "type": "string"
                },
                "example": "*"
              },
              "Access-Control-Allow-Methods": {
                "schema": {
                  "type": "string"
                },
                "example": "GET"
              },
              "Access-Control-Allow-Headers": {
                "schema": {
                  "type": "string"
                },
                "example": "Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With"
              }
            }
          }
        }
      }
    },
    "/create-account": {
      "post": {
        "description": "",
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "example": "{\n    \"version\": \"1.1\",\n    \"success\": true,\n    \"data\": {\n        \"token\": {\n            \"access\": {\n                \"token\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTI0LCJlbWFpbCI6IkdVU1RBVk8uQU5UVU5FU0BJTkZPWE5FVC5DT00uQlIiLCJjbGllbnRJZCI6MzQsImRvYyI6IjY3NTE5Mjk4MDM1IiwiZmlyc3ROYW1lIjoiR1VTVEFWTyIsImlhdCI6MTcwMzI1MzMxOCwiZXhwIjoxNzAzMjU2OTE4LCJzdWIiOiJHVVNUQVZPLkFOVFVORVNASU5GT1hORVQuQ09NLkJSIn0.5TgPeS9i3myJilbjyigIzbANTq2oj9yAcXgBqSGYOxI\",\n                \"expiresIn\": 360000000000\n            },\n            \"refresh\": {\n                \"token\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDMyNTMzMTgsImV4cCI6MTcwMzI5NjUxOH0.BqG6_fBJBH2sDNwQX8nztM666ooqcH-uTZFOqqEuXlU\",\n                \"expiresIn\": 432000000000\n            }\n        }\n    }\n}"
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "schema": {
                  "type": "string"
                },
                "example": "*"
              },
              "Access-Control-Allow-Methods": {
                "schema": {
                  "type": "string"
                },
                "example": "GET"
              },
              "Access-Control-Allow-Headers": {
                "schema": {
                  "type": "string"
                },
                "example": "Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With"
              }
            }
          }
        }
      }
    }
  }
}
```

#### basic comand
```
$ poetry install
```

#### run testing tool on port 8089
```
$ locust
```

### More Info
> [poetry-commands](https://python-poetry.org/docs/cli/)

> [mockoon](https://python-poetry.org/docs/cli/)

> [locust](https://docs.locust.io/en/stable/)
