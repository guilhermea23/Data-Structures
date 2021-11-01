def height(node):
        if node is None:
            return 0
        else:
            lheight = height(node.esq)
            rheight = height(node.dir)
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1
