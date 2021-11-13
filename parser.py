from dataclasses import dataclass
from tokenizer import *
from parsernodes import *


class Parser:
    def parse(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
        self.lookahead = tokenizer.get_next_token()
        return self.Start() 
    
    def consume(self, token_type: int):
        if self.lookahead.type != token_type:
            raise Exception(f"Expected token of type {token_type}, got {self.lookahead.type}")
        old_lookahead = self.lookahead
        self.lookahead = self.tokenizer.get_next_token()
        return old_lookahead
    

    def Start(self):
        return StartNode(self.ListOfPapers())

    def ListOfPapers(self):
        papers = [self.Paper()]
        while not self.lookahead.type == EOF and self.lookahead.type == PAPER_KW:
            papers.append(self.Paper())
        return papers;
    
    def Paper(self):
        self.consume(PAPER_KW)
        title = self.String()
        self.consume(LEFT_CB)
        exps = self.ListOfExperiments()
        self.consume(RIGHT_CB)
        return PaperNode(title, exps)

    def ListOfExperiments(self):
        experiments = [self.Experiment()]
        while not self.lookahead.type == EOF and self.lookahead.type == EXPERIMENT_KW:
           experiments.append(self.Experiment())
        return experiments

    def Experiment(self):
        self.consume(EXPERIMENT_KW)
        title = self.String()
        self.consume(LEFT_CB)
        if self.lookahead.type != RIGHT_CB:
            statements = self.ListOfStatements()
        self.consume(RIGHT_CB)
        return ExperimentNode(title, statements)
    
    def ListOfDefinitions(self):
        definitions = [self.Definition()]
        while not self.lookahead.type == EOF and self.lookahead.type == LET_KW:
            definitions.append(self.Definition())
        return definitions

    def ListOfStatements(self):
        statements = [self.Statement()]
        while not self.lookahead.type == EOF and self.lookahead.type != RIGHT_CB:
            statements.append(self.Statement())
        return statements

    def Statement(self):
        if self.lookahead.type == LET_KW:
            return self.Definition()
        if self.lookahead.type == ID:
            return self.FunctionCall()
        raise Exception("Couldn't process statement.")

    def Definition(self):
        self.consume(LET_KW)
        varName = self.consume(ID)
        self.consume(EQUALS)
        value = self.Value()
        return DefinitionNode(varName.value, value)

    def FunctionCall(self):
        name = self.consume(ID)
        self.consume(LEFT_PAR)
        if self.lookahead.type == RIGHT_PAR:
            self.consume(RIGHT_PAR)
            return FunctionCallNode(name, [])
        args = self.CommaSeparatedArgs()
        self.consume(RIGHT_PAR)
        return FunctionCallNode(name, args) 

    def CommaSeparatedArgs(self):
        args = [self.Arg()]
        while not self.lookahead.type == EOF and self.lookahead.type == COMMA:
            self.consume(COMMA)
            args.append(self.Arg())
        return args 

    def Arg(self):
        if self.lookahead.type == ID:
            return ArgNode("ID", self.consume(ID).value)
        if self.lookahead.type == STRING:
            return ArgNode("STRING", self.String().value)
        return ArgNode("NUMBER", self.Number().value)

    def Value(self):
        if self.lookahead.type == STRING:
            return self.String()
        return self.Number()

    def String(self):
        token = self.consume(STRING)
        return ValueNode("STRING", token.value.replace("\"", ""))

    def Number(self):
        token = self.consume(NUMBER)
        return ValueNode("NUMBER", token.value)
