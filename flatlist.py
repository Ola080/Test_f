def flatten_ragged_list(ragged_list: list[list[int]]) -> list[int]:

    flatlist = []
    for item in ragged_list:
        ilength = len(item)
        for i in range(ilength):
            flatlist.append(item[i])

    return flatlist

def access_element(ragged_list: list[list[int]], i: int, j: int) -> int | None:
    if ragged_list is None:
        return (3, None)
    elif i < 0 or i >= len(ragged_list):
        return (1, None)
    elif j < 0 or j >= len(ragged_list[i]):
        return (2, None)
    else:
        return (0, ragged_list[i][j])


data = [[1, 2], [3], [4, 5, 6]]

print(access_element(data, 2, 1))