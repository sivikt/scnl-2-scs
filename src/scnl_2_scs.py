#coding=utf-8

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

import sys 
import codecs
from pyparsing import ParseException
from optparse import OptionParser
from grammar import SCnLGrammar

def translate(argv=None):
    if argv is None:
        argv = sys.argv
        
    # Description of the arguments and options of the program
    usage = 'usage: %prog options arg1 arg2'
    parser = OptionParser(usage=usage, version='%prog 0.1.0')
    
    parser.add_option('-i', '--src_file', help='File to translate.')
    parser.add_option('-s', '--src_str', help='String to translate.')
    parser.add_option('-o', '--out_file', help='File to save the results. If not specified then the results are displayed in the console.')
    
    # Parse program arguments
    (options, argv[1:]) = parser.parse_args()
    
    scnl_grammar = SCnLGrammar()
    scnl_grammar.debug_lvl = 0
    
    source = None
    if options.src_file != None:
        try:
            source = codecs.open(options.src_file, 'r', encoding='utf-8')
        except Exception, err:
            print "Input file '%s' open error" % options.src_file
            print err
            return 2
    
    try:
        generated_code = ''
        if source != None:
            generated_code = scnl_grammar.generate_from_file(source)
            source.close
        else:
            generated_code = scnl_grammar.generate_from_string(test.tests[sys.argv[1]])
    except ParseException, err:
        print err.line
        print u' ' * (err.column - 1) + u'^'
        print unicode(err).encode('utf-8')
        return 2
    except Exception, err:
        print u'An error occured:'
        print unicode(err).encode('utf-8')
        raise
    else:
        if len(scnl_grammar.errors) > 0:
            print 'There are %d errors:' % len(scnl_grammar.errors)
            for (i, err) in enumerate(scnl_grammar.errors):
                print u'%d. ' % (i + 1), unicode(err).encode('utf-8'), '\n'
        else:
            print 'Translation successful'
      
            if options.out_file:
                try:
                    out = codecs.open(options.out_file, 'w', encoding='cp1251')
                except Exception:
                    print "Output file '%s' open error" % options.out
                    return 2
                else:
                    out.write(generated_code)
                    out.close
            else:
                print generated_code

    return 0

if __name__ == "__main__":
    try:
        import psyco
        print 'on psyco'
        psyco.full()
    except ImportError:
        pass
        
    translate()
