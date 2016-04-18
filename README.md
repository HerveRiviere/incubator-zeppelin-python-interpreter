#A Zeppelin python interpreter 

##Warning : 
This repository is a fork of the [official Apache Zeppelin repository](https://github.com/apache/incubator-zeppelin) with some additionnal commits to add the python interpreter.

To know more about Zeppelin :  [http://zeppelin.incubator.apache.org](http://zeppelin.incubator.apache.org)


##Features of this python interpreter : 
### Easy installation : the interpreter just need the computer python path 
[![pythonpath](/docs/interpreter/screenshots/pyInterpreter3.png)](/docs/interpreter/screenshots/pyInterpreter3.png)
No dependency with spark or others framework.
Python and zeppelin must be installed on the same computer
Python code is executed on Zeppelin server only.
All installed python library (with pip, easy_install...) will be available in the interpreter

###%python, example
[![pythonexec](/docs/interpreter/screenshots/pyInterpreter1.png)](/docs/interpreter/screenshots/pyInterpreter1.png)

###Matplotlib integration
Adding of the function zeppelin_show to display matplot lib graph in Zeppelin
[![pythonexec](/docs/interpreter/screenshots/pyInterpreter2.png)](/docs/interpreter/screenshots/pyInterpreter2.png)

##Installation 

DO NOT USE THIS REPOSITORY TO BUILD / INSTALL ZEPPELIN.
If you need a fresh install of zeppelin go to the [official Apache Zeppelin repository](https://github.com/apache/incubator-zeppelin) 

### Add the interpreter in a zeppelin built with original sources
<pre>
$ cd incubator-zeppelin
$  wget https://github.com/hriviere/incubator-zeppelin-python-interpreter/raw/master/python/dist/python-interpreter.tar.gz && tar -xzvf python-interpreter.tar.gz && mv python interpreter && rm python-interpreter.tar.gz
</pre>

If the file conf/zeppelin-site.xml doesn't exist, create it with conf/zeppelin-site.xml.template

In conf/zeppelin-site.xml, add the interpreter in the zeppelin.interpreters property : 
<pre>
&ltproperty>
  &ltname>zeppelin.interpreters&lt/name>
  &ltvalue>.....,org.apache.zeppelin.python.PythonInterpreter,.....&lt/value>
  &ltdescription>Comma separated interpreter configurations. First interpreter become a default&lt/description>
&lt/property>
</pre>

Restart zeppelin, python interpreter must be present in the webapp interpreters page



**License:** [Apache 2.0](https://github.com/apache/incubator-zeppelin/blob/master/LICENSE)




