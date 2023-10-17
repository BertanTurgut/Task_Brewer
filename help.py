command_dict = dict()
command_dict["help"] = "Prints available commands for main tab."
command_dict["exit"] = "Stores the complete data and terminates program."
command_dict["exit without save"] = "Terminates program without saving any changed data."
command_dict["active"] = "Lists active tasks and selects the \"actives\" tab."
command_dict["completed"] = "Lists completed tasks."
command_dict["cancelled"] = "Lists cancelled tasks."
command_dict["missed"] = "Lists missed tasks."
command_dict["add task"] = "Adds task."
command_dict["search"] = "Asks for an input string and tries to find this string in all tasks."
command_dict["search in active"] = "Asks for an input string and tries to find this string in active tasks."
command_dict["search in completed"] = "Asks for an input string and tries to find this string in completed tasks."
command_dict["search in cancelled"] = "Asks for an input string and tries to find this string in cancelled tasks."
command_dict["search in missed"] = "Asks for an input string and tries to find this string in missed tasks."
command_dict["\"actives\"->search"] = "Asks for an input string and tries to find this string in active tasks."
command_dict["\"actives\"->help"] = "Prints available commands for actives tab."
command_dict["\"actives\"->edit task"] = "Edits task by selection."
command_dict["\"actives\"->cancel task"] = "Cancels task by selection."
command_dict["\"actives\"->complete task"] = "Completes task by selection."
command_dict["\"actives\"->list"] = "Lists active tasks."
command_dict["\"actives\"->exit"] = "Exits \"actives\" tab and returns main tab."

def helpString(path: str = "all"):
    help_string = ""
    command_list = []
    for command in command_dict.keys():
        command_list.append(command)
    command_list.sort()
    for command in command_list:
        match path:
            case "all":
                help_string += f"{command : <40}{command_dict[command]}\n"
            case "main":
                if command[0] != "\"":
                    help_string += f"{command : <40}{command_dict[command]}\n"
            case "actives":
                if command[:9] == "\"actives\"":
                    help_string += f"{command : <40}{command_dict[command]}\n"
    return help_string
