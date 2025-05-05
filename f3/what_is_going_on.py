# This file contains complex code that needs explanation
# Ask Copilot to help you understand how these functions work!

from typing import List, Dict, Optional
from datetime import datetime
import re

class TaskScheduler:
    """
    A task scheduler that manages recurring tasks with priorities and dependencies.
    Tasks can be scheduled, executed, and tracked with their dependencies.
    """
    def __init__(self):
        self.tasks: Dict[str, Dict] = {}
        self.dependencies: Dict[str, List[str]] = {}
        self.execution_history: List[Dict] = []
    
    def add_task(self, task_id: str, description: str, 
                 priority: int = 1, dependencies: List[str] = None) -> bool:
        """Adds a new task with optional dependencies"""
        if task_id in self.tasks:
            return False
            
        self.tasks[task_id] = {
            'description': description,
            'priority': priority,
            'status': 'pending',
            'created_at': datetime.now()
        }
        
        if dependencies:
            self.dependencies[task_id] = dependencies
            
        return True
    
    def get_executable_tasks(self) -> List[str]:
        """Returns list of tasks that can be executed (all dependencies met)"""
        executable = []
        
        for task_id, task in self.tasks.items():
            if task['status'] != 'pending':
                continue
                
            if task_id in self.dependencies:
                deps = self.dependencies[task_id]
                if all(self.tasks[dep]['status'] == 'completed' 
                      for dep in deps if dep in self.tasks):
                    executable.append(task_id)
            else:
                executable.append(task_id)
                
        return sorted(executable, 
                     key=lambda x: self.tasks[x]['priority'], 
                     reverse=True)
    
    def execute_task(self, task_id: str) -> Optional[Dict]:
        """Executes a specific task if possible"""
        if task_id not in self.tasks:
            return None
            
        task = self.tasks[task_id]
        if task['status'] != 'pending':
            return None
            
        # Check dependencies
        if task_id in self.dependencies:
            deps = self.dependencies[task_id]
            if not all(self.tasks[dep]['status'] == 'completed' 
                      for dep in deps if dep in self.tasks):
                return None
        
        # Execute task
        task['status'] = 'completed'
        task['completed_at'] = datetime.now()
        
        execution_record = {
            'task_id': task_id,
            'description': task['description'],
            'executed_at': task['completed_at'],
            'dependencies': self.dependencies.get(task_id, [])
        }
        self.execution_history.append(execution_record)
        
        return execution_record

    def get_task_status(self, task_id: str) -> Optional[Dict]:
        """Returns the current status of a task"""
        return self.tasks.get(task_id)


# Example usage and test data
if __name__ == "__main__":
    # Create a scheduler
    scheduler = TaskScheduler()
    
    # Add some tasks with dependencies
    scheduler.add_task('setup_database', 'Initialize database', priority=3)
    scheduler.add_task('load_data', 'Load initial data', 
                      dependencies=['setup_database'], priority=2)
    scheduler.add_task('start_server', 'Start web server', 
                      dependencies=['load_data'], priority=1)
    
    # Print executable tasks (should only be setup_database initially)
    print("\nExecutable tasks:", scheduler.get_executable_tasks())
    
    # Execute tasks in order
    print("\nExecuting tasks:")
    for task_id in ['setup_database', 'load_data', 'start_server']:
        result = scheduler.execute_task(task_id)
        if result:
            print(f"Executed: {result['description']}")
    
    # Print execution history
    print("\nExecution history:")
    for record in scheduler.execution_history:
        print(f"Task: {record['description']}")
        print(f"Dependencies: {record['dependencies']}")
        print(f"Executed at: {record['executed_at']}\n")