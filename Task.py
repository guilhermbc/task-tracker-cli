from datetime import datetime

class Task:
    def __init__(self, description: str, id: int, createdAt: str, updatedAt: str, status: str = 'todo'):
        now = datetime.now().isoformat()

        self.id = id
        self.description = description
        self.createdAt = createdAt or now
        self.updatedAt = updatedAt or now
        self.status = status # 'todo', 'in-progress', 'done'
        
    def __str__(self):
        return (f'{self.id} - {self.description} ({self.status}) | Last updated at: {self.updatedAt}\n')

    def mark_in_progress(self):
        self.status = 'in-progress'
        self.touch()

    def mark_done(self):
        self.status = 'done'
        self.touch()

    def update_description(self, new_description: str):
        self.description = new_description
        self.touch()

    def touch(self):
        """Updates the updatetAt attribute to the current datetime"""
        self.updatedAt = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Converts the Task object to a dictionary (ready for JSON)"""
        return {'id': self.id,
                'description': self.description,
                'status': self.status,
                'createdAt': self.createdAt,
                'updatedAt': self.updatedAt
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Creates a Task instance from a JSON dictionary"""
        return cls(
            id=data['id'],
            description=data["description"],
            status=data["status"],
            createdAt=data["createdAt"],
            updatedAt=data["updatedAt"],
        )