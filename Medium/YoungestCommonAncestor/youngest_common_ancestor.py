class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(D) time | O(1) space
def getYoungestCommonAncestor(top_ancestor, descendant_one, descendant_two):
    desc_one_depth = depth(descendant_one, top_ancestor)
    desc_two_depth = depth(descendant_two, top_ancestor)

    if desc_one_depth > desc_two_depth:
        return backtrack_ancestral_tree(descendant_one, descendant_two, desc_one_depth - desc_two_depth)
    else:
        return backtrack_ancestral_tree(descendant_two, descendant_one, desc_two_depth - desc_one_depth)


def depth(decendant, top_ancestor):
    depth = 0

    while decendant != top_ancestor:
        depth += 1
        decendant = decendant.ancestor

    return depth


def backtrack_ancestral_tree(lower_desc, higher_desc, diff):
    # Level the lower descendant node
    while diff > 0:
        lower_desc = lower_desc.ancestor
        diff -= 1

    while lower_desc != higher_desc:
        lower_desc = lower_desc.ancestor
        higher_desc = higher_desc.ancestor

    return higher_desc
