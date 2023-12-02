API решения задачи Хакатона Phystech GigaChat Challenge (https://gigachat-challenge.tech/)
<hr>

#### Формулировка задачи:
Придумать и реализовать бизнес-продукт на основании возможностей, которые предоставляют **GigaChat** и его SDK GigaChain, а также нейросеть **Kandinsky**.


<hr>
- python 3.12

## Quick Start Guide

### Clone git repo
```
git clone git@github.com:RakhimBek/gigachat-challenge.git
```

### Copy environment variables file

 + Go to: https://developers.sber.ru/studio/workspaces
 + Click: "Generate new client secret"
 + Choose: "Authorization" field
 + Add to **.env** as ``GIGACHAT_CREDENTIAL`` property

e.g.
```
GIGACHAT_CREDENTIAL=O0GGGzzzZ123YzU0Mi0zZ123Y110MitN456MzdjYMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMONNNNNNNNNNNNNNNNNNNNMA==
```

###  Add environment variable
```
$ source .env
$ export $(cut -d= -f1 .env)
```

### Update pip, setuptools
```
$ pip install -U pip setuptools
```

### Install requirements:
```
$ pip install -r requirements.txt
```

### Run server
```
$ python main.py
```

### API
Automatic interactive API documentation
```
/docs
```