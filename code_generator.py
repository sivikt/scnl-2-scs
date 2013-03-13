# -*- coding: utf-8 -*-

"""
-----------------------------------------------------------------------------
This source file is part of OSTIS (Open Semantic Technology for Intelligent Systems)
For the latest info, see http://www.ostis.net

Copyright (c) 2011 OSTIS

OSTIS is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OSTIS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OSTIS.  If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------------------
"""
"""
Created on 7.03.2011
Last modified 24.04.2011

@author: Sergei Sintsov
"""

from utils import *
import grammar

# current SCs element ID value
current_id = 0

def gen_unique_id():
    """Generates unique ID
    """
    global current_id
    
    current_id += 1
    return str(current_id)

class SCnLCodeGen(object):
    """This class contains basic functionality to generate result SCs code
    """
    ERRONEOUS_NODE = u'!|erroneous_node|!'
    
    def __init__(self):
        # defines debug level
        # 0 - no debug
        # 1 - print different debug messages
        # 2 - print only parsing results, without executing parse actions (grammar-only testing)
        self.__debug_lvl = 0
        
        # grammar to parse
        self._grammar = None
        # symbol table
        self.__symtable = SymbolTable()
        # sintax and semantic errors
        self.__errors = []
        # generated code
        self.__code = ''
    
    def get_errors(self):
        return self.__errors
    
    errors = property(get_errors)
    
    def get_symtable(self):
        """Returns sybols table
        """
        return self.__symtable
    
    symtable = property(get_symtable)
    
    def set_debug_lvl(self, debug_lvl=0):
        """Sets debug level
        """
        self.__debug_lvl = debug_lvl
    
    def get_debug_lvl(self):
        """Gets debug level
        """
        return self.__debug_lvl
        
    debug_lvl = property(get_debug_lvl, set_debug_lvl)
    
    def _append_to_code(self, text):
        """Appends text to the result code
        """
        self.__code += text

    def _append_to_code_newline(self, text, indent=False, shift=4):
        """Appends to the result code text
        """
        self._append_to_code(u'\n')
        if indent:
            self._append_to_code(u' ' * shift)
        self._append_to_code(text)

    def _generate_node(self, node, type, add_to_result_code=True):
        """Adds node to the symbol table and generates text code for it
        """
        new_insert = False
        sindex = self.symtable.lookup_symbol(node, type)
        
        text_code = None
        if sindex == None:
            new_insert = True
            sindex = self.symtable.insert_symbol(node, type)
            text_code = u'{0} = {1};'.format(node, u'{..}' if type == symbol_type.VAR else u'{}')
            
            if add_to_result_code:
                self._append_to_code_newline(text_code)
                
        return [new_insert, sindex, text_code]
        
    def generate_from_file(self, src_file):
        """Generates result code from the source file
            src_file - source file object to parse
        """
        try:
            parse_res = self._grammar.parseFile(src_file)
            if self.debug_lvl > 1: 
                return parse_res

            return self.__code
        except:
            raise
     
    def generate_from_string(self, str):
        """Generates result code from the source string
            str - string to parse
        """
        try:
            parse_res = self._grammar.parseString(str)
            if self.debug_lvl > 1: 
                return parse_res

            return self.__code
        except:
            raise
            
class SCnLCommonCodeGen(SCnLCodeGen):
    """This class contains common methods and actions to generate result code
    """
    def __init__(self):
        super(SCnLCommonCodeGen, self).__init__()
        
        # contains information about current parse status
        self.__exception_info = ExceptionInfo()

        # action flags
        self.__is_var_declaration_section = False
        self.__is_in_atomic_exist_section = False
        
        # code buffers
        self.__contour_concepts_text_code = []
        self.__contour_elements_text_code = []
        
        # helpfull generators
        self.__scnl_operation_codegen = SCnLMathOperationCodeGen(self)
        self.__scnl_relation_codegen = SCnLMathRelationCodeGen(self)
               
    def _text_action(self, str, loc, toks):
        """Code executed after recognising a text
            Tokens sequence: see grammar
        """
        return toks[0]
    
    def _linked_text_body_action(self, str, loc, toks):
        """Code executed after recognising a linked text body
            Tokens sequence: see grammar
        """
        return toks[-1]
        
    def _tex_text_action(self, str, loc, toks):
        """Code executed after recognising a tex text
        """
        return toks[1]
        
    def _vars_declaration_start_action(self, str, loc, toks):
        """Code executed before linked vars list
            Tokens sequence: see grammar
        """
        self.__is_var_declaration_section = True
        
    def _vars_declaration_end_action(self, str, loc, toks):
        """Code executed after linked vars list
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
            
        self.__is_var_declaration_section = False
        
        for var_node in toks[0]:
            new_insert = self._generate_node(var_node, symbol_type.VAR)[0]

            if not new_insert:
                self.__exception_info.setpos(loc, str)
                self.errors.append(SemanticException(u'Duplicate variable declaration', self.__exception_info))
        
        contour_node = u'$linked_vars_' + gen_unique_id()
        text_code = u'{0} = [{1};];\n'.format(contour_node, u'; '.join(toks[0]))
        self._append_to_code_newline(text_code)
        
        return self.symtable.insert_contour(contour_node)
    
    def _var_action(self, str, loc, toks):
        """Code executed after recognising a var
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
            
        var_node = toks[1]
        if not var_node.startswith(u'_'):
            var_node = u'_' + var_node
        
        var_node = u'"' + var_node + u'"'
        
        if self.__is_var_declaration_section:
            return var_node
        
        sindex = self.symtable.lookup_symbol(var_node, symbol_type.VAR)
        if sindex == None:
            self.__exception_info.setpos(loc, str)
            self.errors.append(SemanticException(u'Unknown variable ' + var_node, self.__exception_info))
            return -1
        
        return sindex
 
    def _concept_action(self, text, loc, toks):
        """Code executed after recognising a concept
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
        
        concept_node = u'"' + toks[1] + u'"'
        sindex = self.symtable.lookup_symbol(concept_node, symbol_type.CONCEPT)
        if sindex == None:
            sindex = self.symtable.insert_concept(concept_node)
            self.__contour_concepts_text_code.append(concept_node + u' = {};')
                
        return sindex
    
    def _attribute_action(self, text, loc, toks):
        """Code executed after recognising a attribute
            Tokens sequence: see grammar
        """
        return toks[1]
        
    def _atomic_exist_begin_action(self, text, loc, toks):
        """Code executed before recognising an atomic axistential expression
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
            
        self._generate_node(u'"атомарное существование"', symbol_type.CONCEPT)
        
    def _atomic_exist_end_action(self, text, loc, toks):
        """Code executed after recognising an atomic axistential expression
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
        
        for text_code in self.__contour_concepts_text_code: 
           self._append_to_code_newline(text_code)
        self.__contour_concepts_text_code = []
        
        atomic_exist_node = u'$contour_' + gen_unique_id()
        text_code = u'{0} = ['.format(atomic_exist_node)
        self._append_to_code_newline(text_code)
        
        for text_code in self.__contour_elements_text_code: 
            self._append_to_code_newline(text_code, True)
        self.__contour_elements_text_code = []
        
        self._append_to_code_newline(u'];\n')
        
        return self.symtable.insert_contour(atomic_exist_node)
     
    def _math_set_end_action(self, text, loc, toks):
        """Code executed after recognising a not oriented set
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
        
        elements = []
        for i in toks[1]:
            entry = self.symtable.get_entry(i)
            elements.append(entry.name if entry != None else self.ERRONEOUS_NODE)
        
        set_node = u'$math_set_' + gen_unique_id()
        text_code = u'{0} = {{. {1} .}};'.format(set_node, u', '.join(elements))
        self.__contour_elements_text_code.append(text_code)
        
        return self.symtable.insert_node(set_node)
    
    def _math_oset_end_action(self, text, loc, toks):
        """Code executed after recognising an oriented set
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
        
        elements = []
        # creates attributes
        for (i, toks_elem) in enumerate(toks[1]): 
            if len(toks_elem) > 1:
                elem_index = toks_elem[1]
                attr_node = self.symtable.get_entry_safe(toks_elem[0]).name
            else:
                elem_index = toks_elem[0]
                attr_node = u'"' + str(i + 1) + u'_"'
                gen_result = self._generate_node(attr_node, symbol_type.ATTR_CONCEPT, False)
                
                if gen_result[0]:
                    self.__contour_concepts_text_code.append(gen_result[2])

            elem_entry = self.symtable.get_entry(elem_index)
            elem_node = elem_entry.name if elem_entry != None else self.ERRONEOUS_NODE
            text_code = u'{0}::{1}'.format(attr_node, elem_node)
            elements.append(text_code)
        
        oset_node = u'$math_oset_' + gen_unique_id()
        text_code = u'{0} = {{. {1} .}};'.format(oset_node, u', '.join(elements))
        self.__contour_elements_text_code.append(text_code)
        
        return self.symtable.insert_node(oset_node)
    
    def _math_operation_end_action(self, text, loc, toks):
        """Code executed after recognising a math operation
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
            
        help_nodes = self.__scnl_operation_codegen.generate(toks, self.__contour_elements_text_code)
        
        for node in help_nodes:
            gen_result = self._generate_node(node, symbol_type.CONCEPT, False)
            if gen_result[0]:
                self.__contour_concepts_text_code.append(gen_result[2])
        
    def _math_relation_end_action(self, text, loc, toks):
        """Code executed after recognising a math relation
            Tokens sequence: see grammar
        """
        if self.debug_lvl > 1: 
            return
        
        help_nodes = self.__scnl_relation_codegen.generate(toks, self.__contour_elements_text_code)
        
        for node in help_nodes:
            gen_result = self._generate_node(node, symbol_type.CONCEPT, False)
            if gen_result[0]:
                self.__contour_concepts_text_code.append(gen_result[2])

class SCnLMathOperationCodeGen(object):
    """This class genarates result code for math operations
    """
    def __init__(self, scnl_codegen):
        self.root_codegen = scnl_codegen
        
    def generate(self, toks, code_buf):
        """Generates text code for a math operation
            toks - tokens to generate code
            Returns help_concept_nodes_used_to_generate_code
        """
        type = toks[1]
        res_type = toks[3]
        left_op_entry = self.root_codegen.symtable.get_entry_safe(toks[0])
        right_op_entry = self.root_codegen.symtable.get_entry_safe(toks[2])
        result_entry = self.root_codegen.symtable.get_entry_safe(toks[4])
        left_op = left_op_entry.name if left_op_entry != None else SCnLCodeGen.ERRONEOUS_NODE
        right_op = right_op_entry.name if right_op_entry != None else SCnLCodeGen.ERRONEOUS_NODE
        result = result_entry.name if result_entry != None else SCnLCodeGen.ERRONEOUS_NODE
            
        text_code = SCnLCodeGen.ERRONEOUS_NODE
        help_nodes = []

        rel_arc = u'->>' if res_type == grammar.GRAMMAR_CONST['SCnEqual'][1] else u'~>>'
        
        # BIIiiig switch
        if type == grammar.GRAMMAR_CONST['SCnUnion'][1]:
            help_nodes = [u'"объединение*"', u'"1_"', u'"2_"']
            
            union_set = u'$union_set_' + gen_unique_id()
            union_set_text_code = u'{0} = {{. {1}, {2} .}};'.format(union_set, left_op, right_op)
            code_buf.append(union_set_text_code)
            
            text_code = u'"объединение*" {0} {{. "1_"::{1}, "2_"::{2} .}};'.format(rel_arc, union_set, result)
        
        elif type == grammar.GRAMMAR_CONST['SCnIntersection'][1]:
            help_nodes = [u'"пересечение*"', u'"1_"', u'"2_"']
            
            intersect_set = u'$interset_set_' + gen_unique_id()
            intersect_set_text_code = u'{0} = {{. {1}, {2} .}};'.format(intersect_set, left_op, right_op)
            code_buf.append(intersect_set_text_code)
            
            text_code = u'"пересечение*" {0} {{. "1_"::{1}, "2_"::{2} .}};'.format(rel_arc, intersect_set, result)
        
        code_buf.append(text_code)
        
        return help_nodes

class SCnLMathRelationCodeGen(object):
    """This class genarates result code for math relations
    """
    def __init__(self, scnl_codegen):
        self.root_codegen = scnl_codegen
    
    def generate(self, toks, code_buf):
        """Generates text code for a math relation
            toks - tokens to generate code
            Returns help_concept_nodes_used_to_generate_code
        """
        type = toks[1]
        left_op_entry = self.root_codegen.symtable.get_entry_safe(toks[0])
        right_op_entry = self.root_codegen.symtable.get_entry_safe(toks[2])
        left_op = left_op_entry.name if left_op_entry != None else SCnLCodeGen.ERRONEOUS_NODE
        right_op = right_op_entry.name if right_op_entry != None else SCnLCodeGen.ERRONEOUS_NODE
            
        text_code = SCnLCodeGen.ERRONEOUS_NODE
        help_nodes = []

        # BIIiiig switch
        if type == grammar.GRAMMAR_CONST['SCnNotEqual'][1]:
            help_nodes = [u'"равенство*"']
            text_code = u'"равенство*" ~>> {{. {0}, {1} .}};'.format(left_op, right_op)
        
        elif type == grammar.GRAMMAR_CONST['SCnEqual'][1]:
            help_nodes = [u'"равенство*"']
            text_code = u'"равенство*" ->> {{. {0}, {1} .}};'.format(left_op, right_op)
        
        elif type == grammar.GRAMMAR_CONST['SCnSupset'][1]:
            help_nodes = [u'"включение*"', u'"1_"', u'"2_"']
            text_code = u'"включение*" ->> {{. "1_"::{0}, "2_"::{1} .}};'.format(left_op, right_op)
        
        elif type == grammar.GRAMMAR_CONST['SCnSubset'][1]:
            help_nodes = [u'"включение*"', u'"1_"', u'"2_"']
            text_code = u'"включение*" ->> {{. "1_"::{0}, "2_"::{1} .}};'.format(right_op, left_op)
            
        elif type == grammar.GRAMMAR_CONST['SCnProperSupset'][1]:
            help_nodes = [u'"строгое включение*"', u'"1_"', u'"2_"']
            text_code = u'"строгое включение*" ->> {{. "1_"::{0}, "2_"::{1} .}};'.format(left_op, right_op)

        elif type == grammar.GRAMMAR_CONST['SCnProperSubset'][1]:
            help_nodes = [u'"строгое включение*"', u'"1_"', u'"2_"']
            text_code = u'"строгое включение*" ->> {{. "1_"::{0}, "2_"::{1} .}};'.format(right_op, left_op)
            
        elif type == grammar.GRAMMAR_CONST['SCnElement'][1]:
            text_code = u'{0} ->> {1};'.format(right_op, left_op)
        
        elif type == grammar.GRAMMAR_CONST['SCnNotElement'][1]:
            text_code = u'{0} ~>> {1};'.format(right_op, left_op)
        
        code_buf.append(text_code)
        
        return help_nodes
        
class SCnLStatementCodeGen(SCnLCommonCodeGen):
    """This class genarates result code for whole logic statement
    """
    def __init__(self):
        super(SCnLStatementCodeGen, self).__init__()
        
        # helpfull generators
        self.quantifier_codegen = SCnLQuantifierCodeGen(self)
        self.implication_codegen = SCnLImplicationCodeGen(self)
        self.many_places_connective_codegen = SCnLManyPlacesConnectiveCodeGen(self)
    
    def _quantifier_action(self, str, loc, toks):
        """Code executed after recognising a quantifier
        """
        if self.debug_lvl > 1:
            return
        
        return self.quantifier_codegen.generate(str, loc, toks)

    def _many_places_connective_action(self, str, loc, toks):
        """Code executed after recognising a many-places connective
        """
        if self.debug_lvl > 1:
            return
        
        return self.many_places_connective_codegen.generate(str, loc, toks)
        
    def _implication_action(self, str, loc, toks):
        """Code executed after recognising an implication
        """
        if self.debug_lvl > 1:
            return
        
        return self.implication_codegen.generate(str, loc, toks)
    
    def _generate(self, str, loc, toks):
        """Action after logic statement recognized
        """
        if self.debug_lvl > 1:
            return
        
        if self.debug_lvl == 1:
            print self.symtable.to_string()
        
class SCnLQuantifierCodeGen(object):
    """This class genarates result code for logic quantifiers
        Tokens sequence: see grammar
    """
    def __init__(self, root_codegen):
        """root_codegen - an instance of SCnLStatementCodeGen
        """        
        self.root_codegen = root_codegen
        # contains information about current parse status
        self.exception_info = ExceptionInfo()
        
    def generate(self, str, loc, toks):
        """Generates text code for one of two quatifiers (universal or existential)
        """
        quantifier_type = u'"существование*"' if toks[0] == grammar.GRAMMAR_CONST['SCnLExistential'][1] else u'"всеобщность*"'
        self.root_codegen._generate_node(quantifier_type, symbol_type.CONCEPT)
        
        self.root_codegen._generate_node(u'"связываемые переменные_"', symbol_type.ATTR_CONCEPT)
        
        if len(toks[2]) > 1:
            self.exception_info.setpos(loc, str)
            self.root_codegen.errors.append(SemanticException(u'Quantifier must takes only one argument', self.exception_info))
                
        arg = self.root_codegen.symtable.get_entry(toks[2][0]).name
       
        linked_vars_node = self.root_codegen.symtable.get_entry(toks[1]).name
        quantifier_node = u'$quantifier_' + gen_unique_id()
        text_code = u'{0} = {{"связываемые переменные_": {1}, {2}}};\n{3} -> {4};'.format(quantifier_node, linked_vars_node, arg, quantifier_type, quantifier_node)
        self.root_codegen._append_to_code_newline(text_code)
        
        return self.root_codegen.symtable.insert_node(quantifier_node)

class SCnLImplicationCodeGen(object):
    """This class genarates result code for implication
        Tokens sequence: see grammar
    """
    def __init__(self, root_codegen):
        """root_codegen - an instance of SCnLStatementCodeGen
        """
        self.root_codegen = root_codegen
        
    def generate(self, str, loc, toks):
        """Generates text code for implication
        """
        self.root_codegen._generate_node(u'"импликация*"', symbol_type.CONCEPT)
        self.root_codegen._generate_node(u'"если_"', symbol_type.ATTR_CONCEPT)
        self.root_codegen._generate_node(u'"то_"', symbol_type.ATTR_CONCEPT)
        
        if_arg = self.root_codegen.symtable.get_entry(toks[2]).name
        then_arg = self.root_codegen.symtable.get_entry(toks[4]).name
        
        impl_node = u'$implication_' + gen_unique_id()
        text_code = u'{0} = {{"если_": {1}, "то_": {2}}};\n"импликация*" -> {3};'.format(impl_node, if_arg, then_arg, impl_node)
        self.root_codegen._append_to_code_newline(text_code)
        
        return self.root_codegen.symtable.insert_node(impl_node)
            
class SCnLManyPlacesConnectiveCodeGen(object):
    """This class genarates result code for many-places logic connectives such as conjunction, disjunction,
        exclusive disjunction or equivalance.
        Tokens sequence: see grammar
    """
    def __init__(self, root_codegen):
        """root_codegen - an instance of SCnLStatementCodeGen
        """
        self.root_codegen = root_codegen
        # contains information about current parse status
        self.exception_info = ExceptionInfo()
        
    def generate(self, str, loc, toks):
        """Generates text code for one of the many-places logic connectives
        """
        arguments = []
        first_lvl = toks[1]
        for i in range(2, len(toks), 2):
            lvl = toks[i - 1]
            arg = toks[i]
            if lvl >= first_lvl:
                arguments.append(self.root_codegen.symtable.get_entry(arg).name)
            else:
                i += -1
                break
                
        parent_args = [] if i == len(toks) - 1 else toks[i:]
        
        connective_code = toks[0]
        if connective_code == grammar.GRAMMAR_CONST['SCnLConjunction'][1]:
            connective_name = u'"конъюнкция*"'
            if len(arguments) < 2:
                self.exception_info.setpos(loc, str)
                self.root_codegen.errors.append(SemanticException(u'Conjunction must takes two or more arguments', self.exception_info))
                
        elif connective_code == grammar.GRAMMAR_CONST['SCnLDisjunction'][1]:
            connective_name = u'"дизъюнкция*"'
            if len(arguments) < 2:
                self.exception_info.setpos(loc, str)
                self.root_codegen.errors.append(SemanticException(u'Disjunction must takes two or more arguments', self.exception_info))
                
        elif connective_code == grammar.GRAMMAR_CONST['SCnLExclDisjunction'][1]:
            connective_name = u'"альтернатива*"'
            if len(arguments) < 2:
                self.exception_info.setpos(loc, str)
                self.root_codegen.errors.append(SemanticException(u'Exclusive Disjunction takes two or more arguments', self.exception_info))
                
        else:
            connective_name = u'"эквиваленция*"'
            if len(arguments) > 2:
                self.exception_info.setpos(loc, str)
                self.root_codegen.errors.append(SemanticException(u'Equivalance must takes only two arguments', self.exception_info))
            
        self.root_codegen._generate_node(connective_name, symbol_type.CONCEPT)
        connective_node = u'$connective_' + gen_unique_id()
        text_code = u'{0} = {{ {1} }};\n{2} -> {3};'.format(connective_node, u', '.join(arguments), connective_name, connective_node)
        self.root_codegen._append_to_code_newline(text_code)
        
        sindex = self.root_codegen.symtable.insert_node(connective_node)
        return [sindex] + parent_args

