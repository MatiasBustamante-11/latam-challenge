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

    422: {
        "description": "ValidationError",
        "content": {
            "application/json": {
                "examples": {
                    "default": {
                        "summary": "Validation error",
                        "value": { "details": [
                            {
                                "parameter": "mes",
                                "message": "ensure this value is less than or equal to 12"
                            },
                            {
                                "parameter": "opera",
                                "message": "value is not a valid enumeration member"
                            }
                        ],
                        "message": "Unable to process your request due to invalid data"}
                    },
                }
            }
        }
    },

}