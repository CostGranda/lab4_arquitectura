
# coding: utf-8

# In[92]:


import matplotlib.pyplot as plt
import numpy as np
import RPi.GPIO as GPIO
np.seterr(divide='ignore', invalid='ignore')


# In[93]:


LED1 = 13
LED2 = 19
LED3 = 26
LED4 = 20


def setup_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.setup(LED3, GPIO.OUT)
    GPIO.setup(LED4, GPIO.OUT)


def leds_off():
    GPIO.output(LED1, GPIO.LOW)
    GPIO.output(LED2, GPIO.LOW)
    GPIO.output(LED3, GPIO.LOW)
    GPIO.output(LED4, GPIO.LOW)


def led_on(led):
    GPIO.output(led, GPIO.HIGH)
    print("Led ON")


# In[3]:


def valores(a=-0.5, b=0.5):
    x = np.arange(a, b, 0.02)
    y = (np.tanh(3*x) - np.cos(3*x)/np.sin(3*x)) / (((2*x)/5) - 3*x)
    return {'x': x, 'y': y, 'puntos': b - a + 1}


# In[66]:


def cuadrantes(a, b, num, cant):
    if(a <= num <= a+cant):
        leds_off()
        print("Cuadrante 1")
        led_on(LED1)
    elif(a <= num <= a+cant*2):
        leds_off()
        print("Cuadrante 2")
        led_on(LED2)
    elif(a <= num <= a+cant*3):
        leds_off()
        print("Cuadrante 3")
        led_on(LED3)
    elif(a <= num <= b):
        leds_off()
        print("Cuadrante 4")
        led_on(LED4)


# In[90]:


def graficar(a=1, b=1, x=None):
    rangos = valores(a, b)
    delta = (b - a) / 4
    plt.plot(rangos['x'], rangos['y'])
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    for i in range(1, 4):
        plt.axvline(x=a+delta*i, linestyle='--', color='g')
    plt.title("Grafica lab 4")
    if x is not None:
        y = (np.tanh(3*x) - np.cos(3*x)/np.sin(3*x)) / (((2*x)/5) - 3*x)
        plt.annotate("({},{:.1f})".format(x, y), xy=(x, y), xytext=(
            3, 1.5), size=12, arrowprops=dict(arrowstyle='->'))
    plt.text(
        b+1, a-1, r'$f(x)=\frac{tanh(3x) - cot(3x)} {\frac{2x}{5}-{3x}} $', color='g', fontsize=20)


# In[91]:


opc = int(input("""
1) Acotar por X
2) Acotar por Y
3) Evaluar
4) Salir
"""))
x = None
if(opc == 1):
    x = eval(input("Ingrese el rango [a,b]: "))
    #rangos = valores(x[0], x[1])
    graficar(x[0], x[1])
elif(opc == 2):
    pass
elif(opc == 3):
    x = eval(input("Ingrese el rango [a,b]: "))
    print(type(x[0]))
    punto = eval(input("Ingrese el valor a evaluar: "))
    graficar(x[0], x[1], punto)
elif(opc == 4):
    exit()
