## importamos flask
from flask import Flask
app= Flask (__name__)

## definimos la ruta principal
@app. route("/")
def Holaflask():
    return"<h1> ¡Hola flask! </h1> <hr>"

##Ahora tomanos la segunda ruta y la reemplazamos por el siguiente ejemplo
##1.) Haga un progarama que calcule el promedio de notas que tienen un valor de
## 30%, 30% y 40% respectivamente.
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resltado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1> el resultado es: {resultado}</h1> <hr>"

if __name__=="__main__":
    ## el valor de true indica que la app se deja en modo debug
    app.run(debug=True)
    
    ##ahora tomamos la tercera ruta y la reemplazamos por el siguinte ejemplo
    ## 2.) un programa que al capturar la edad diga sis es :
    ## Menos de edad (Menor a 18 años )
    ## Adulto (Mayor o igual a 18 años o igual a 60 años )
    ## Adulto mayor (Mayor o igual a 60 años )
    @app.route("/edades")
    @app.route("/edades/<int:edad>")
    def edades(edad=0): 
        if edad<18:
            R="menor de edad"
        elif(edad<60):
            R="Adulto"
        else:
            R="Adulto mayor"
            return f"<h1>La persona es: {R}</h1> <hr>"
        if __name__=="__main__":
            ## E l valor True indica que la app se deja en modo debug
            app.run(debug=True)
            
## creamos otra ruta realizamos el siguiente ejemplo
##3.) programa para crear arreglos aleatorios
## importamos la librerio numpy si no exite con: pip install nuppy
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arrelglos(valore=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=( filas,columnas))
        return f"<h1>el arreglo aleatorio es: {arreglo}</h1> <hr>"
    if __name__=="__main__":
        ## E l valor True indica que la app se deja en modo debug
            app.run(debug=True)
        