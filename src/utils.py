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
Created on 23.04.2011
Last modified 24.04.2011

@author: Sergei Sintsov
"""

from pyparsing import (lineno, col, line)

class Enumerate(dict):
    """Enumerate a whitespace separated sequence
    """
    def __init__(self, names):
        for number, name in enumerate(names.split()):
            setattr(self, name, number)
            self[number] = name

class ExceptionInfo(object):
    """Class for exception handling data
    """
    def __init__(self):
        # position in currently parsed text
        self.location = 0
        # currently parsed text
        self.text = ''

    def setpos(self, location, text):
        """Sets curently parsed text and position
        """
        self.location = location
        self.text = text

class SemanticException(Exception):
    """Exception for semantic errors found during parsing, similar to ParseException.
       Introduced because ParseException is used internally in pyparsing and custom
       messages got lost and replaced by pyparsing's generic errors.
    """
    def __init__(self, message, ex_info, print_location=True):
        """message - message to print
            ex_info - an object of ExceptionInfo
        """
        super(SemanticException, self).__init__()
        
        self._message = message
        self.location = ex_info.location
        self.print_location = print_location
        
        if ex_info.location != None:
            self.line = lineno(ex_info.location, ex_info.text)
            self.col = col(ex_info.location, ex_info.text)
            self.text = line(ex_info.location, ex_info.text)
        else:
            self.line = self.col = self.text = None
            
    def _get_message(self):
        """Returns user message
        """
        return self._message
        
    def _set_message(self, message):
        """Sets user message
        """
        self._message = message
    
    message = property(_get_message, _set_message)
    
    def __str__(self):
        msg = u'Error'
        
        if self.print_location and (self.line != None):
            msg += u' at line %d, col %d' % (self.line, self.col)
            
        msg += u': %s' % self.message
        
        if self.print_location and (self.line != None):
            msg += u'\n%s' % self.text
        
        return msg
        
# Supported types of sc entities
symbol_type = Enumerate('NONE VAR CONCEPT CONTOUR ATTR_CONCEPT NODE')

class SymbolTableEntry(object):
    """Class which represents one symbol table entry.
    """
    def __init__(self, sname='', stype=symbol_type.NONE):
        """sname - symbol name
           stype - symbol type
        """
        self.name = sname
        self.type = stype

class SymbolTable(object):
    """Class for symbol table
    """
    def __init__(self):
        self.table = []
        self.lable_len = 0

    def error(self, text=''):
        """Symbol table error exception. It should happen only if index is out of range while accessing symbol table.
           This exeption is not handled by the compiler, so as to allow traceback printing
        """
        if text == u'':
            raise Exception(u'Symbol table index out of range')
        else:
            raise Exception(u'Symbol table error: %s' % text)

    def to_string(self):
        """Displays the symbols table content
        """
        if len(self.table) == 0: return ''
        
        # Finding the maximum length for each column
        sym_name = u'Symbol name'
        sym_len = max(max(len(i.name) for i in self.table), len(sym_name))
        type_name = u'Type'
        type_len = max(max(len(symbol_type[i.type]) for i in self.table), len(type_name))
        
        # table header
        table_content_str = u'{0:3s} | {1:^{2}s} | {3:^{4}s}\n'.format(u' No', sym_name, sym_len, type_name, type_len)
        table_content_str += '-----------------------------' + '-' * (sym_len + type_len) + '\n'
        
        # table content
        for i, sym in enumerate(self.table):
            table_content_str += u'{0:3d} | {1:^{2}s} | {3:^{4}s}\n'.format(i, sym.name, sym_len, symbol_type[sym.type], type_len)
        
        return table_content_str

    def insert_symbol(self, sname, stype):
        """Inserts new symbol at the end of the symbol table.
           Returns symbol index
           sname - symbol name
           stype - symbol type
        """
        self.table.append(SymbolTableEntry(sname, stype))
        self.table_len = len(self.table)
        return self.table_len - 1
        
    def lookup_symbol(self, sname, stype=symbol_type.keys()):
        """Searches for symbol, from the end to the begining.
           Returns symbol index or None
           sname - symbol name
           stype - symbol type (or None) default: any type
        """
        stype = stype if isinstance(stype, list) else [stype]
        for i, sym in [[x, self.table[x]] for x in range(0, len(self.table))]:
            if (sym.name == sname) and (sym.type in stype):
                return i
        
        return None

    def insert_var(self, sname):
        """Inserts a new variable ID
        """
        return self.insert_symbol(sname, symbol_type.VAR)

    def insert_concept(self, sname):
        """Inserts a new concept ID
        """
        return self.insert_symbol(sname, symbol_type.CONCEPT)
    
    def insert_atrribute(self, sname):
        """Inserts a new attribute ID
        """
        return self.insert_symbol(sname, symbol_type.ATTR_CONCEPT)
        
    def insert_contour(self, sname):
        """Inserts a new contour ID
        """
        return self.insert_symbol(sname, symbol_type.CONTOUR)
    
    def insert_node(self, sname):
        """Inserts a new common node ID
        """
        return self.insert_symbol(sname, symbol_type.NODE)
            
    def get_entry_safe(self, index):
        """Returns SymbolTableEntry entity by its index number
        """
        try:
            return self.table[index]
        except Exception:
            self.error()
    
    def get_entry(self, index):
        """Returns SymbolTableEntry entity by its index number or
            None if there is no entity with the given index
        """
        try:
            return self.table[index]
        except Exception:
            return None
