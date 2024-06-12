![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/-Docker-333333?style=flat&logo=docker)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)

# Rol: 🛠️Data Engineer

#### 🛠️Para empezar el proceso, debemos corroborar los datos

**📦 Extraccio**n de datos:

- La fuente de datos para este proyecto fueron 3 enormes archivos json.

🔄 **Transformaciones de los datos:**

- Preparamos los dataset de Steam para la correcta lectura:
- Eliminados columnas irrelevantes para optimizar el rendimiento de la API.
- Eliminados datos faltantes o nulos.
- Eliminados registros o filas repetidas.
- Transformaciones en los tipos de datos.

**📤 Carga de datos limpios**

- Exportamos los archivos en formato parquet por su **peso, eficiencia en la lectura o escritura de datos y acelerando **las consultas****
- Se puede visualizar el proceso 🛠️ ETL en los siguientes links:
  - [🛠️ ETL 📂](https://github.com/Lorenzo09/STEAM_MLOPS/blob/master/1.ETL.ipynb)

**🌐 Desarrollo de la API**

- El sistema se implementa como una **API** a traves del Framework **FastAPI** , lo que permite a los usuarios interactuar con el modelo a través de solicitudes HTTP desde cualquier dispositivo conectado a internet.

**La API ofrece la funcionalidad para obtener la informacion de los siguientes 3 endpoints** :

**FeatureEngeneering**
1. ✅ `developer(desarrollador:str)`: Devuelve la cantidad de juegos y porcentaje de contenido Free por año según la empresa desarrolladora
2. ✅ `userdata(User_id:str): `Dinero gastado por el usuario, porcentaje de recomendación y cantidad de items.
Desarrolladas en el siguiente [Repositorio 📂](https://github.com/Lorenzo09/STEAM_MLOPS/blob/master/2.FutureEngeneering.ipynb)

**MachineLearning**
3. ✅ `recomendacion_juego/{user_id}: `Devuelve una lista de 5 juegos recomendados para un usuario específico.
Desarrollada en el siguiente [Repositorio 📂](https://github.com/Lorenzo09/STEAM_MLOPS/blob/master/4.MACHINELEARNING.ipynb)

#### 🌐 Deployment en Render

1. Creamos un nuevo servicio en Render
2. Lo conectamos a nuestro repositorio.
   1. Para ahorrar espacio en el plan gratuito de Render, utilizamos un repositorio exclusivo para el despliegue con los datos que limpiamos en este proyecto (podes visualizarlo aquí [STEAM_MLOPS_DEPLOYRENDER](https://github.com/Lorenzo09/RenderDeploy.git)).
3. Nuestro servicio está corriendo en el link: [DEPLOY_RENDER](https://steam-mlops-renderdeploy.onrender.com/)