#!/usr/bin/env python3

import cgitb
import cgi
import webbrowser


cgitb.enable()

form = cgi.FieldStorage()

pnome = form.getvalue('pnome')

op = '0'
webbrowser.open('music.mp3')

print("Content-type:text/html\r\n\r\n")
print("""<html>
            <head>
                <meta charset=\"UTF-8\">
                <title>Título</title>
            </head>
            <body>""")

print("<h1>MUSIC PLAYER</h1><hr>")

print("<table border=1>")
print("""
        <tr>
         <th>Nome da musica</th>
        </tr>""")
print("""<tr>
        <td>{}</td>
        </tr>""".format("Spactrem - Shine"))
print("</table>")
print("""<a href="../index.html">Voltar para o inicio</a><br>""")

# print(form.keys())
# print(form.value)

print("</body></html>")
