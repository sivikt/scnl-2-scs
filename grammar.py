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

from pyparsing import *
from code_generator import SCnLStatementCodeGen

"""Something like:
    {{SCnLStatement|1|
        {{SCnLUniversal|1}} {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}} {{SCnLThereIs|1}}
            {{SCnLevel|1}} {{SCnLImplication|1}}
                {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLIf|1}}
                    {{SCnLAtomicExist|
                        {{SCnLSet| {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Непрямолинейная тройка точек|непрямолинейная тройка точек]]}}
                    }};
                {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLThen|1}}
                    {{SCnLExistential|1}} {{SCnLVar| {{SCnLTex|\alpha}}}} {{SCnLExistentialPropPref|1}}
                        {{SCnLevel|2}} {{SCnLСonjunction|1}}
                            {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist|
                                {{SCnLVar| {{SCnLTex|\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}};
                                {{SCnLevel|3}} {{SCnLVar|_ti}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\alpha}}}};
                                {{SCnLevel|3}} {{SCnLVar|_tj}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\alpha}}}};
                                {{SCnLevel|3}} {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\alpha}}}}
                            }};
                            {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLUniversal|1}} {{SCnLVar| {{SCnLTex|\beta}}}} {{SCnLThereIs|1}}
                                {{SCnLevel|3}} {{SCnLImplication|1}}
                                    {{SCnLevel|4|{{SCn_перечисление|3}}}} {{SCnLIf|1}}
                                        {{SCnLAtomicExist|
                                            {{SCnLVar| {{SCnLTex|\beta}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}},
                                            {{SCnLVar|_ti}} {{SCn_принадлежность}} {{SCnLVar| {{SCnLTex|\beta}}}},
                                            {{SCnLVar|_tj}} {{SCn_принадлежность}} {{SCnLVar| {{SCnLTex|\beta}}}},
                                            {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar| {{SCnLTex|\beta}}}}
                                        }};
                                    {{SCnLevel|4|{{SCn_перечисление|3}}}} {{SCnLThen|1}}
                                        {{SCnLAtomicExist|
                                            {{SCnLSet| {{SCnLVar| {{SCnLTex|\alpha}}}}, {{SCnLVar| {{SCnLTex|\beta}}}} }} {{SCn_принадлежность}} {{SCnLConcept|совпадение*}}
                                        }}
    .|cont }}
"""

code_counter = 0
def gen_code():
    """Generates unique code ID
    """
    global code_counter
    
    code_counter += 1
    return code_counter

# Literals
GRAMMAR_CONST = dict(
    SCnLVar = [u'SCnLVar', gen_code()],
    SCnLTex = [u'SCnLTex', gen_code()],
    SCnLConcept = [u'SCnLConcept', gen_code()],
    SCnLAttr = [u'SCnLAttr', gen_code()],
    SCnEnumerate = [u'SCn_перечисление', gen_code()],
    SCnLevel = [u'SCnLevel', gen_code()],
    SCnNotEqual = [u'SCn_не_равно', gen_code()],
    SCnSupset = [u'SCn_надмножество', gen_code()],
    SCnProperSupset = [u'SCn_строгое_надмножество', gen_code()],
    SCnNotElement = [u'SCn_непринадлежность', gen_code()],
    SCnSubset = [u'SCn_подмножество', gen_code()],
    SCnElement = [u'SCn_принадлежность', gen_code()],
    SCnEqual = [u'SCn_равно', gen_code()],
    SCnProperSubset = [u'SCn_строгое_подмножество', gen_code()],
    SCnUnion = [u'SCn_объединение', gen_code()],
    SCnIntersection = [u'SCn_пересечение', gen_code()],
    SCnLSet = [u'SCnLSet', gen_code()],
    SCnLOSet = [u'SCnLOSet', gen_code()],
    SCnLAtomicExist = [u'SCnLAtomicExist', gen_code()],
    SCnLUniversal = [u'SCnLUniversal', gen_code()],
    SCnLExistential = [u'SCnLExistential', gen_code()],
    SCnLExistentialPropPref = [u'SCnLExistentialPropPref', gen_code()],
    SCnLThereIs = [u'SCnLThereIs', gen_code()],
    SCnLConjunction = [u'SCnLConjunction', gen_code()],
    SCnLDisjunction = [u'SCnLDisjunction', gen_code()],
    SCnLExclDisjunction = [u'SCnLExclDisjunction', gen_code()],
    SCnLEquivalence = [u'SCnLEquivalence', gen_code()],
    SCnLImplication = [u'SCnLImplication', gen_code()],
    SCnLIf = [u'SCnLIf', gen_code()],
    SCnLThen = [u'SCnLThen', gen_code()],
    SCnLStatement = [u'SCnLStatement', gen_code()]
)

people = [ {'name': "Tom", 'age': 10}, {'name': "Mark", 'age': 5} ]
name_indexer = dict((p['name'], i) for i, p in enumerate(people))
name_indexer.get('Tom', -1)

ParserElement.enablePackrat()

class SCnLGrammar(SCnLStatementCodeGen):
    
    def __init__(self):
        super(SCnLGrammar, self).__init__()
        self._grammar = self.__make_grammar()
             
    def __make_grammar(self):
        """ BEGIN GRAMMAR
        """
        wrapped_in_template = lambda expr: Suppress(u'{') + Suppress(u'{') + expr + Suppress(u'}') + Suppress(u'}')
        comma_list = lambda expr: delimitedList(expr, delim=u',')
        
        template_type = Suppress(u'|') + Regex(r'\d+')
        suprs_template_type = template_type.suppress()
        
        # Alphabet definition.
        cyrillic_alphas = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        special_chars = u'_:.,-*()<>;?!`/+=@\\^~'
        all_chars = cyrillic_alphas + alphanums + special_chars
        
        word = Word(all_chars)
        
        text = Combine(OneOrMore(word), u' ', adjacent=False)
        text.setParseAction(self._text_action)
        
        tex_text = GRAMMAR_CONST['SCnLTex'][0] + Suppress(u'|') + text
        tex_text = wrapped_in_template(tex_text)
        tex_text.setParseAction(self._tex_text_action)

        # Wiki link template definition: [[text_link | link description]]
        linked_text_body = Optional(text + Suppress(u'|')) + text
        linked_text_body.setParseAction(self._linked_text_body_action)
        linked_text= Suppress(u'[') + Suppress(u'[') + linked_text_body + Suppress(u']') + Suppress(u']')
        
        # Variable definition
        var = GRAMMAR_CONST['SCnLVar'][0] + Suppress(u'|') + (text ^ linked_text ^ tex_text)
        var = wrapped_in_template(var)
        var.setParseAction(self._var_action)
        
        # Concept definition
        concept = GRAMMAR_CONST['SCnLConcept'][0] + Suppress(u'|') + (text ^ linked_text)
        concept = wrapped_in_template(concept)
        concept.setParseAction(self._concept_action)
        
        # Oriented set element's attribute definition
        attribute = GRAMMAR_CONST['SCnLAttr'][0] + Suppress(u'|') + (var ^ concept)
        attribute = wrapped_in_template(attribute)
        attribute.setParseAction(self._attribute_action)
        
        # All symbols that can appear between tokens
        stopSymbols = Optional(text).suppress()
        
        # Level marker
        # tokens: (0)lvl_code (1)lvl_number
        lvl_enum = Suppress(u'|') + wrapped_in_template(GRAMMAR_CONST['SCnEnumerate'][0] + template_type).suppress()
        lvl = wrapped_in_template(GRAMMAR_CONST['SCnLevel'][0] + template_type + Optional(lvl_enum))
        opt_lvl = Optional(lvl).suppress()
        lvl.setParseAction(lambda t: int(t[1]))
        
        """ Elements for theory of discrete mathematics
        """
        relation_operators = {}
        relation_operators[ GRAMMAR_CONST['SCnNotEqual'][0] ] = GRAMMAR_CONST['SCnNotEqual'][1] 
        relation_operators[ GRAMMAR_CONST['SCnSupset'][0] ] = GRAMMAR_CONST['SCnSupset'][1]
        relation_operators[ GRAMMAR_CONST['SCnProperSupset'][0] ] = GRAMMAR_CONST['SCnProperSupset'][1]
        relation_operators[ GRAMMAR_CONST['SCnNotElement'][0] ] = GRAMMAR_CONST['SCnNotElement'][1]
        relation_operators[ GRAMMAR_CONST['SCnSubset'][0] ] = GRAMMAR_CONST['SCnSubset'][1]
        relation_operators[ GRAMMAR_CONST['SCnElement'][0] ] = GRAMMAR_CONST['SCnElement'][1]
        relation_operators[ GRAMMAR_CONST['SCnEqual'][0] ] = GRAMMAR_CONST['SCnEqual'][1]
        relation_operators[ GRAMMAR_CONST['SCnProperSubset'][0] ] = GRAMMAR_CONST['SCnProperSubset'][1]
       
        operation_operators = {}
        operation_operators[ GRAMMAR_CONST['SCnUnion'][0] ] = GRAMMAR_CONST['SCnUnion'][1]
        operation_operators[ GRAMMAR_CONST['SCnIntersection'][0] ] = GRAMMAR_CONST['SCnIntersection'][1]
        
        operation_result_operators = {}
        operation_result_operators[ GRAMMAR_CONST['SCnEqual'][0] ] = GRAMMAR_CONST['SCnEqual'][1]
        operation_result_operators[ GRAMMAR_CONST['SCnNotEqual'][0] ] = GRAMMAR_CONST['SCnNotEqual'][1]
        
        # Nonoriented set definition
        math_set = Forward()
        
        # Oriented set definition
        math_orient_set = Forward()
        
        # Math operand definition
        math_operand = var ^ concept ^ math_set ^ math_orient_set
        math_operand.ignore(lvl)
        
        # tokens: (0)set_code (1)[args]
        math_set_body = GRAMMAR_CONST['SCnLSet'][0] + Suppress(u'|') + Group(comma_list(math_operand))
        math_set << wrapped_in_template(math_set_body)
        math_set.setParseAction(self._math_set_end_action)
        
        # tokens: (0)oset_code (1)[args]
        math_orient_set_elem = Group(Optional(attribute) + math_operand)
        math_orient_set_body = GRAMMAR_CONST['SCnLOSet'][0] + Suppress(u'|') + Group(comma_list(math_orient_set_elem))
        math_orient_set << wrapped_in_template(math_orient_set_body)
        math_orient_set.setParseAction(self._math_oset_end_action)
        
        # Definition of the operation of the discrete mathematics
        operation_op = oneOf(operation_operators.keys()).setParseAction(lambda t: operation_operators[t[0]])
        operation_result_op = oneOf(operation_result_operators.keys()).setParseAction(lambda t: operation_result_operators[t[0]])
        
        math_operation_left = math_operand + wrapped_in_template(operation_op) + math_operand
        math_operation_right = wrapped_in_template(operation_result_op) + math_operand + stopSymbols
        math_operation = math_operation_left + math_operation_right
        math_operation.setParseAction(self._math_operation_end_action)
        
        # Definition of the relation of the discrete mathematics
        relation_op = oneOf(relation_operators.keys()).setParseAction(lambda t: relation_operators[t[0]])
        
        math_relation = math_operand + wrapped_in_template(relation_op) + math_operand + stopSymbols
        math_relation.setParseAction(self._math_relation_end_action)
        
        """Atomic existential definition
        """
        # tokens: (0)atomic_code (1)[var_toks]
        atomic_exist_prefix = GRAMMAR_CONST['SCnLAtomicExist'][0] + Suppress(u'|') + Empty().setParseAction(self._atomic_exist_begin_action)
        atomic_exist_args = OneOrMore(math_operation ^ math_relation)
        atomic_exist = wrapped_in_template(atomic_exist_prefix + atomic_exist_args) + stopSymbols
        atomic_exist.setParseAction(self._atomic_exist_end_action)
        
        """Logic quantifiers definition
        """
        quantifier = Forward()
        
        # Universal definition
        universal_prefix = wrapped_in_template(GRAMMAR_CONST['SCnLUniversal'][0] + suprs_template_type).setParseAction(lambda t: GRAMMAR_CONST['SCnLUniversal'][1]) + \
                            Empty().setParseAction(self._vars_declaration_start_action) + Group(comma_list(var)).setParseAction(self._vars_declaration_end_action)
        
        # Existential definition
        exist_prop_prefix = wrapped_in_template(GRAMMAR_CONST['SCnLExistentialPropPref'][0] + template_type).suppress()
        exist_prefix = wrapped_in_template(GRAMMAR_CONST['SCnLExistential'][0] + suprs_template_type).setParseAction(lambda t: GRAMMAR_CONST['SCnLExistential'][1]) + \
                        Empty().setParseAction(self._vars_declaration_start_action) + \
                        Group(comma_list(var)).setParseAction(self._vars_declaration_end_action) + exist_prop_prefix
        
        """Logic connectives definition
        """
        there_is = Optional(wrapped_in_template(GRAMMAR_CONST['SCnLThereIs'][0] + template_type)).suppress()
        
        connective = Forward()
                
        # Conjunction definition
        conj_prefix = wrapped_in_template(GRAMMAR_CONST['SCnLConjunction'][0] + suprs_template_type).setParseAction(lambda t: GRAMMAR_CONST['SCnLConjunction'][1])
        
        # Disjunction definition
        disj_prefix = wrapped_in_template(GRAMMAR_CONST['SCnLDisjunction'][0] + suprs_template_type).setParseAction(lambda t: GRAMMAR_CONST['SCnLDisjunction'][1])
        
        # Exclusive disjunction definition
        excl_disj_prefix = wrapped_in_template(GRAMMAR_CONST['SCnLExclDisjunction'][0] + suprs_template_type).setParseAction(lambda t: GRAMMAR_CONST['SCnLExclDisjunction'][1])
        
        # Equivalence definition
        equiv_prefix = wrapped_in_template(GRAMMAR_CONST['SCnLEquivalence'][0] + suprs_template_type).setParseAction(lambda t: GRAMMAR_CONST['SCnLEquivalence'][1])
        
        # Implication definition
        # tokens: (0)impl_code   (1)if_code (2)if_arg_node_id   (3)then_code (4)then_arg_node_id
        impl_arg = atomic_exist ^ quantifier ^ connective
        impl_if_prefix = Suppress(lvl) + wrapped_in_template(GRAMMAR_CONST['SCnLIf'][0] + suprs_template_type) + there_is + opt_lvl
        impl_then_prefix = Suppress(lvl) + wrapped_in_template(GRAMMAR_CONST['SCnLThen'][0] + suprs_template_type) + there_is + opt_lvl
        impl = wrapped_in_template(GRAMMAR_CONST['SCnLImplication'][0] + suprs_template_type) + impl_if_prefix + impl_arg + impl_then_prefix + impl_arg
        impl.setParseAction(self._implication_action)
        
        """General logic statement elements
        """
        # Simple Logic Colpula definition
        # tokens: (0)connective_code (1)lvl_code (2)arg_node_id] (3)lvl_code (4)arg_node_id ...
        many_places_connective = Forward()
        
        many_places_connective_prefix = conj_prefix ^ disj_prefix ^ excl_disj_prefix ^ equiv_prefix
        many_places_connective_arg = lvl + (atomic_exist ^ quantifier ^ connective)
        many_places_connective << many_places_connective_prefix + OneOrMore(many_places_connective_arg)
        many_places_connective.setParseAction(self._many_places_connective_action)
        
        connective << (impl ^ many_places_connective)
        
        # Logic Quantifier definition
        # tokens: (0)quant_code (1)[var_toks] (2)arg_node_id
        quantifier << (universal_prefix ^ exist_prefix) + there_is + opt_lvl + Group((atomic_exist ^ connective))
        quantifier.setParseAction(self._quantifier_action)
        
        # Logic stetement definition
        logic_stmt = GRAMMAR_CONST['SCnLStatement'][0] + template_type + u'|' + quantifier + u'|' + u'cont'
        logic_stmt = wrapped_in_template(logic_stmt)
        logic_stmt.setParseAction(self._generate)
        
        return logic_stmt
        
    def validate_grammar(self):
        try:
            self._grammar.validate()
        except:
            raise
            
