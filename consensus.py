from collections import defaultdict
from enum import Enum

categories = [
    ["2021", "albums", "3", "", "ff"],
    ["2021", "Swift albums", "3", "Republic Records albums", "gg" ],
    ["2020", "albums", "3", "Republic Records albums"],
]

sentence = [
    ["2021 albums 3 ff"],
    ["2021 3albums 4 ff" ],
    ["2020 albums 3 bb ff"],
]

class VALID_STRATEGIES(Enum):
    IN_ONE_OR_MORE = "in_one_or_more"
    CROSSES_THRESHOLD = "crosses_threshold"
    IN_LAST_N_DAYS = "in_last_n_days"
    UNANIMOUS = "unanimous"

def consensus_list(items: list, strategy: VALID_STRATEGIES, threshold=0.5) -> set:
    """
    Given a list of lists, returns the consensus of the lists.

    This function accepts the following strategies:

    - IN_ONE_OR_MORE: An item must be in one or more entries.
    - CROSSES_THRESHOLD: An item must be in more than a certain percentage of entries.
    - IN_LAST_N_DAYS: An item must be in the last n entries.
    - UNANIMOUS: An item must be in all entries.
    """
    unique_items = set()
    membership_counts_in_total = defaultdict(int)
    
    return_array = list()

    for array_items in items:
        new_list = list()
        for i in array_items:
            try:
                new_list.append(i)
            except IndexError:
                print("")
           
        for i in new_list:
            
            membership_counts_in_total[i] = membership_counts_in_total[i] + 1

        return_array = list()

        if strategy == VALID_STRATEGIES.CROSSES_THRESHOLD:
            new_list2 = list(
                [
                    i
                    for i in membership_counts_in_total
                    if membership_counts_in_total[i] / len(items) * 100 > threshold
                ]
            )
            return_array.append(new_list2)
    return return_array[0]        

    raise ValueError(
        "strategy is not in VALID_STRATEGIES. Choose from: "
        + ", ".join(VALID_STRATEGIES.__annotations__.values())
    )

def consensus_sentence(items: list, threshold=0.5) -> set:
    """
    Given a list of lists, returns the consensus of the lists.

    This function accepts the following strategies:

    - IN_ONE_OR_MORE: An item must be in one or more entries.
    - CROSSES_THRESHOLD: An item must be in more than a certain percentage of entries.
    - IN_LAST_N_DAYS: An item must be in the last n entries.
    - UNANIMOUS: An item must be in all entries.
    """
    unique_items = set()
    membership_counts_in_total = defaultdict(int)
    
    return_array = list()

    for array_items in items:
        new_list = list()
        for i in array_items[0].split():
            try:
                new_list.append(i)
            except IndexError:
                print("")
           
        for i in new_list:
            
            membership_counts_in_total[i] = membership_counts_in_total[i] + 1

        return_array = list()

        # if strategy == VALID_STRATEGIES.CROSSES_THRESHOLD:
        new_list2 = list(
            [
                i
                for i in membership_counts_in_total
                if membership_counts_in_total[i] / len(items) * 100 > threshold
            ]
        )
        return_array.append(new_list2)
    return return_array[0]        

    raise ValueError(
        "strategy is not in VALID_STRATEGIES. Choose from: "
        + ", ".join(VALID_STRATEGIES.__annotations__.values())
    )    

def order_alphabetically(categories):
    return sorted(categories)

# print(
#     consensus_list(categories, VALID_STRATEGIES.CROSSES_THRESHOLD, threshold=66)
# )  

# print(
#     consensus_sentence(sentence, threshold=66)
# )  
