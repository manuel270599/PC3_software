# Compresor de datos con el algoritmo de Huffman

La estructura del proyecto es de la siguiente manera:

![image](https://github.com/user-attachments/assets/326774cb-a0d8-4961-953b-b8ee7f4d9071)

## Explicación del codigo principal:
La clase **HuffmanNode** representa un nodo del árbol de Huffman.

Método __lt__: Este método permite comparar nodos de Huffman basados en la frecuencia

![image](https://github.com/user-attachments/assets/6c7d8f6e-a593-4fd5-88db-2f333510436d)

## 
La función **build_huffman_tree** construye el árbol de Huffman a partir del texto aquí se calcula la frecuencia de cada carácter en el texto usando Counter.
Se crea una lista de nodos HuffmanNode para cada carácter y su frecuencia y se convierte esta lista en una cola de prioridad que organiza los nodos en orden ascendente de frecuencia.
Se fusionan los dos nodos con menor frecuencia hasta que solo quede un nodo, que será la raíz del árbol de Huffman.

![image](https://github.com/user-attachments/assets/c484d2c8-2342-4433-95a1-b58e08e7281d)


##
La función **build_huffman_codes** genera los códigos de Huffman (cadenas de bits) para cada carácter basado en el árbol de Huffman:

![image](https://github.com/user-attachments/assets/5009f02e-560d-45e9-87b5-61ea4cba5729)

##
La función **compress** comprime el texto usando el algoritmo de Huffman
La función **decompress** descomprime el texto usando el árbol de Huffman

![image](https://github.com/user-attachments/assets/9b13cb5d-8c08-4b6d-a2cf-1fc658f545f0)

## 
### Función write_tree_to_file
Esta función serializa el árbol de Huffman y lo guarda en un archivo.

![image](https://github.com/user-attachments/assets/bf693b2a-e91b-40e4-a893-17c54c3704ec)

##
### Función some_function
Esta función simplemente llama a **write_tree_to_file**, guardando el árbol en un archivo llamado **tree.txt**.

![image](https://github.com/user-attachments/assets/7396b807-e7f0-49ba-aed6-e0d6a8eb5855)

##
### Parte principal del código

![image](https://github.com/user-attachments/assets/f1b6e0ce-2b8d-486b-a4ef-ac48bcd31392)


##
### Se define el texto "AAABBCCCC". 
Resultados:

![image](https://github.com/user-attachments/assets/559956d8-b6cf-4799-8ed0-d00a05101d3c)

##
# Archivos Dockerfile y devcontainer:

![image](https://github.com/user-attachments/assets/57dc8282-cd11-4c3d-8f4c-05cdea90bffa)

![image](https://github.com/user-attachments/assets/4ed8b488-b200-4d74-9373-69e93e799cff)

## 
# Requeriments:
Estan todas las versiones y herramientas que se usan en el contenedor, no es optimo no escribir las versiones en cada herramienta por ende acá lo especifico y asi evito conflictos al menos en mi ordenador.

![image](https://github.com/user-attachments/assets/6db81095-fea9-447e-8f3a-2d221c68d9ab)

##
# Pruebas Unitarias
##
### Método setUp
Se ejecuta antes de cada prueba individual. 
Su función es preparar los datos comunes que se usarán en las pruebas

![image](https://github.com/user-attachments/assets/1fcdc27b-1c9e-4588-b99d-87a51be21e8e)

##
Método ***test_build_huffman_tree***  verifica que la función build_huffman_tree cree un árbol de Huffman válido.

Método ***test_build_huffman_codes*** verifica que la función build_huffman_codes genere correctamente los códigos de Huffman para cada carácter.

Método ***test_compress*** prueba que las funciones compress y decompress trabajen correctamente.

![image](https://github.com/user-attachments/assets/929c1ff6-d55e-4b6d-b928-5d25feb7686d)

##

## Mocks

Método ***test_write_tree_to_file*** verifica que la función write_tree_to_file intente abrir un archivo y escribir el árbol en el archivo.
Se utiliza mock.patch para reemplazar la función **open** de builtins por un objeto mock_open, simula la apertura de archivos sin necesidad de interactuar realmente con el sistema de archivos  evitando la ejecucion del codigo
principal para el testeo de la función

![image](https://github.com/user-attachments/assets/a1191c87-5a75-4fec-a69e-21f410adaf71)

Método **test_some_function** verifica que la función some_function llame correctamente a la función write_tree_to_file.
Aquí se usa mock.patch para reemplazar la función **write_tree_to_file** por un "mock" que simula su comportamiento.
**mock_write_tree.assert_called_once_with(self.tree, "tree.txt")** verifica que write_tree_to_file haya sido llamada una vez con los parámetros correctos (self.tree y "tree.txt").

![image](https://github.com/user-attachments/assets/7c837fe3-597f-4882-9817-e985e12e8638)

## Verificamos que las pruebas pasen:

![image](https://github.com/user-attachments/assets/9884d11b-b99a-403f-b908-68eae9b67ef1)


## Cobertura de código 

Vemos cuanto de cobertura dentro del código se ha abarcado

![image](https://github.com/user-attachments/assets/9cfb130b-b919-4eb0-b012-ae13c9f40d5a)

Dentro del contenedor:

![image](https://github.com/user-attachments/assets/9b5ea2d5-9c36-4e09-968c-61be5a1b7d49)

## Ejecución dentro del contenedor:

![image](https://github.com/user-attachments/assets/25e1ccd8-aac8-4527-ad2c-dcba5a968ba0)

## Conclusiones 
Si bien no hay un manejo de datos mucho mas grandes el programa se presta para ser adaptado o ser solicitado en cualquier aplicación, bajos fines del quien programa se usa datos simples para una buena explicación.

##
##
##
# Fin de contenido


