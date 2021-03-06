def help():
    print("Help for Checker CLI:")
    print("")
    print("\033[1mCommands:\033[0m")
    print("\tstatus <project_id> [task_num]\t: Gets the status of a "+
          "certain project or task")
    print("\t\tproject_id\t: The ID of the project to get the " +
          "status of, \n\t\t\t\t  or contains the task to get the status of")
    print("\t\ttask_num\t: (Optional) The number of the task to " +
          "get the status of")
    print("\t\t\033[1mColor Code:\033[0m (When getting project status)")
    print("\t\t\t\033[0mWhite\t: Task has not been checked with CheckerCLI")
    print("\t\t\t\033[32mGreen\033[0m\t: Task has passed all checks")
    print("\t\t\t\033[31mRed\033[0m\t: Task has not passed all checks")
    print("")
    print("\tcheck <project_id> <task_num>\t: Checks a certain task")
    print("\t\tproject_id\t: The ID of the project that has the task to check")
    print("\t\ttask_num\t: The number of the task to check")
    print("\t\t\033[1mColor Code:\033[0m")
    print("\t\t\t\033[0m\u2713/\u2717\t: Requirement check pass/fail")
    print("\t\t\t\033[1;32m\u2713\033[0m/\033[1;31m\u2717\033[0m\t: Code check pass/fail")
    print("\t\t\t\033[1;95m\u2713\033[0m/\033[1;93m\u2717\033[0m\t: Efficiency check pass/fail")
    print("\t\t\t\033[1;34m\u2713\033[0m/\033[1;33m\u2717\033[0m\t: Text answer  pass/fail")
    print("")
    print("\trefresh\t: Prompts credential refresh")
    print("")
    #print("\trun\t: Pushes code and runs checker")
   # print("\t\t-d{n}\t: Dry mode. Runs checker for task `n` without " +
   #       "pushing new code. \n\t\t\t  Note: `n` should be the number next " +
   #       "to the task, not the file prefix.")
   # print("")
    print("\t -h, --help\t: Shows this help output")
    print("")
