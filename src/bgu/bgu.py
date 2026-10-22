def split_dataframe(df, size: int=1_000_000): 
    """
    Split `DataFrame` to parts, of `size` rows.

    Parameters
    ----------
    df : DataFrame
        The primary matrix or iterable structure containing source records.
    size : int, default=1_000_000
        Number of rows per part.

    Returns
    -------
    list
        `list` of partial `DataFrame`s
    """
    import math
    result = list()
    n_parts = math.ceil(len(df) / size)
    for i in range(n_parts):
        result.append(df[i*size:(i+1)*size])
    return result
