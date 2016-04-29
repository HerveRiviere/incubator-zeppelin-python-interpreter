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

import signal
def intHandler(signum, frame):
 print ("Paragraph interrupted")
 raise KeyboardInterrupt()

# Set the signal handler
signal.signal(signal.SIGINT, intHandler)


try:
 from StringIO import StringIO
except ImportError:
 from io import StringIO

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
 print ("%html <div style='"+style+"'>" + img.buf+"<div>")



def help():
 print ('%html')
 print ('<h2>Python Interpreter help</h2>')
  print ('<h3>Forms</h3>')
 print ('<h4>Input forms</h4>')
 print ('<pre> print "&#36{input_form(name)=defaultValue}"</pre>')
 print ('<h4>Checkbox forms</h4>')
 print ('<pre> print "&#36{checkbox:checkbox_form=op1,op1|op2|op3}"</pre>')
 print ('<h3>Matplotlib graph</h3>')
 print ('''<pre>import matplotlib.pyplot as plt
plt.figure()
(.. ..)
zeppelin_show(plt)
plt.close()
</pre>''')
 print ('<div>NB : zeppelin_show function can take optional parameters to adapt graph width and height</div>')
 print ("<div><b>example </b>:<br/> zeppelin_show(plt,width='50px')<br/> zeppelin_show(plt,height='150px') </div>")


