# -*- coding: utf-8 -*-
import os
import shutil
from datetime import datetime

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>文件和目录 os os.path shutil>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

sys = os.name
print("操作系统 is", sys)
# >>>操作系统 is nt

env = os.environ
print(env)
# >>>environ({'ADB': 'D:\\Android\\Sdk\\platform-tools', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'ANDROID': 'D:\\Android\\android-sdk-windows\\tools;D:\\Android\\android-sdk-windows\\platform-tools;', 'ANDROID_NDK_HOME': 'D:\\Android\\android-ndk-r10d', 'APPDATA': 'C:\\Users\\moreface2019\\AppData\\Roaming', 'CATALINA_BASE': 'D:\\Java\\Tomcat 7.0', 'CATALINA_HOME': 'D:\\Java\\Tomcat 7.0', 'CLASSPATH': '.;D:\\Java\\jdk1.8.0_181\\lib\\dt.jar;D:\\Java\\jdk1.8.0_181\\lib\\tools.jar;', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-1BAQGR2', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\moreface2019', 'IDEA_INITIAL_DIRECTORY': 'C:\\WINDOWS\\System32', 'JAVA_HOME': 'D:\\Java\\jdk1.8.0_181', 'LOCALAPPDATA': 'C:\\Users\\moreface2019\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-1BAQGR2', 'M3_HOME': 'D:\\apache-maven-3.6.3', 'MAVEN_HOME': 'D:\\apache-maven-3.6.3', 'NDK_HOME': 'D:\\Android\\android-ndk-r10d', 'NLS_LANG': 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\moreface2019\\OneDrive', 'ORACLE_HOME': 'D:\\Oracle\\Instant Client', 'OS': 'Windows_NT', 'PATH': 'D:\\Python\\venv\\Scripts;D:\\Java\\jdk1.8.0_181\\bin;D:\\Java\\jdk1.8.0_181\\jre\\bin;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;d:\\Program Files\\Git\\cmd;D:\\Android\\Sdk\\platform-tools;C:\\Program Files\\OpenVPN\\bin;C:\\Program Files\\TortoiseSVN\\bin;D:\\Android\\android-sdk-windows\\tools;D:\\Android\\android-sdk-windows\\platform-tools;;D:\\Oracle\\Instant Client\\bin;D:\\Android\\android-ndk-r10d;D:\\Android\\android-ndk-r10d;C:\\Users\\moreface2019\\AppData\\Local\\atom\\bin;D:\\apache-maven-3.6.3\\bin ;D:\\Java\\Tomcat 7.0\\bin;D:\\Java\\Tomcat 7.0\\lib;C:\\Program Files\\MySQL\\MySQL Shell 8.0\\bin\\;C:\\Users\\moreface2019\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\;C:\\Users\\moreface2019\\AppData\\Local\\Programs\\Python\\Python38\\;C:\\Users\\moreface2019\\AppData\\Local\\Microsoft\\WindowsApps;D:\\JetBrains\\PyCharm Community Edition 2020.1\\bin;;D:\\apache-maven-3.6.3\\bin;;C:\\Users\\moreface2019\\AppData\\Local\\Microsoft\\WindowsApps', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 142 Stepping 9, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '8e09', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(venv) $P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM COMMUNITY EDITION': 'D:\\JetBrains\\PyCharm Community Edition 2020.1\\bin;', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Users\\moreface2019\\Desktop\\MyProjects\\MyPythonProject', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\MOREFA~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\MOREFA~1\\AppData\\Local\\Temp', 'TNS_ADMIN': 'D:\\Oracle\\Instant Client\\network\\admin', 'TOMCAT_HOME': 'D:\\Java\\Tomcat 7.0', 'USERDOMAIN': 'DESKTOP-1BAQGR2', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-1BAQGR2', 'USERNAME': 'moreface2019', 'USERPROFILE': 'C:\\Users\\moreface2019', 'VIRTUAL_ENV': 'D:\\Python\\venv', 'WINDIR': 'C:\\WINDOWS', '_OLD_VIRTUAL_PATH': 'D:\\Java\\jdk1.8.0_181\\bin;D:\\Java\\jdk1.8.0_181\\jre\\bin;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;d:\\Program Files\\Git\\cmd;D:\\Android\\Sdk\\platform-tools;C:\\Program Files\\OpenVPN\\bin;C:\\Program Files\\TortoiseSVN\\bin;D:\\Android\\android-sdk-windows\\tools;D:\\Android\\android-sdk-windows\\platform-tools;;D:\\Oracle\\Instant Client\\bin;D:\\Android\\android-ndk-r10d;D:\\Android\\android-ndk-r10d;C:\\Users\\moreface2019\\AppData\\Local\\atom\\bin;D:\\apache-maven-3.6.3\\bin ;D:\\Java\\Tomcat 7.0\\bin;D:\\Java\\Tomcat 7.0\\lib;C:\\Program Files\\MySQL\\MySQL Shell 8.0\\bin\\;C:\\Users\\moreface2019\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\;C:\\Users\\moreface2019\\AppData\\Local\\Programs\\Python\\Python38\\;C:\\Users\\moreface2019\\AppData\\Local\\Microsoft\\WindowsApps;D:\\JetBrains\\PyCharm Community Edition 2020.1\\bin;;D:\\apache-maven-3.6.3\\bin;;C:\\Users\\moreface2019\\AppData\\Local\\Microsoft\\WindowsApps', '_OLD_VIRTUAL_PROMPT': '$P$G'})
print('JAVA_HOME is', env.get('JAVA_HOME'))
# >>>D:\Java\jdk1.8.0_181

pwd = os.path.abspath('.')
print('pwd is', pwd)
# >>>pwd is C:\Users\moreface2019\Desktop\MyProjects\MyPythonProject\inout
print()

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
# >>>       708  2021-01-06 15:22  0001_file.py
# >>>        ... ...
# >>>        17  2021-01-06 15:23  test.txt
print()

print("# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数")
print(os.path.join('dir', 'file'))
# >>>dir\file
print("# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数")
print(os.path.split("dir\\file"))
# >>>('dir', 'file')
print("# os.path.splitext()可以直接让你得到文件扩展名")
print(os.path.splitext(os.path.join('dir', 'file.txt')))
# >>>('dir\\file', '.txt')

# 列出当前目录下的所有目录
parent = os.path.abspath(os.path.join(os.getcwd(), ".."))  # 父目录
print(parent)
# >>>C:\Users\moreface2019\Desktop\MyProjects\MyPythonProject

list = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(list)
# >>>['0001_file.py', '0002_stringio.py', '0003_bytesio.py', '0004_filedir.py', '__init__.py']

f = open('test.txt', 'w')
f.write('test')
f.close()
print("# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充")
shutil.copyfile('test.txt', 'test1.txt')
os.rename('test.txt', 'test.py')  # 对文件重命名
os.remove('test.py')  # 删掉文件
os.remove('test1.txt')  # 删掉文件
