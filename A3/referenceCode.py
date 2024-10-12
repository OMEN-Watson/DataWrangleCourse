import blocking
def phonetic_blocking_first_last(rec_dict, first_name_index, last_name_index):
    """
    Perform phonetic blocking using first name and last name.

    Parameters:
    - rec_dict: Dictionary of records with record IDs as keys.
    - first_name_index: Index of the first name attribute.
    - last_name_index: Index of the last name attribute.

    Returns:
    - A dictionary where keys are combined phonetic codes and values are lists of record IDs.
    """
    blocks = {}

    for rec_id, rec_values in rec_dict.items():
        first_name = rec_values[first_name_index].strip().lower()
        last_name = rec_values[last_name_index].strip().lower()

        # Generate phonetic codes
        first_name_code = blocking.phoneticBlocking(first_name)
        last_name_code = blocking.phoneticBlocking(last_name)

        # Combine phonetic codes to create the blocking key
        blocking_key = first_name_code + last_name_code

        # Add record to the block
        blocks.setdefault(blocking_key, []).append(rec_id)

    return blocks

# Example usage:
# Assuming first name index is 1 and last name index is 3
# blockA_pass1 = phonetic_blocking_first_last(recA_dict, first_name_index=1, last_name_index=3)
# blockB_pass1 = phonetic_blocking_first_last(recB_dict, first_name_index=1, last_name_index=3)

def get_candidate_pairs_from_blocks(blockA_dict, blockB_dict):
    """
    Generate candidate record pairs from the given blocks.

    Parameters:
    - blockA_dict: Blocks from dataset A.
    - blockB_dict: Blocks from dataset B.

    Returns:
    - A set of candidate record ID pairs (rec_idA, rec_idB).
    """
    candidate_pairs = set()

    for blocking_key in blockA_dict:
        if blocking_key in blockB_dict:
            rec_ids_A = blockA_dict[blocking_key]
            rec_ids_B = blockB_dict[blocking_key]

            # Generate all possible pairs between records in the matching blocks
            for rec_idA in rec_ids_A:
                for rec_idB in rec_ids_B:
                    candidate_pairs.add((rec_idA, rec_idB))

    return candidate_pairs

# Get candidate pairs from both passes
# candidate_pairs_pass1 = get_candidate_pairs_from_blocks(blockA_pass1, blockB_pass1)
# candidate_pairs_pass2 = get_candidate_pairs_from_blocks(blockA_pass2, blockB_pass2)

