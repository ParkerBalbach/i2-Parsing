#!/usr/bin/env python
""" generated source for module Node """

#  (C) 2013 Jim Buffenbarger
#  All rights reserved.

class Node(object):
    """ generated source for class Node """
    pos = 0

    def __str__(self):
        """ generated source for method toString """
        result = ""
        result += str(self.__class__.__name__)
        result += " ( "
        fields = self.__dict__
        for field in fields:
            result += "  "
            result += str(field)
            result += str(": ")
            result += str(fields[field])
        result += str(" ) ")
        return result

class NodeAssn(Node):
    """ generated source for class NodeAssn """

    def __init__(self, id, num):
        """ generated source for method __init__ """
        super(NodeAssn, self).__init__()
        self.id = id
        self.num = num

class NodeStmt(NodeAssn):

    def __init__(self, assn):
        super(NodeStmt).__init__()
        self.assn = assn


class NodeBlock(NodeStmt):

    def __init__(self, stmt, block):
        super(NodeBlock).__init__()
        self.stmt = stmt
        self.block = block


        
       



