import sys
sys.displayhook = lambda x: None
"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import StringIO

def zeppelin_show(p,width=0,height=0):
 img = StringIO.StringIO()
 p.savefig(img, format='svg')
 img.seek(0)
 style=""
 if(width>0):
  style+='width:'+width
 if(height>0):
  if(len(style)>0):
   style+=","
  style+='height:'+height
 print "%html <div style='"+style+"'>" + img.buf+"<div>"



def printHelp():
 print '\r==========================='
 print '\rPYTHON Interpreter help'
 print '\r===========================\n'
 print '\rWARNING : Cancel paragraph exexution will stop the whole interpreter !\n'
 print '''\rDISPLAY MATPLOTLIB GRAPH :
import matplotlib.pyplot as plt
plt.figure()
(.. ..)
zeppelin_show(plt)
plt.close()
'''
 print '\rNB : zeppelin_show function can take optional parameters to adapt graph width and height'
 print "\rexample : zeppelin_show(plt,width='50px')/ zeppelin_show(plt,height='150px') \r"


printHelp()