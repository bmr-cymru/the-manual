dest_hashes = defaultdict(list)
for path, entry in tree_b.items():
    if entry.is_file and entry.content_hash:
        dest_hashes[entry.content_hash].append((path, entry))
