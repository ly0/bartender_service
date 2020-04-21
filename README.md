BarTender Service
======

Simple BarTender service web api using bottle.py, **Attention: Windows+Python3 ONLY**

I wrote this simple server for integrating auto label printing to my ERP system. I strongly recommand using Anaconda 3.

PRs are welcome, so as the issues :)


### Usage

First, you need to install all dependencies.

```
pip install pythonnet
pip install bottle
```

#### Get Printers

```
curl http://127.0.0.1:8080/printers
```
Return:

```
{"error": 0, "data": {"printers": ["Deli DL-888B(NEW)", "Fax", "Microsoft Print to PDF", "Microsoft XPS Document Writer", "OneNote", "PDFCreator"]}}
```

#### Print label

```
curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8080/print -d '{"template": "1", "count": 2, "data": [{"key": "title", "value": "Test 测试"}]}'
```
