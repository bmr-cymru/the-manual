def _best_sibling_proximity(
    orig_path: str, candidates: List[Tuple[str, FsEntry]]
) -> Tuple[str, FsEntry]:
    """
    Sibbling proximity heuristic: choose the "best" move
    destination when multiple candidates exist.

    :param orig_path: The original path before the move.
    :type orig_path: ``str``
    :param candidates: Possible candidates for the destination,
                       as a list of (path, entry) pairs.
    :type candidates: ``List[Tuple[str, FsEntry]]``
    :returns: The winning (path, entry) pair.
    :rtype: ``Tuple[str, FsEntry]``
    """

    def filename_distance(path_a: str, path_b: str) -> float:
        """
        Quick and cheap edit distance approximation.

        :param path_a: The first path to compare.
        :type path_a: ``str``
        :param path_b: The second path to compare.
        :type path_b: ``str``
        :returns: A value 0..1 indicating the approximate
                  similarity of the paths.
        :rtype: ``float``
        """
        if not path_a or not path_b:
            return 0.0

        # Quick wins first
        if path_a.startswith(path_b) or path_b.startswith(path_a):
            return 1.0
        if path_a.endswith(path_b) or path_b.endswith(path_a):
            return 1.0

        # Token overlap for compound names
        tokens_a = set(re.split(r"[ -_.,:@]", path_a))
        tokens_b = set(re.split(r"[ -_.,:@]", path_b))
        overlap = len(tokens_a & tokens_b) / len(tokens_a | tokens_b)
        return overlap

    if len(candidates) > 1:
        candidates.sort(
            key=lambda x: filename_distance(orig_path, x[0]), 
            reverse=True,
        )

    return candidates[0]

