# Simple To-Do List Application

This is a basic command-line To-Do List Application implemented in Python. The program allows users to manage their tasks interactively by adding, viewing, deleting tasks, and quitting the application.

## Features

1. **Add Tasks:**
   - Users can add tasks to their to-do list.
   - Tasks are stored in a Python list for temporary storage during the session.

2. **View Tasks:**
   - Displays the current tasks in the list with their index numbers.
   - Alerts the user if the list is empty.

3. **Delete Tasks:**
   - Lists all tasks before deletion for easy selection.
   - Users can delete tasks by entering the exact task name.
   - Alerts the user if the task does not exist in the list.

4. **Quit Application:**
   - Allows users to exit the application.

## How to Use

1. Copy and paste the code into a Python environment (e.g., VS Code, PyCharm, or a Python shell).
2. Run the program.
3. Interact with the application through the menu options displayed:
   - Type `add` to add a task.
   - Type `view` to view the current task list.
   - Type `delete` to remove a specific task.
   - Type `quit application` to exit the program.

## Requirements

- Python 3.x

## Example Usage

```
Welcome, what are you looking to do today? add, view, delete, or quit application.
> add
What task would you like to add? Complete homework

Welcome, what are you looking to do today? add, view, delete, or quit application.
> view
Your tasks are:
1. Complete homework

Welcome, what are you looking to do today? add, view, delete, or quit application.
> delete
Your tasks are:
1. Complete homework

Enter the task you would like to delete: Complete homework
'Complete homework' has been deleted.

Welcome, what are you looking to do today? add, view, delete, or quit application.
> quit application
Have a good day!
```

## Known Issues

- The `index` variable in the `view` block does not increment correctly, resulting in repeated values.
- Tasks are case-sensitive when deleting. Enter the exact name of the task for successful deletion.
- Tasks are not persisted between program runs since the list is only stored in memory.

## Future Improvements

- Fix the index increment issue for task numbering.
- Add case-insensitive matching for task deletion.
- Save tasks to a file or database for persistence.
- Implement more robust input validation.

## Notes

- Ensure you type the task name correctly (case and spaces) when deleting.
- The application is suitable for basic session-based task management.

## License

This project is open-source and free to use.

