from collections import defaultdict 

tasks = []
completedTask = defaultdict(str) # add the completed task with time it took to complete
    
async def add_Task(ctx, taskString):
    tasks.append(taskString)
    
    if taskString in tasks:
        await ctx.send(f"Task: **{taskString}** is already in your list of tasks!")
    
    await ctx.send(f"Your Task: **{taskString}** has been added to your list.")
    
    # displaying all current tasks
    task_list_msg = "**Your Tasks:**\n"
    
    for index, task in enumerate(tasks, start = 1):
        task_list_msg += f"{index}. {task}\n"
    await ctx.send(task_list_msg)
        
async def complete_Task(ctx, taskString, session):
    
    # Check if this task is not in tasks
    if taskString not in tasks:
        await ctx.send(f"**Task **{taskString}** does not exist in your list of tasks**")
        return

    # Remove the task off of tasks since its been completed
    tasks.remove(taskString)
    
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    hours, remainder = divmod(int(duration), 3600)
    minutes, seconds = divmod(remainder, 60)
    human_readable = f"{hours:02} hours: {minutes:02} minutes: {seconds:02} seconds"
       
    completedTask[taskString] = human_readable
        
    completed_tasks_msg = "**Completed Tasks:**\n"
    for task, time in completedTask.items():
        completed_tasks_msg += f"- {task}: {time}\n"
    await ctx.send(completed_tasks_msg)

async def delete_task(ctx, taskString):
    
    if taskString not in tasks:
        await ctx.send(f"Task **{taskString}** does not exist in your list of tasks!")
        return
    
    tasks.remove(taskString)
    
    await ctx.send(f"task: **{taskString}** has been removed from your task list.")
    
    task_list_msg = "**Your Tasks:**\n"
    for index, task in enumerate(tasks, start = 1):
        task_list_msg += f"{index}. {task}\n"
    await ctx.send(task_list_msg)