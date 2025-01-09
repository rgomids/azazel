from consts import AZAZEL_STONE


def get_history():
    lists = []
    with open(AZAZEL_STONE.HISTORY_PATH, "r") as file:
        for line in file:
            line_list = line.strip().split()
            lists.append(line_list)

    return lists


def set_on_history(author: str, data: str):
    with open(AZAZEL_STONE.HISTORY_PATH, "a") as file:
        data = f"{author}: {data}"
        file.write("".join(data) + "\n")


def clean_historic():
    with open(AZAZEL_STONE.HISTORY_PATH, "w") as file:
        pass
