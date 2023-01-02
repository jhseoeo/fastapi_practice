# list
def process_items_list(items: list[str]):
    for item in items:
        print(item)


# tuple
def process_items_tuple(items: tuple[int, int, str]):
    for item in items:
        print(item)


# set
def process_items_set(items: set[int]):
    for item in items:
        print(item)


# dict
def process_items_dict(items: dict[str, float]):
    for item in items:
        print(item)


# union
def process_item_union(item: int | str):
    print(item)


# optional
# the field of parameter 'item' can be empty
def process_item_optional(item: str | None = None):
    if item is not None:
        print(item)
