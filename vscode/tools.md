# AWESOME tools & tips

## use peek for screen recorder to gif

```bash
sudo add-apt-repository ppa:peek-developers/stable
sudo apt update
sudo apt install -y peek
```

## install snyk for security

```bash
sudo apt install -y npm
npm install -g snyk
cd ~/projects/myproj/


machine:~/project$ snyk test
Please run `pip install -r requirements.txt`

machine:~/project$ sudo pip2 install -r requirements.txt
The directory '~/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '~/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting python-tds (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/5a/8a/d2f56210011f76616ff1673f3a4d77b80f4092de0c7e6207e66ad7fe124d/python-tds-1.9.1.tar.gz (74kB)
    100% |████████████████████████████████| 81kB 325kB/s
Collecting python-logstash (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/4e/8d/7ff2e8e8e2613e7bb7654790480bb4cf51a55721371adbb631b16cb16dce/python-logstash-0.4.6.tar.gz
Collecting logstash_formatter (from -r requirements.txt (line 3))
  Downloading https://files.pythonhosted.org/packages/7f/69/73c5b373ac656de0ee61175597d6739bd69bddcbc80894940cdb4237af8a/logstash_formatter-0.5.17.tar.gz
Collecting python-dateutil (from -r requirements.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/0c/57/19f3a65bcf6d5be570ee8c35a5398496e10a0ddcbc95393b2d17f86aaaf8/python_dateutil-2.7.2-py2.py3-none-any.whl (212kB)
    100% |████████████████████████████████| 215kB 347kB/s
Collecting pytest==3.3.2 (from -r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/38/af/8dcf688d192914928393f931b7b550f2530299bbb08018b2f17efa6aab73/pytest-3.3.2-py2.py3-none-any.whl (185kB)
    100% |████████████████████████████████| 194kB 662kB/s
Collecting coverage==4.4.2 (from -r requirements.txt (line 6))
  Downloading https://files.pythonhosted.org/packages/a9/59/042a3b5ba4e9a88aaf77c86bd5f8a76a9e10f705a2cf3e72e9d02c9f66ad/coverage-4.4.2-cp27-cp27mu-manylinux1_x86_64.whl (194kB)
    100% |████████████████████████████████| 204kB 405kB/s
Requirement already satisfied (use --upgrade to upgrade): requests in /usr/lib/python2.7/dist-packages (from -r requirements.txt (line 7))
Collecting pytest-cov (from -r requirements.txt (line 8))
  Downloading https://files.pythonhosted.org/packages/30/7d/7f6a78ae44a1248ee28cc777586c18b28a1df903470e5d34a6e25712b8aa/pytest_cov-2.5.1-py2.py3-none-any.whl
Collecting pysnow (from -r requirements.txt (line 9))
  Downloading https://files.pythonhosted.org/packages/34/e2/28f4a7f6f4096e7b6e6d46a15e15b05bcf2dd78333fe297766b25da55ee1/pysnow-0.7.3.tar.gz
Requirement already satisfied (use --upgrade to upgrade): six>=1.4.1 in /usr/lib/python2.7/dist-packages (from python-tds->-r requirements.txt (line 1))
Collecting py>=1.5.0 (from pytest==3.3.2->-r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/67/a5/f77982214dd4c8fd104b066f249adea2c49e25e8703d284382eb5e9ab35a/py-1.5.3-py2.py3-none-any.whl (84kB)
    100% |████████████████████████████████| 92kB 542kB/s
Requirement already satisfied (use --upgrade to upgrade): setuptools in /usr/lib/python2.7/dist-packages (from pytest==3.3.2->-r requirements.txt (line 5))
Collecting funcsigs; python_version < "3.0" (from pytest==3.3.2->-r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/69/cb/f5be453359271714c01b9bd06126eaf2e368f1fddfff30818754b5ac2328/funcsigs-1.0.2-py2.py3-none-any.whl
Collecting pluggy<0.7,>=0.5 (from pytest==3.3.2->-r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/11/bf/cbeb8cdfaffa9f2ea154a30ae31a9d04a1209312e2919138b4171a1f8199/pluggy-0.6.0.tar.gz
Collecting attrs>=17.2.0 (from pytest==3.3.2->-r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/b5/60/4e178c1e790fd60f1229a9b3cb2f8bc2f4cc6ff2c8838054c142c70b5adc/attrs-17.4.0-py2.py3-none-any.whl
Collecting oauthlib (from pysnow->-r requirements.txt (line 9))
  Downloading https://files.pythonhosted.org/packages/e0/ac/c6a0c98788aa0d61915190d089e9ebe680905a94261effe3936eb8fe356f/oauthlib-2.0.7-py2.py3-none-any.whl (124kB)
    100% |████████████████████████████████| 133kB 327kB/s
Collecting requests_oauthlib (from pysnow->-r requirements.txt (line 9))
  Downloading https://files.pythonhosted.org/packages/77/34/d0957563f20b259a31c12f14e858d79f2e66eb539d3c1b9ab7077ef030ca/requests_oauthlib-0.8.0-py2.py3-none-any.whl
Collecting httpretty (from pysnow->-r requirements.txt (line 9))
  Downloading https://files.pythonhosted.org/packages/ee/0b/2514804a7a3b8fc79bc20ff5e7ef780b54b020c91220badb2b58abff83e4/httpretty-0.8.14-py2-none-any.whl
Collecting ijson (from pysnow->-r requirements.txt (line 9))
  Downloading https://files.pythonhosted.org/packages/7f/e9/8508c5f4987ba238a2b169e582c1f70a47272b22a2f1fb06b9318201bb9e/ijson-2.3-py2.py3-none-any.whl
Installing collected packages: python-tds, python-logstash, logstash-formatter, python-dateutil, py, funcsigs, pluggy, attrs, pytest, coverage, pytest-cov, oauthlib, requests-oauthlib,httpretty, ijson, pysnow
  Running setup.py install for python-tds ... done
  Running setup.py install for python-logstash ... done
  Running setup.py install for logstash-formatter ... done
  Running setup.py install for pluggy ... done
  Running setup.py install for pysnow ... done
Successfully installed attrs-17.4.0 coverage-4.4.2 funcsigs-1.0.2 httpretty-0.8.14 ijson-2.3 logstash-formatter-0.5.17 oauthlib-2.0.7 pluggy-0.6.0 py-1.5.3 pysnow-0.7.3 pytest-3.3.2 pytest-cov-2.5.1 python-dateutil-2.7.2 python-logstash-0.4.6 python-tds-1.9.1 requests-oauthlib-0.8.0
You are using pip version 8.1.1, however version 9.0.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
machine:~/project$ snyk test

Testing ~/project...
✗ High severity vulnerability found on requests@2.9.1
- desc: HTTP Request Redirection
- info: https://snyk.io/vuln/SNYK-PYTHON-REQUESTS-40470
- from: scripts@0.0.0 > pysnow@0.7.3 > requests-oauthlib@0.8.0 > requests@2.9.1


✗ High severity vulnerability found on requests@2.9.1
- desc: HTTP Request Redirection
- info: https://snyk.io/vuln/SNYK-PYTHON-REQUESTS-40470
- from: scripts@0.0.0 > pysnow@0.7.3 > requests@2.9.1


✗ High severity vulnerability found on requests@2.9.1
- desc: HTTP Request Redirection
- info: https://snyk.io/vuln/SNYK-PYTHON-REQUESTS-40470
- from: scripts@0.0.0 > requests@2.9.1


Organisation: sharkguto
Package manager: pip
Target file: requirements.txt
Open source: no

Tested 19 dependencies for known vulnerabilities, found 1 vulnerability, 3 vulnerable paths.

machine:~/project$
```

## install vscode

```bash
sudo apt-get update -y
sudo apt-get install -y curl git
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get update -y
sudo apt-get install -y code
```

## install python dependences

```bass
sudo apt install -y python3 python3-dev python3-pip
sudo apt install -y freetds-dev freetds-bin freetds-common
sudo apt install -y openjdk-8-jdk openjdk-8-jre
sudo pip3 install yapf autopep8 pylint flake8
sudo pip3 install pytest pytest-cov requests python-dateutil
sudo pip3 install python-tds pymssql ujson
```

## vscode config example

```json
{
    "python.autoComplete.addBrackets": true,
    "python.pythonPath": "python3",
    "sonarlint.ls.javaHome": "/usr/lib/jvm/java-8-openjdk-amd64/",
    "sonarlint.ls.vmargs": "-Xmx1024m",
    "pydocs.style": "google",
    "git.autofetch": true,
    "templateGenerator.fields.author": "Gustavo M Freitas",
    "templateGenerator.fields.email": "gustavo@gmf-tech.com",
    "templateGenerator.fields.link": "https://github.com/sharkguto",
    "git.enableSmartCommit": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": true,
    "window.zoomLevel": 0,
    "python.unitTest.promptToConfigure": false,
    "python.unitTest.pyTestEnabled": false,
    "editor.codeLens": true,
    "workbench.editor.labelFormat": "default",
    "workbench.iconTheme": "vscode-icons",
    "tidyMarkdown.disableFormatter": false,
    "python.formatting.autopep8Path": "autopep8",
    "python.formatting.provider": "autopep8",
    "python.linting.pep8Enabled": true,
    "explorer.confirmDelete": false
}
```

## plugins

- bash beautify (ahmed hamdy)
- excel viewer(grapecity)
- git history(don jayamanne)
- markdownlint/markdown all in one (david anson/yu zhang)
- python (from microsoft)
- sonarlint (sonarsource)

```bash
code --install-extension shakram02.bash-beautify
code --install-extension GrapeCity.gc-excelviewer
code --install-extension donjayamanne.githistory
code --install-extension yzhang.markdown-all-in-one
code --install-extension DavidAnson.vscode-markdownlint
code --install-extension ms-python.python
code --install-extension SonarSource.sonarlint-vscode
code --install-extension robertohuertasm.vscode-icons
code --install-extension azaugg.vscode-python-docstring
code --install-extension DotJoshJohnson.xml
code --install-extension codezombiech.gitignore
code --install-extension eamodio.gitlens
code --install-extension DengSir.template-generator-vscode
```

## install sonar by command line, it will install jars dependences automatically

![peek + sonar](../images/sonar.gif)

## vscode key bind example for generate def docs ... google style

keybindings.json

```json
[
    {
        "key": "ctrl+1",
        "command": "extension.addPyDocstring"
    }
]
```

![peek + sonar](../images/using_template.gif)

## template generator

To create file with template
type: alt+control+n
write field: the name of file or folder
option: choose python.py or anything else

```bash
machine:~/github/how-to$ cat ~/.vscode/templates/\{__name__.python\}.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# {__name__}.py
# @Author : {__author__} ({__email__})
# @Link   : {__link__}
# @Date   : {__date__}
machine:~/github/how-to$
```

![peek + template generator](../images/using_template.gif)