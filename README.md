# Fibonacci Recursivo vs Dinámico

Comparación entre las implementaciones Recursiva y Dinámica de la secuencia de Fibonacci usando Python 🐍.



## Fibonacci

Usaremos la definición recursiva de la secuencia de Fibonacci:
$$
F_{n} = F_{n-1} + F_{n-2}
$$
donde:
$$
F_{0} = 0,\;F_{1} = 1
$$



### Implementación Recursiva

Para la implementación recursiva usaremos únicamente dos casos base ($F_{0} = 0,\;F_{1} = 1$) y la definición recursiva de Fibonacci.

```python
def recursive(n):

	if n <= 1:
		return n

	return recursive(n - 1) + recursive(n - 2)
```



### Implementación Dinámica

Para la implementación dinámica usaremos un diccionario inicializado con dos casos base (`{0: 0, 1: 1}`), un `try-except`, y la definición recursiva de Fibonacci.

```python
def dynamic(n, memo={0: 0, 1: 1}):

	try:
		return memo[n]
	except KeyError:
		memo[n] = dynamic(n - 1, memo) + dynamic(n - 2, memo)
		return memo[n]
```



## Comparación

Compararemos los algoritmos mediante:

* Registro de Tiempos
* Notación Asintótica



### Registro de Tiempos

Usaremos la siguiente función para registrar los tiempos de ejecución de ambas funciones:

```python
def get_times(implementation, samples=10):

	times = []
	for i in range(samples + 1):
		start = time.time()
		implementation(i)
		end = time.time()
		times.append((i, end - start))

	return times
```

La función `get_times` recibe como parámetros la implementación (recursiva o dinámica) y el número de muestras a recolectar, retorna un arreglo de tuplas con el número de la secuencia que se calculó y su respectivo tiempo de ejecución:

images in progress ...



### Notación Asintótica

Las implementaciones recursiva y dinámica tiene una complejidad algorítmica $O(2^{n})$ y $O(n)$ respectivamente. Si bien $O(2^{n})$ representa muy bien el comportamiento de la implementación recursiva, $O(n)$ es una aproximación de la implementación dynamica ya que dicho algoritmo no es estable.



## Conclusión

Podemos concluir según las pruebas realizadas que la implementación recursiva es estable en comparación a la implementación dinámica; sin embargo, la implementación dinámica es mucho más eficiente que la recursiva en términos de su complejidad algoritmica.

Mientras que calcular el número 40 de la secuencia toma aproximadamente 50 segundos con la implementación recursiva, toma entre $1.0\mathrm{e}{-6}$ y $2.0\mathrm{e}{-6}$ segundos calcular el número 400 de la secuencia con la implementación dinámica.

