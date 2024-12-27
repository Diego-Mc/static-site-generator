def markdown_to_blocks(markdown):
    return list(filter(lambda y: len(y) > 0, map(lambda x: x.strip("\n "), markdown.split("\n\n"))))