ADD_MEMORY_TOOL = {
    "name": "add_memory",
    "description": "Add a new memory",
    "parameters": {
        "data": {
            "type": "string",
            "description": "Content of the memory to add"
        }
    }
}

UPDATE_MEMORY_TOOL = {
    "name": "update_memory",
    "description": "Update an existing memory",
    "parameters": {
        "memory_id": {
            "type": "string",
            "description": "ID of the memory to update"
        },
        "data": {
            "type": "string",
            "description": "New content for the memory"
        }
    }
}

DELETE_MEMORY_TOOL = {
    "name": "delete_memory",
    "description": "Delete an existing memory",
    "parameters": {
        "memory_id": {
            "type": "string",
            "description": "ID of the memory to delete"
        }
    }
}
