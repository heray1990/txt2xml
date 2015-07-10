#!/usr/bin/python2.7
#
# txt2xml.py
#
# Author: Sam Lin
# Created: July 8, 2015

import sys
import os
import re
import codecs
import shutil
from xml.dom.minidom import Document

XML_FILE_NAME = "strings.xml"
XML_FILE_DIR_PREFIX = "values-"

class unicodetxt_to_android_stringxml_obj:
    def __init__(self):
        self.txtfd = 0
        self.xmlfd = 0
        self.langls = []
        self.stringdict = {}

    def parse_txt_file(self, txt_fname):
        cwd = os.path.dirname(sys.argv[0])
        self.txt_fd = codecs.open(os.path.join(cwd,txt_fname),'r','utf-16')

        ls = [line.strip().encode('utf-8') for line in self.txt_fd]
        self.txt_fd.close()

        self.langls = ls[0].split('\t')
        
        lskey = []
        lsval = []
        for i in ls[1:]:
            subls = i.split('\t')
            lskey.append(subls[0])
            lsval.append(subls[1:])

        self.stringdict = dict(zip(lskey,lsval))

    def build_xml_file(self):
        cwd = os.path.dirname(sys.argv[0])
        lsdir = os.listdir('.')

        # Remove directories whose name are start with "values-".
        for i in lsdir:
            if i.startswith(XML_FILE_DIR_PREFIX):
                shutil.rmtree(i)

        for j in self.langls:
            # Create the directories according to the language.
            os.mkdir(XML_FILE_DIR_PREFIX + j)

            doc = Document()
            resources = doc.createElement("resources")
            doc.appendChild(resources)

            for k,v in self.stringdict.items():
                stringele = doc.createElement("string")
                stringele.setAttribute("name",k)
                text = doc.createTextNode(v[self.langls.index(j)])
                stringele.appendChild(text)
                resources.appendChild(stringele)

            # The hacky solution see:
            # http://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
            uglyXml = doc.toprettyxml(indent='  ')
            text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
            prettyXml = text_re.sub('>\g<1></', uglyXml)

            f = open(os.path.join(XML_FILE_DIR_PREFIX + j,XML_FILE_NAME),'w')
            #doc.writexml(f)
            f.write(prettyXml)
            f.close()

obj = unicodetxt_to_android_stringxml_obj()
obj.parse_txt_file(sys.argv[1])
obj.build_xml_file()
