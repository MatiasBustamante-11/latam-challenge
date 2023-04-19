ml_response_codes = {

    404: {

        "description": "Error",

        "content": {

            "application/json": {

                "examples": {

                    "default": {

                        "summary": "Not found",

                        "value": { "detail": "Not found error",}

                    },

                }

            }

        }

    },

    500: {

        "description": "InternalServerError",

        "content": {

            "application/json": {

                "examples": {

                    "default": {

                        "summary": "Server error",

                        "value": { "message": "Could not process your request, please retry later",}

                    },

                }

            }

        }

    },

}