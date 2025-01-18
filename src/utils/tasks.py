from collections import defaultdict 

tasks = [] # Array of tasks the user gives
completedTask = defaultdict(str) # Add the completed task with time it took to complete


async def add_Task(ctx, taskString):
    """
    Method to add a task to an array 'tasks'.

    Args:
        ctx (_type_): discord API context.
        taskString (str): Task string given by the user.
    """
    
    # If task is already in the array, return
    if taskString in tasks:
        await ctx.send(f"Task: **{taskString}** is already in your list of tasks!")
        return
    
    tasks.append(taskString) # Append the task to 'tasks'
    
    await ctx.send(f"Your Task: **{taskString}** has been added to your list.\nType **!viewTasks** to view your tasks")
    
      
async def view_tasks(ctx):
    """
    Method that returns the list of tasks

    Args:
        ctx (_type_): discord API context.
    """
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


async def complete_Task(ctx, taskString, session):
    """
    Method to transfer taskes to a dictionary of completed tasks
    completedTask = {task : completion time}

    Args:
        ctx (_type_): discord API context.
        taskString (str): Task string given by the user.
        session (session): Data Class to initilize a session with: :is_active: bool [false], :start_time: int [0].
    """
    
    # Check if this task is not in tasks
    if taskString not in tasks:
        await ctx.send(f"**Task **{taskString}** does not exist in your list of tasks**")
        return

    tasks.remove(taskString) # Remove the task off of tasks since its been completed
    
    # Same time calculation as refered in "endSession.py" method
    if session.is_active:
        end_time = ctx.message.created_at.timestamp()
        duration = end_time - session.start_time
        hours, remainder = divmod(int(duration), 3600)
        minutes, seconds = divmod(remainder, 60)
        human_readable = f"Completion time: {hours:02} hours: {minutes:02} minutes: {seconds:02} seconds"
    else:
        human_readable = f"No completion time"
    
    # Use the task as the key and the time as the value
    completedTask[taskString] = human_readable
    
    await ctx.send(f"You have completed task: **{taskString}**; well done.\nType **!viewCompletedTasks** to view your completed tasks.")
    

async def view_completed_tasks(ctx):
    """
    Method that returns the list of completed tasks.

    Args:
        ctx (_type_): discord API context.
    """

    if not completedTask:
        await ctx.send(f"There are no current completed tasks in your list.")
        return
    
    # Display all current completed tasks
    completed_tasks_msg = "**Completed Tasks:**\n"
    
    for task, time in completedTask.items():
        completed_tasks_msg += f"- {task}: {time}\n"
    await ctx.send(completed_tasks_msg)


async def delete_task(ctx, taskString):
    """
    Method to delete a task from the list of tasks

    Args:
        ctx (_type_): discord API context.
        taskString (str): Task string given by the user.
    """
    
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
    

async def clear_tasks(ctx):
    """
    Method that clears all current tasks in the list of tasks, if empty, promt user.

    Args:
        ctx (_type_): discord API context.
    """
   # Check if tasks is empty, if it is, promt the user and return
    if not tasks:
        await ctx.send(f"There are no current tasks in your list; Please add tasks")
        return
    
    # Use the clear method to delete all tasks
    tasks.clear()
    
    await ctx.send(f"Task(s) have been cleared")
    
async def remind_task(ctx):
    """
    Method to remind the user of tasks left in their list when reminded to take a break.

    Args:
        ctx (_type_): discord API context.
    """
    if not tasks:
        return
    
    # Display all current tasks
    task_list_msg = "**Your Remaining Tasks:**\n"
    for index, task in enumerate(tasks, start = 1):
        task_list_msg += f"{index}. {task}\n"
    await ctx.send(task_list_msg)
    
    await ctx.send(f"Please finish your tasks after your break!")
    