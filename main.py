from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior 
from kivy.uix.image import Image
from kivy.core.window import Window
class ImageButton1(ButtonBehavior, Image):
    pass
class ImageButton2(ButtonBehavior, Image):
    pass
class ImageButton3(ButtonBehavior, Image):
    pass
class GerenciadorTelas(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tela2(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)
    def apagar2(self):
        self.ids.label2.text = self.ids.label2.text[:-1]
    def decimal(self):
        num=(self.ids.label2.text) #numeros inteiros e decimais na msma variavel
        aux=[] #poe os numeros inteiros no indice 0 e decimais no indice 1
        if ',' in num:
            aux=num.split(',')
            num=''
            num=num+aux[0]
            try: #corrigindo erro caso o usuario idiota digite coisas sem sentido
                a=int(aux[1])/100 #variavel a está com os numeros decimais
            except ValueError:
                self.ids.label2.text=''
                return

            lista=[] #essa lista vai conter os numeros decimais já convertidos pra binario
            for i in range(10):
                a=a*2
                if a==1:
                    lista.append(1)
                    break
                if a<1:
                    lista.append(0)
                if  a>1 :
                    lista.append(1)
                    a=a%1
            a='' #esvazio a variavel para colocar os numeros demais convertidos
            x=0 #variavel pra incrementar o indice
            for j in lista:
                a=a+str(lista[x])
                x+=1

        lista=[] #agora começamos a converter os numeros inteiros para binario
        try:#corrigindo erro caso o usuario aperte o enter varias vezes
            num=int(num) #variavel num está com os numeros inteiros 
        except ValueError:
            self.ids.label2.text=''
            return
        while num>=2:
            lista.append(num%2)
            num=num//2
        lista.append(num%2)
        x=0 #variavel para incremntar o indice
        resultado='' #variavel para armazenar numeros inteiros convertidos
        for k in lista:
            resultado=str(lista[x])+resultado
            x+=1
        if ',' in self.ids.label2.text:
            resultado=resultado +','+a 

        self.ids.bina2.text=self.ids.bina2.text+resultado
        self.ids.dec2.text=self.ids.dec2.text + self.ids.label2.text
       
       #na base hexadecimal
        num=(self.ids.label2.text)
        aux=[]
        if ',' in num:
            aux=num.split(',')
            num=''
            num=num+aux[0]
    
    #tratando a parte inteira
        num=int(num)  
        lista=[]
        while num>=16:
            lista.append(num%16)
            num=num//16
        lista.append(num%16)

        resultado=''
        j=0
        for i in lista:
            if lista[j]==10:
                lista[j]='A'
            elif lista[j]==11:
                lista[j]='B'
            elif lista[j]==12:
                lista[j]='C'
            elif lista[j]==13:
                lista[j]='D'
            elif lista[j]==14:
                lista[j]='E'
            elif lista[j]==15:
                lista[j]='F'
            resultado=str(lista[j])+resultado
            j+=1

        self.ids.hexa2.text=self.ids.hexa2.text+ resultado
        self.ids.label2.text= ''

class Tela1(Screen):

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)
    def apagar(self):
        self.ids.label.text = self.ids.label.text[:-1]
    
    def binario(self):
        resultado=0
        expoente=0
        usu=self.ids.label.text
        for i in usu:
            usu=int(usu)
            resultado+= (usu%10)  * (2**expoente)
            usu=usu//10
            expoente+=1
        self.ids.dec.text=self.ids.dec.text+ str(resultado)
        self.ids.bina.text=self.ids.bina.text + self.ids.label.text
        self.ids.label.text= ''

      #parte hexadecimal
        lista=[]
        final=''
        j=0
        while resultado>16 :
            lista.append(resultado%16)
            resultado= resultado//16
        lista.append(resultado)
        for i in lista:
            if lista[j]==10:
                lista[j]='A'
            elif lista[j]==11:
                lista[j]='B'
            elif lista[j]==12:
                lista[j]='C'
            elif lista[j]==13:
                lista[j]='D'
            elif lista[j]==14:
                lista[j]='E'
            elif lista[j]==15:
                lista[j]='F'
            final=str(lista[j])+ final
            j+=1
        self.ids.hexa.text= self.ids.hexa.text + final

class Tela3(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)
    def apagar3(self):
        self.ids.label3.text = self.ids.label3.text[:-1]
    def hexadecimal(self):
        expoente=0
        acumulador=0
        resultado=0
        numero=self.ids.label3.text
        lista=[]
        for i in numero:
            if (i== 'A'):
                i='10'
                lista.append(i)
            elif (i== 'B'):
                i='11'
                lista.append(i)
            elif (i== 'C'):
                i='12'
                lista.append(i)
            elif (i== 'D'):
                i='13'
                lista.append(i)
            elif (i== 'E'):
                i='14'
                lista.append(i)
            elif (i== 'F'):
                i='15'
                lista.append(i)
            else:
                i=i
                lista.append(i)

        i=len(lista)-1
        for j in range(i+1):
            numero=int(lista[i])
            acumulador+=numero * (16**expoente)
            i-=1
            expoente+=1
        self.ids.dec3.text= self.ids.dec3.text+ str(acumulador)
        self.ids.hexa3.text=self.ids.hexa3.text + self.ids.label3.text
        self.ids.label3.text= ''

#binario
        lista=[]
        j=0
        resultado=''
        while acumulador>=2:
            lista.append(acumulador%2)
            acumulador=acumulador//2
        lista.append(acumulador%2)
        for i in lista:
            resultado=str(lista[j])+resultado
            j+=1
        self.ids.bina3.text=self.ids.bina3.text+ resultado


class Calculadora(App):
    def build(self):
        return GerenciadorTelas()
print("blu")

Calculadora().run()
        

