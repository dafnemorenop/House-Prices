## Descripción de variables y sus Valores

Este documento describe las variables utilizadas en el análisis de datos de NTTData, obtenidas de dos archivos CSV que contienen datos de entrenamiento y prueba. A continuación se presenta la descripción de cada variable junto con los valores posibles.


## 1. Variable: SalePrice
- **Descripción**: Precio de venta de la propiedad en dólares. Esta es la variable objetivo que se intenta predecir.
- **Tipo**: Flotante
- **Valores posibles**:
  - Desde 34,900.0 hasta 755,000.0 (los valores NaN corresponden a los datos de prueba).
  
## 2. Variable: MSSubClass
- **Descripción**: Clase del edificio.
- **Tipo**: Entero
- **Valores posibles**:
  - `60`: Vivienda unifamiliar de un solo piso (1 story).
  - `20`: Vivienda bifamiliar de un solo piso (1 story).
  - `70`: Vivienda unifamiliar de dos pisos (2 story).
  - `50`: Duplex (propiedad de dos unidades).
  - `190`: Vivienda unifamiliar de un solo piso en un PUD (planned unit development).
  - `45`: Propiedades residenciales de tipo misceláneo.
  - `90`: Vivienda unifamiliar de dos pisos en un PUD (2 story, PUD).
  - `120`: Propiedades ubicadas en zonas cercanas a parques.
  - `30`: Condominio.
  - `85`: Vivienda multifamiliar de dos pisos (2 stories).
  - `80`: Vivienda unifamiliar de nivel dividido (split-level).
  - `160`: Vivienda unifamiliar de un piso y medio (1.5 stories).
  - `75`: Vivienda unifamiliar de dos pisos en un PUD (2 story, PUD).
  - `180`: Vivienda unifamiliar de tres pisos (3 story).
  - `40`: Vivienda multifamiliar de un solo piso (1 story).
  - `150`: Vivienda bifamiliar de dos pisos (2 story).

  (PUD) o Desarrollo de Unidad Planificada es un tipo de desarrollo inmobiliario que combina características residenciales, comerciales, industriales y recreativas dentro de una misma comunidad o área específica.

## 3. Variable: MSZoning
- **Descripción**: Clasificación de zonificación general.
- **Tipo**: Objeto
- **Valores posibles**:
  - `RL`: Zona residencial de baja densidad
  - `RM`: Zona residencial de media densidad
  - `C (all)`: Zona comercial
  - `FV`: Zona residencial flotante (planificada)
  - `RH`: Zona residencial alta densidad

## 4. Variable: LotFrontage
- **Descripción**: Pies lineales de calle conectados a la propiedad.
- **Tipo**: Flotante

## 5. Variable: LotArea
- **Descripción**: Tamaño del lote en pies cuadrados.
- **Tipo**: Entero

## 6. Variable: Street
- **Descripción**: Tipo de acceso por carretera.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Pave`: Pavimentado
  - `Grvl`: Grava

## 7. Variable: Alley
- **Descripción**: Tipo de acceso por callejón.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Grvl`: Callejón de grava
  - `Pave`: Callejón pavimentado

## 8. Variable: LotShape
- **Descripción**: Forma general de la propiedad.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Reg`: Regular
  - `IR1`: Levemente irregular
  - `IR2`: Moderadamente irregular
  - `IR3`: Muy irregular

## 9. Variable: LandContour
- **Descripción**: Planicidad de la propiedad.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Lvl`: Nivelado
  - `Bnk`: Terreno con pendiente hacia la calle
  - `HLS`: Ladera
  - `Low`: Depresión

## 10. Variable: Utilities
- **Descripción**: Tipo de servicios disponibles.
- **Tipo**: Objeto
- **Valores posibles**:
  - `AllPub`: Todos los servicios públicos (agua, electricidad, gas)
  - `NoSeWa`: Sin alcantarillado

## 11. Variable: LotConfig
- **Descripción**: Configuración del lote.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Inside`: Lote interior
  - `Corner`: Lote en esquina
  - `CulDSac`: Cul-de-sac (carretera sin salida)
  - `FR2`: Frontal a dos calles
  - `FR3`: Frontal a tres calles

## 12. Variable: LandSlope
- **Descripción**: Pendiente de la propiedad.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Gtl`: Terreno ligeramente inclinado
  - `Mod`: Terreno moderadamente inclinado
  - `Sev`: Terreno severamente inclinado

## 13. Variable: Neighborhood (Vecindario)
- **Descripción**: Ubicaciones físicas dentro de los límites de la ciudad de Ames.
- **Tipo**: Objeto
- **Valores posibles**:
  - `CollgCr`: College Creek (Arroyo de la Universidad)
  - `Veenker`: Veenker
  - `Crawfor`: Crawford
  - `NoRidge`: North Ridge (Ridge Norte)
  - `Mitchel`: Mitchell
  - `Somerst`: Somerset
  - `NWAmes`: North West Ames (Ames Noroeste)
  - `OldTown`: Old Town (Ciudad Vieja)
  - `BrkSide`: Brookside (Lado del Arroyo)
  - `Sawyer`: Sawyer
  - `NridgHt`: North Ridge Heights (Alturas de North Ridge)
  - `NAmes`: North Ames (Ames Norte)
  - `SawyerW`: Sawyer West (Sawyer Oeste)
  - `IDOTRR`: Iowa Department of Transportation Rail Road (Ferrocarril del Departamento de Transporte de Iowa)
  - `MeadowV`: Meadow Village (Aldea de Meadow)
  - `Edwards`: Edwards
  - `Timber`: Timber (Madera)
  - `Gilbert`: Gilbert
  - `StoneBr`: Stone Brook (Arroyo de Piedra)
  - `ClearCr`: Clear Creek (Arroyo Claro)
  - `NPkVill`: North Park Village (Aldea del Parque Norte)
  - `Blmngtn`: Bloomington
  - `BrDale`: Brook Dale (Dale del Arroyo)
  - `SWISU`: South West Iowa State University (Universidad Estatal de Iowa Suroeste)
  - `Blueste`: Blue Stone (Piedra Azul)

## 14. Variable: Condition1
- **Descripción**: Proximidad a diversas condiciones, como carreteras principales, secundarias o ferrocarriles.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Norm`: Normal.
  - `Feedr`: Adyacente a una calle secundaria.
  - `PosN`: Cerca de una característica positiva fuera del sitio (parque, cinturón verde, etc.).
  - `Artery`: Adyacente a una calle arterial.
  - `RRAe`: Adyacente al ferrocarril Este-Oeste.
  - `RRNn`: A menos de 200 pies (aproximadamente 61 metros) del ferrocarril Norte-Sur.
  - `RRAn`: Adyacente al ferrocarril Norte-Sur.
  - `PosA`: Adyacente a una característica positiva fuera del sitio.
  -  `RRNe`: A menos de 200 pies del ferrocarril Este-Oeste
## 15. Variable: Condition2
- **Descripción**: Proximidad a la carretera principal o ferrocarril (si hay un segundo presente).
- **Tipo**: Objeto
- **Valores posibles**:
  - `Norm`: Normal  
  - `Artery`: Adyacente a una calle arterial  
  - `Feedr`: Adyacente a una calle secundaria  
  - `PosN`: Cerca de una característica positiva fuera del sitio (parque, cinturón verde, etc.)  
  - `RRAe`: Adyacente al ferrocarril Este-Oeste  
  - `RRNn`: A menos de 200 pies (aproximadamente 61 metros) del ferrocarril Norte-Sur  
  - `RRAn`: Adyacente al ferrocarril Norte-Sur  
  - `PosA`: Adyacente a una característica positiva fuera del sitio  

## 16. Variable: BldgType
- **Descripción**: Tipo de vivienda.
- **Tipo**: Objeto
- **Valores posibles**:
  - `1Fam`: Vivienda unifamiliar
  - `2FmCon`: Duplex (conversion)
  - `Duplex`: Duplex estándar
  - `TwnhsE`: Casa adosada esquina
  - `Twnhs`: Casa adosada interior

## 17. Variable: HouseStyle
- **Descripción**: Estilo de la vivienda.
- **Tipo**: Objeto
- **Valores posibles**:
  - `1Story`: Una planta  
  - `1.5Fin`: Una y media plantas: nivel superior terminado  
  - `1.5Unf`: Una y media plantas: nivel superior sin terminar  
  - `2Story`: Dos plantas  
  - `2.5Fin`: Dos y media plantas: nivel superior terminado  
  - `2.5Unf`: Dos y media plantas: nivel superior sin terminar  
  - `SFoyer`: Entrada tipo Split Foyer (separada por escaleras) 
  - `SLvl`: Entrada tipo Split Level (desniveles internos)

## 18. Variable: OverallQual
- **Descripción**: Calidad general de los materiales y acabados.
- **Tipo**: Entero
- **Valores posibles**:
  - Rango de 1 a 10 (donde 1 es de mala calidad y 10 es de excelente calidad)

## 19. Variable: OverallCond
- **Descripción**: Calificación de la condición general.
- **Tipo**: Entero
- **Valores posibles**:
  - Rango de 1 a 9 (donde 1 es de mala condición y 9 es de muy buena condición)

## 20. Variable: YearBuilt
- **Descripción**: Fecha de construcción original.
- **Tipo**: Entero
- **Valores posibles**:
  - Año entre 1872 y 2010

## 21. Variable: YearRemodAdd
- **Descripción**: Fecha de remodelación.
- **Tipo**: Entero
- **Valores posibles**:
  - Año entre 1950 y 2010

## 22. Variable: RoofStyle
- **Descripción**: Tipo de techo.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Gable`: A dos aguas
  - `Hip`: A cuatro aguas
  - `Flat`: Plano
  - `Mansard`: Mansarda (techo de doble inclinación)
  - `Gambrel`: Techo granero
  - `Shed`: Techo inclinado

## 23. Variable: RoofMatl
- **Descripción**: Material del techo.
- **Tipo**: Objeto
- **Valores posibles**:
  - `CompShg`: Teja compuesta
  - `WdShngl`: Teja de madera
  - `Metal`: Metal
  - `WdShake`: Teja de madera (se refiere a tablones de madera)
  - `Membran`: Membrana
  - `Tar&Grv`: Teja de asfalto y grava
  - `Roll`: Techo enrollado
  - `ClyTile`: Teja de arcilla

## 24. Variable: Exterior1st
- **Descripción**: Recubrimiento exterior de la casa.
- **Tipo**: Objeto
- **Valores posibles**:
  - `VinylSd`: Vinilo
  - `MetalSd`: Metal
  - `Wd Sdng`: Madera (wood siding)
  - `HdBoard`: Tablero de alta densidad
  - `BrkFace`: Ladrillo
  - `WdShing`: Tejas de madera
  - `CemntBd`: Cemento
  - `Plywood`: Contrachapado
  - `AsbShng`: Recubrimiento de asbesto
  - `Stucco`: Estuco
  - `BrkComm`: Ladrillo comercial
  - `AsphShn`: Recubrimiento asfáltico
  - `Stone`: Piedra
  - `ImStucc`: Estuco sintético
  - `CBlock`: Bloques de concreto

## 25. Variable: Exterior2nd
- **Descripción**: Recubrimiento exterior de la casa (si hay más de un material).
- **Tipo**: Objeto
- **Valores posibles**:
  - `VinylSd`: Vinilo
  - `MetalSd`: Metal
  - `Wd Shng`: Tejas de madera
  - `HdBoard`: Tablero de alta densidad
  - `Plywood`: Contrachapado
  - `Wd Sdng`: Madera (wood siding)
  - `CmentBd`: Cemento
  - `BrkFace`: Ladrillo
  - `Stucco`: Estuco
  - `AsbShng`: Recubrimiento de asbesto
  - `Brk Cmn`: Ladrillo común
  - `ImStucc`: Estuco sintético
  - `AsphShn`: Recubrimiento asfáltico
  - `Stone`: Piedra
  - `Other`: Otro material
  - `CBlock`: Bloques de concreto

## 26. Variable: MasVnrType
- **Descripción**: Tipo de revestimiento de mampostería.
- **Tipo**: Objeto
- **Valores posibles**:
  - `BrkFace`: Ladrillo
  - `Stone`: Piedra
  - `BrkCmn`: Ladrillo común

## 27. Variable: MasVnrArea
- **Descripción**: Área de revestimiento de mampostería en pies cuadrados.
- **Tipo**: Flotante

## 28. Variable: ExterQual
- **Descripción**: Calidad del material exterior.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular

## 29. Variable: ExterCond
- **Descripción**: Condición actual del material exterior.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular
  - `Po`: Pobre

## 30. Variable: Foundation
- **Descripción**: Tipo de cimentación.
- **Tipo**: Objeto
- **Valores posibles**:
  - `PConc`: Concreto
  - `CBlock`: Bloque de cemento
  - `BrkTil`: Ladrillo
  - `Slab`: Losa
  - `Stone`: Piedra
  - `Wood`: Madera

## 31. Variable: BsmtQual
- **Descripción**: Altura del sótano.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular

## 32. Variable: BsmtCond
- **Descripción**: Condición general del sótano.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular
  - `Po`: Pobre

## 33. Variable: BsmtExposure
- **Descripción**: Indica la calidad de la exposición de las paredes del sótano que están al nivel del suelo o al nivel del jardín. Esta variable se refiere a la cantidad de luz natural y la visibilidad que recibe el sótano a través de las ventanas o aberturas. 
- **Tipo**: Objeto
- **Valores posibles**:
  - `Gd`: Buena
  - `Av`: Promedio
  - `Mn`: Mínima
  - `No`: Ninguna

## 34. Variable: BsmtFinType1
- **Descripción**: Calidad del área terminada del sótano.
- **Tipo**: Objeto
- **Valores posibles**:
  - `GLQ`: Buena calidad
  - `ALQ`: Calidad aceptable
  - `BLQ`: Calidad de finalización mínima
  - `Rec`: Recreativo
  - `LwQ`: Calidad baja
  - `Unf`: Sin terminar

## 35. Variable: BsmtFinSF1
- **Descripción**: Pies cuadrados terminados del tipo 1.
- **Tipo**: Flotante

## 36. Variable: BsmtFinType2
- **Descripción**: Calidad del segundo área terminada (si está presente).
- **Tipo**: Objeto
- **Valores posibles**:
  - `GLQ`: Buena calidad
  - `ALQ`: Calidad aceptable
  - `BLQ`: Calidad de finalización mínima
  - `Rec`: Recreativo
  - `LwQ`: Calidad baja
  - `Unf`: Sin terminar

## 37. Variable: BsmtFinSF2
- **Descripción**: Pies cuadrados terminados del tipo 2.
- **Tipo**: Flotante

## 38. Variable: BsmtUnfSF
- **Descripción**: Pies cuadrados sin terminar del área del sótano. 
- **Tipo**: Flotante

## 39. Variable: TotalBsmtSF
- **Descripción**: Pies cuadrados totales del área del sótano.     
- **Tipo**: Flotante

## 40. Variable: Heating
- **Descripción**: Tipo de calefacción.
- **Tipo**: Objeto
- **Valores posibles**:
  - `GasA`: Gas de ciudad
  - `GasW`: Gas de agua
  - `Grav`: Calefacción de gravedad
  - `OthW`: Otra calefacción
  - `Wall`: Calefacción de pared
  - `Floor`: Calefacción de suelo

## 41. Variable: HeatingQC
- **Descripción**: Calidad de calefacción.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular
  - `Po`: Pobre

## 42. Variable: CentralAir
- **Descripción**: Aire acondicionado central.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Y`: Sí
  - `N`: No

## 43. Variable: Electrical
- **Descripción**: Sistema eléctrico.
- **Tipo**: Objeto
- **Valores posibles**:
  - `SBrkr`: Interruptor automático (sistema de disyuntores)
  - `FuseA`: Fusibles de 60 amperios y más
  - `FuseF`: Fusibles de 60 amperios
  - `FuseP`: Fusibles de 30 amperios
  - `Mix`: Mixto (combinación de diferentes sistemas eléctricos)

## 44. Variable: 1stFlrSF
- **Descripción**: Área del primer piso (pies cuadrados).
- **Tipo**: Flotante

## 45. Variable: 2ndFlrSF
- **Descripción**: Área del segundo piso (pies cuadrados).
- **Tipo**: Flotante

## 46. Variable: LowQualFinSF
- **Descripción**: Área de finalización de baja calidad.
- **Tipo**: Flotante

## 47. Variable: GrLivArea
- **Descripción**: Área de vida sobre el suelo (piedra cuadrada).
- **Tipo**: Flotante

## 48. Variable: BsmtFullBath
- **Descripción**: Número de baños completos en el sótano.
- **Tipo**: Entero
- **Valores posibles**:
  - De 0 a 3 baños en el sótano

## 49. Variable: BsmtHalfBath
- **Descripción**: Número de baños de media en el sótano.
- **Tipo**: Entero

## 50. Variable: FullBath
- **Descripción**: Número de baños completos.
- **Tipo**: Entero
- **Valores posibles**:
  - De 0 a 4 baños

## 51. Variable: HalfBath
- **Descripción**: Número de baños de media.
- **Tipo**: Entero
- **Valores posibles**:
  - De 0 a 2 baños 

## 52. Variable: BedroomAbvGr
- **Descripción**: Número de dormitorios por encima del nivel del suelo.
- **Tipo**: Entero
- **Valores posibles**:
  - De 0 a 8 dormitorios encima del nivel del suelo

## 53. Variable: KitchenAbvGr
- **Descripción**: Número de cocinas por encima del nivel del suelo.
- **Tipo**: Entero
- **Valores posibles**:
  - De 0 a 3 cocinas

## 54. Variable: KitchenQual
- **Descripción**: Calidad de la cocina.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular

## 55. Variable: TotRmsAbvGrd
- **Descripción**: Total de habitaciones por encima del nivel del suelo (sin contar baños).
- **Tipo**: Entero
- **Valores posibles**:
  - De 2 a 15 habitaciones

## 56. Variable: Functional
- **Descripción**: Funcionalidad de la vivienda.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Typ`: Típico
  - `Min1`: Minimamente funcional
  - `Min2`: Minimamente funcional
  - `Mod`: Moderadamente funcional
  - `Maj1`: Mayormente funcional
  - `Maj2`: Mayormente funcional
  - `Sev`: Severamente funcional

## 57. Variable: Fireplaces
- **Descripción**: Número de chimeneas.
- **Tipo**: Entero
- **Valores posibles**:
  - De 0 a 4 chimeneas

## 58. Variable: FireplaceQu
- **Descripción**: Calidad de la chimenea.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular
  - `Po`: Pobre

## 59. Variable: GarageType
- **Descripción**: Ubicación del garaje.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Attchd`: Garaje adjunto (conectado directamente a la casa)
  - `Detchd`: Garaje separado (independiente de la casa)
  - `BuiltIn`: Garaje integrado (construido como parte de la estructura principal de la casa)
  - `CarPort`: Cochera (espacio cubierto pero sin paredes)
  - `Basement`: Garaje en el sótano (debajo de la casa)
  - `2Types`: Dos tipos de garaje presentes en la propiedad

## 60. Variable: GarageYrBlt
- **Descripción**: Año en que se construyó el garaje.
- **Tipo**: Entero
- **Valores posibles**:
  - De 1915 a 2010 (Hay un valor de 2207 que hay que modificar)

## 61. Variable: GarageFinish
- **Descripción**: Acabado interior del garaje.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Fin`: Terminado
  - `RFn`: Terminado con calefacción
  - `Unf`: Sin terminar

## 62. Variable: GarageCars
- **Descripción**: Tamaño del garaje en capacidad de automóviles.
- **Tipo**: Entero
- **Valores posibles**:
  - De 0 a 5 garajes

## 63. Variable: GarageArea
- **Descripción**: Tamaño del garaje en pies cuadrados.
- **Tipo**: Flotante

## 64. Variable: GarageQual
- **Descripción**: Calidad del garaje.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular
  - `Po`: Pobre

## 65. Variable: GarageCond
- **Descripción**: Condición del garaje.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `TA`: Aceptable
  - `Fa`: Regular
  - `Po`: Pobre

## 66. Variable: PavedDrive
- **Descripción**: Entrada pavimentada.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Y`: Sí
  - `N`: No
  - `P`: Parcial

## 67. Variable: WoodDeckSF
- **Descripción**: Área de la cubierta de madera en pies cuadrados.
- **Tipo**: Entero

## 68. Variable: OpenPorchSF
- **Descripción**: Área de porche abierto en pies cuadrados.
- **Tipo**: Entero

## 69. Variable: EnclosedPorch
- **Descripción**: Área del porche cerrado en pies cuadrados.
- **Tipo**: Entero

## 70. Variable: 3SsnPorch
- **Descripción**: Área de porche de tres estaciones en pies cuadrados.
- **Tipo**: Entero

## 71. Variable: ScreenPorch
- **Descripción**: Área de porche con pantalla en pies cuadrados.
- **Tipo**: Entero

## 72. Variable: PoolArea
- **Descripción**: Área de la piscina en pies cuadrados.
- **Tipo**: Entero

## 73. Variable: PoolQC
- **Descripción**: Calidad de la piscina.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Ex`: Excelente
  - `Gd`: Buena
  - `Fa`: Regular

## 74. Variable: Fence
- **Descripción**: Calidad de la cerca.
- **Tipo**: Objeto
- **Valores posibles**:
  - `GdPrv`: Buena privacidad
  - `MnPrv`: Privacidad mínima
  - `GdWo`: Buena sin privacidad
  - `MnWw`: Mínima sin privacidad

## 75. Variable: MiscFeature
- **Descripción**: Característica adicional de la propiedad no cubierta en otras categorías.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Shed`: Cobertizo 
  - `Gar2`: Garaje doble 
  - `Othr`: Otro 
  - `TenC`: Cancha de tenis 

## 76. Variable: MiscVal
- **Descripción**: Valor de la característica adicional.
- **Tipo**: Entero

## 77. Variable: MoSold
- **Descripción**: Mes de la venta.
- **Tipo**: Entero
- **Valores posibles**:
  - `1`: Enero
  - `2`: Febrero
  - `3`: Marzo
  - `4`: Abril
  - `5`: Mayo
  - `6`: Junio
  - `7`: Julio
  - `8`: Agosto
  - `9`: Septiembre
  - `10`: Octubre
  - `11`: Noviembre
  - `12`: Diciembre

## 78. Variable: YrSold
- **Descripción**: Año de la venta.
- **Tipo**: Entero
- **Valores posibles**:
  - Año entre 2006 y 2010

## 79. Variable: SaleType
- **Descripción**: Tipo de venta.
- **Tipo**: Objeto
- **Valores posibles**:
  - `WD`: Venta normal (Warranty Deed - Escritura de garantía común)
  - `New`: Casa nueva (venta de una casa recién construida y nunca ocupada)
  - `COD`: Venta en efectivo (Cash on Delivery)
  - `ConLD`: Contrato de venta a largo plazo (Long-term Contract with Low Down Payment)
  - `ConLI`: Contrato de venta a bajo interés (Contract with Low Interest Rate)
  - `CWD`: Venta con escritura especial de garantía (Contract Warranty Deed)
  - `ConLw`: Contrato de venta con pago inicial bajo (Contract with Low Down Payment)
  - `Con`: Venta mediante contrato general
  - `Oth`: Otro tipo de venta (no clasificada en las opciones anteriores)

## 80. Variable: SaleCondition
- **Descripción**: Condición de venta.
- **Tipo**: Objeto
- **Valores posibles**:
  - `Normal`: Venta normal
  - `Abnorml`: Venta anormal
  - `Partial`: Venta parcial
  - `AdjLand`: Terreno ajustado
  - `Alloca`: Alocado
  - `Family`: Venta familiar


