## Python Interpreter for Apache Zeppelin

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

### Use of matplotlib
<pre>
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [20, 21, 20.5, 20.81, 21.0, 21.48, 22.0, 21.89]

plt.plot(x, y, linestyle='dashed', marker='o', color='red')
zeppelin_show(plt)
</pre>
