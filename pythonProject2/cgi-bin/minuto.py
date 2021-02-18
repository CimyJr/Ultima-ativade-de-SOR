#!/usr/bin/env python3

import cgitb
import cgi


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

print("<h1>Conversor de Tempo</h1><hr>")

print("<table border=1>")
print("""
        <tr>
         <th>Quantidade em minutos</th>
        </tr>""")
print("""<tr>
        <td>{}</td>
        </tr>""".format(int(pnome) * 60))
print("</table>")
print("""<a href="../index.html">Voltar para o inicio</a><br>""")

# print(form.keys())
# print(form.value)

print("</body></html>")