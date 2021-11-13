class NodeVisitor():
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def visitStartNode(self, node):
        for paper in node.papers:
            self.interpreter.new_frame()
            paper.accept(self)
            self.interpreter.pop_frame()

    def visitPaperNode(self, node):
        for experiment in node.experiments:
            self.interpreter.new_frame()
            experiment.accept(self)
            self.interpreter.pop_frame()
            
    def visitExperimentNode(self, node):
        for statement in node.statements:
            statement.accept(self) 
            
    def visitFunctionCallNode(self, node):
        fn_name = node.name.value
        arg_values = [node.accept(self) for node in node.args]
        return self.interpreter.runStandardFn(fn_name, arg_values)

    def visitArgNode(self, node):
        if node.type == "ID":
            var_id = node.value
            value = self.interpreter.get_variable(var_id)
            return value
        return node.value

    def visitDefinitionNode(self, node):
        var_id = node.variable
        var_value = node.value.value
        self.interpreter.define_variable(var_id, var_value)
       
    def visitValueNode(self, node):
       pass 
