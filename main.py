
from kivy.app import App
from kivy.lang import Builder

KC = """
<ventana>:
 canvas:
  Color:
   rgb: 30 /255.0,30 / 255.0, 30 / 255.0
  Rectangle:
   size: self.size
   pos: self.pos
 Label:
  text: "Ingrese el valor de x"
  color: 255/255.0,80/255.0,0/255.0
  pos: 60,470
  font_size:  20
 Label:
  text: "Ingrese el valor de y"
  color: 255/255.0,80/255.0,0/255.0
  pos: 60,370
  font_size:  20 
 Label:
  text: "Ingrese el valor de m"
  color: 255/255.0,80/255.0,0/255.0
  pos: 60,265
  font_size:  20   
"""

KV = '''
<FormaButton@Button>:
 font_size: self.width/3
 color: '#FFFFFF'
BoxLayout
 canvas:
  Color:
   rgb: 30 /255.0,30 / 255.0, 30 / 255.0
  Rectangle:
   size: self.size
   pos: self.pos
 uno: valor_m
 dos: valor_x
 tres: valor_y
 cuatro: respuesta
 GridLayout:
  orientation: "tb-rl"
  rows: 6
  cols:2
  padding: 5
  spacing: 5
  BoxLayout:
   orientation: "vertical"
   BoxLayout:
    Label:
     text: "Ingrese el valor de x"
     color: 255/255.0,80/255.0,0/255.0
     pos: 60,470
     font_size:  20
    Label:
     text: "Ingrese el valor de y"
     color: 255/255.0,80/255.0,0/255.0
     pos: 60,370
     font_size:  20
    Label:
     text: "Ingrese el valor de m"
     color: 255/255.0,80/255.0,0/255.0
     pos: 60,265
     font_size:  20
   BoxLayout:  
    TextInput: 
     id:valor_x
     multiline: False
     size: 150,35
     pos: 225,500
     input_filter: "int"
     hint_text: "x"
    TextInput:
     id:valor_y 
     multiline: False
     size: 150,35
     pos: 225,400
     input_filter: "int"
     hint_text: "y"
    TextInput:
     id:valor_m
     multiline: False
     size: 150,35
     pos: 225,300
     input_filter: "int"
     hint_text: "m"
   Button:
    id:calcular
    size: 100,50
    pos: 270,200
    text: "calcular"
    color: 255/255.0,80/255.0,0/255.0
    on_press: app.calculando(calcular.text)
   Button:
    id:limpiar
    size: 100,50
    pos: 100,200
    text: "limpiar"
    color: 255/255.0,80/255.0,0/255.0
    on_press: app.limpiando(limpiar.text)
  BoxLayout:   
   TextInput:
    #size_hint_y:None
    id: respuesta
    size: 400,400
    pos: 400,350
    background_color: 30 /255.0,30 / 255.0, 30 / 255.0
    disabled: True
    disabled_foreground_color: 255/255.0,80/255.0,0/255.0
    text: "y - y1 = m (x - x1)"
    font_size: 25     
'''


def calcular_simbolos(a,b):
    if a > 0 and b > 0 or a < 0 and b < 0:
        return "+"
    else:  
        return "-"


def resolver(m,x,y):
 resultado = []  

 m_por_x = m * x
 if y < 0 and x > 0:
  resultado.append(("y - (",y,") = ",m," (x - ",x,")"))
  y *= -1
  resultado.append(("y + ",y," = ",m," (x - ",x,")"))
  if m_por_x > 0 and m > 0 or m_por_x < 0 and m < 0:
   m_por_x *= -1 
   resultado.append(("y + ",y," = ",m,"x + ",m_por_x))
   y *= -1
   resultado.append(("y = ",m,"x + ",m_por_x," ", y))
   if "+" in calcular_simbolos(m_por_x,y): 
        if m_por_x + y < 0:  
            resultado.append(("y = ",m,"x"," ", m_por_x + y))
        else:
            resultado.append(("y = ",m,"x" ,calcular_simbolos(m_por_x,y)," ", m_por_x + y))  
   else: 
        if m_por_x + y < 0:  
            resultado.append(("y = ",m,"x" , " ",m_por_x - y))
        else:  
            resultado.append(("y = ",m,"x" ,"+ ",m_por_x + y)) 

  else:
   resultado.append(("y + ",y," = ",m,"x" ," ",m_por_x))
  
 elif x < 0 and y > 0 :  
  resultado.append(("y - ",y, "= ",m," ", "(x - (",x,"))"))
  x *= -1
  resultado.append(("y - ",y," = ",m," (x + ",x,")"))
  if m_por_x < 0:
   m_por_x *= -1 
   resultado.append(("y - ",y," = ",m,"x + ",m_por_x))
   resultado.append(("y = ",m,"x + ",m_por_x," + ",y))
   if "+" in calcular_simbolos(m_por_x,y):
        if m_por_x + y < 0:  
            resultado.append(("y = ",m,"x ",m_por_x + y))
        else:
            resultado.append(("y = ",m,"x ", calcular_simbolos(m_por_x,y), m_por_x + y))  
   else: 
        if m_por_x + y < 0:   
            resultado.append(("y = ",m,"x ",m_por_x - y))
        else:      
            resultado.append(("y = ",m,"x ",calcular_simbolos(m_por_x,y)," ", m_por_x - y))
  else:
   m_por_x *= -1 
   resultado.append(("y - ",y," = ",m,"x " ,m_por_x))
   resultado.append(("y = ",m,"x ",m_por_x," + ",y))

   if "+" in calcular_simbolos(m_por_x,y):
        if m_por_x + y < 0:   
            resultado.append(("y = ",m,"x ",m_por_x + y))
        else:   
            resultado.append(("y = ",m,"x ",calcular_simbolos(m_por_x,y)," ",m_por_x + y))  
   else:
        if m_por_x - y < 0:   
            resultado.append(("y = ",m,"x ",m_por_x + y))
        else:
            resultado.append(("y = ",m,"x ",m_por_x - y)) 
 elif y < 0 and x < 0:
    resultado.append(("y - (",y,") = ",m," ","(x - (",x,"))"))
    y *= -1
    x *= -1
    resultado.append(("y + ",y," = ",m," (x + ",x,")"))
    if m_por_x < 0:
        m_por_x *= -1 
        y *= -1
        resultado.append(("y + ",y," = ",m,"x + ",m_por_x))
        resultado.append(("y = ",m,"x + ",m_por_x,y))
        if "+" in calcular_simbolos(m_por_x,y):
            if m_por_x + y < 0:  
                resultado.append(("y = ",m,"x ",m_por_x + y ))
            else:
                resultado.append(("y = ",m,"x ",calcular_simbolos(m_por_x,y)," ",m_por_x + y))  
        else:
            if m_por_x + y < 0:
                y *= -1  
                resultado.append(("y = ",m,"x " ,m_por_x - y))
            else:
                resultado.append(("y = ",m,"x ",m_por_x - y))
    else:
        m_por_x *= -1 
        resultado.append(("y + ",y," = ",m," x ",m_por_x))
        y *= -1
        resultado.append(("y = ",m,"x  ",m_por_x," ",y))

    if "+" in calcular_simbolos(m_por_x, y):
        if m_por_x + y < 0:
            resultado.append(("y = ", m, "x ", m_por_x + y))
        else:
            resultado.append(
                ("y = ", m, "x ", calcular_simbolos(m_por_x, y), " ", m_por_x + y))
    else:
        if m_por_x + y < 0:
            y *= -1
            resultado.append(("y = ", m, "x ",m_por_x - y))
        else:
            resultado.append(("y = ", m, "x ",m_por_x - y))     
 else:
    resultado.append(("y - ",y," = ",m," (x - ",x,")"))
    resultado.append(("y - ",y," = ",m,"x - ",m_por_x))
    resultado.append(("y = ",m,"x - ",m_por_x," + ",y))
    m_por_x *= -1

    if m_por_x + y < 0: 
        resultado.append(("y = ",m,"x ",m_por_x + y))
    else:
        resultado.append(("y = ",m,"x ","+ ",m_por_x + y))

 return resultado 

class Calculadora(App):
    def calculando(self,instance):
     for i in resolver(int(self.root.uno.text),int(self.root.dos.text),int(self.root.tres.text)):
        a = str(i).replace(",","").replace("'","").replace("(","",1).replace(")","",1)  
        self.root.cuatro.insert_text("\n")
        #self.root.cuatro.insert_text("\n")
        self.root.cuatro.insert_text(str(a)+ "\n")
    def limpiando(self,instance):
     self.root.cuatro.text = "y - y1 = m (x - x1)"    
     self.root.uno.text = ""
     self.root.dos.text = ""
     self.root.tres.text = ""
    title = "Ecuacion Punto Pendiente"
    def build(self):
        return Builder.load_string(KV)
if __name__ == "__main__":
    Calculadora().run()     
    