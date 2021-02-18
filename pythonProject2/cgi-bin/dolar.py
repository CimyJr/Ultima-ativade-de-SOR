#!/usr/bin/env python3

import cgitb
import cgi
import requests
import json

requisicao = requests.get("https://economia.awesomeapi.com.br/json/all")
cotacao = json.loads(requisicao.text)

cgitb.enable()

form = cgi.FieldStorage()

pnome = form.getvalue('pnome')

print("Content-type:text/html\r\n\r\n")
print("""<html>
            <head>
                <meta charset=\"UTF-8\">
                <title>Título</title>
            </head>
            <body>""")

print("<h1>Conversor de Moeda</h1><hr>")

print("<table border=1>")
print("""
        <tr>
         <th>Quantidade em real</th>
        </tr>""")
print("""<tr>
        <td>{}</td>
        </tr>""".format(float(pnome) * float(cotacao['USD']['ask'])))
print("</table>")
print("""<a href="../index.html">Voltar para o inicio</a><br>""")

# print(form.keys())
# print(form.value)

print("</body></html>")