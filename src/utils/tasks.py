from collections import defaultdict 

tasks = [] # Array of tasks the user gives
completedTask = defaultdict(str) # Add the completed task with time it took to complete


# Method to add a task to tasks
async def add_Task(ctx, taskString):
    
    # If task is already in the array, return
    if taskString in tasks:
        await ctx.send(f"Task: **{taskString}** is already in your list of tasks!")
        return
    
    tasks.append(taskString) # Append the task to 'tasks'
    
    await ctx.send(f"Your Task: **{taskString}** has been added to your list.")
    
    # Display all current tasks
    task_list_msg = "**Your Tasks:**\n"
    
    # Enumerate to get the index and task to print
    for index, task in enumerate(tasks, start = 1):
        task_list_msg += f"{index}. {task}\n"
    await ctx.send(task_list_msg)
    
    
# Method that returns the list of tasks   
async def view_tasks(ctx):
    # Check if tasks is empty, if it is, promt the user and return
    if not tasks:
        await ctx.send(f"There are no current tasks in your list; Please add tasks")
        return
    
    # Display all current tasks
    task_list_msg = "**Your Tasks:**\n"
    
    # Enumerate to get the index and task to print
    for index, task in enumerate(tasks, start = 1):
        task_list_msg += f"{index}. {task}\n"
    await ctx.send(task_list_msg)


# Method to transfer taskes to a dictionary of completed tasks
# completedTask = {task : completion time}
async def complete_Task(ctx, taskString, session):
    
    # Check if this task is not in tasks
    if taskString not in tasks:
        await ctx.send(f"**Task **{taskString}** does not exist in your list of tasks**")
        return

    tasks.remove(taskString) # Remove the task off of tasks since its been completed
    
    # Same time calculation as refered in "endSession.py" method
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    hours, remainder = divmod(int(duration), 3600)
    minutes, seconds = divmod(remainder, 60)
    human_readable = f"{hours:02} hours: {minutes:02} minutes: {seconds:02} seconds"
    
    # Use the task as the key and the time as the value
    completedTask[taskString] = human_readable
    
    # Display all current completed tasks
    completed_tasks_msg = "**Completed Tasks:**\n"
    
    for task, time in completedTask.items():
        completed_tasks_msg += f"- {task}: {time}\n"
    await ctx.send(completed_tasks_msg)


# Method to delete a task from the array 'tasks'
async def delete_task(ctx, taskString):
    
    # If task does not exist, promt the user and return
    if taskString not in tasks:
        await ctx.send(f"Task **{taskString}** does not exist in your list of tasks!")
        return
    
    tasks.remove(taskString) # Remove the task from 'tasks'
    
    await ctx.send(f"task: **{taskString}** has been removed from your task list.")
    
    # Display all current tasks again after deletion
    task_list_msg = "**Your Tasks:**\n"
    for index, task in enumerate(tasks, start = 1):
        task_list_msg += f"{index}. {task}\n"
    await ctx.send(task_list_msg)
    

# Method that clears all current tasks in 'tasks', if empty, promt user
async def clear_tasks(ctx):
   # Check if tasks is empty, if it is, promt the user and return
    if not tasks:
        await ctx.send(f"There are no current tasks in your list; Please add tasks")
        return
    
    tasks.clear()
    
    await ctx.send(f"Task(s) have been cleared")
    
async def remind_task(ctx):
    if not tasks:
        return
    
    # Display all current tasks again after deletion
    task_list_msg = "**Your Remaining Tasks:**\n"
    for index, task in enumerate(tasks, start = 1):
        task_list_msg += f"{index}. {task}\n"
    await ctx.send(task_list_msg)
    
    await ctx.send(f"Please finish your tasks after your break!")
    