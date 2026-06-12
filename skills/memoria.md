# Skill: Memoria — Consulta y actualización del conocimiento acumulado

## Propósito

La memoria es lo que convierte a LixMarkt de un agente que empieza desde
cero cada vez en un agente que mejora con cada campaña. Sin memoria, cada
campaña es igual de buena o mala que la primera. Con memoria bien usada,
cada campaña parte de todo lo que se aprendió antes.

**La memoria tiene tres capas distintas y cada una sirve para algo diferente:**
1. **Patrones propios:** lo que ha funcionado y lo que no en las campañas
   de Artilex Parfum. Es el conocimiento más valioso porque es específico
   a este negocio y este público.
2. **Estrategias externas:** conocimiento de marketing de la industria,
   procesado y filtrado para ser relevante para Artilex. Es el marco de
   referencia, no la receta.
3. **Métricas históricas:** el registro acumulativo de resultados de cada
   campaña, con contexto suficiente para ser consultable y útil.

**Hay también un cuarto archivo fundamental:**
4. **Perfil de identidad** (`memoria/identidad/artilex_parfum.md`): quién
   es Artilex visualmente y en tono. No es memoria de campañas — es la
   base sobre la que todo lo demás se construye.

---

## Cuándo consultar la memoria

La memoria se consulta en momentos específicos del flujo, no de forma
genérica. Cada consulta tiene un propósito concreto:

### En el /recon
**Qué buscar:** patrones de campañas anteriores que sean relevantes para
el tipo de campaña que se va a hacer. Tendencias que resultaron pasajeras
vs las que se sostuvieron. Errores documentados que no hay que repetir.
**Para qué:** no empezar desde cero. El recon se enriquece con lo que
ya se sabe, no lo reemplaza.

### En el /strategy
**Qué buscar:** qué formatos han funcionado mejor para este tipo de producto
o público. Qué tono ha generado más engagement. Qué días y horas han
funcionado mejor históricamente. Qué tipos de oferta han convertido.
**Para qué:** tomar decisiones estratégicas informadas, no arbitrarias.

### En el /create
**Qué buscar:** qué estilos visuales han resonado con el público de Artilex.
Qué prompts de imagen han producido resultados mejores. Qué copys o
estructuras de copy han funcionado bien.
**Para qué:** construir sobre lo que funciona, no reinventar cada vez.

### En el /review
**Qué buscar:** campañas anteriores similares para comparar los resultados.
**Para qué:** contextualizar si los resultados de esta campaña son buenos,
malos o normales para Artilex.

---

## Cómo consultar la memoria correctamente

La consulta de memoria no es "leer todo lo que hay" — es buscar lo
que es relevante para la tarea actual.

**Preguntas que guían la consulta:**

Para el recon:
- ¿Qué hemos aprendido sobre campañas de [tipo de producto] antes?
- ¿Hay patrones sobre qué funciona cuando [contexto actual: temporada,
  evento, tendencia]?
- ¿Qué errores están documentados que debería evitar?

Para la estrategia:
- ¿Qué formato ha tenido mejor desempeño para [tipo de campaña]?
- ¿Qué tono ha funcionado mejor con el público de Artilex?
- ¿Qué tipo de oferta ha convertido mejor y en qué contexto?

Para el contenido:
- ¿Qué estilo visual ha generado más engagement?
- ¿Hay prompts de imagen que hayan funcionado excepcionalmente bien?
- ¿Qué estructura de copy ha resonado más?

**Lo que NO es consultar la memoria:**
- Leer los archivos sin buscar algo específico
- Usar los patrones como plantillas a copiar
- Ignorar el contexto actual por seguir lo que funcionó antes

La memoria informa — no dicta. Si el recon muestra que el contexto
actual es muy diferente a campañas anteriores, el contexto actual
pesa más que los patrones históricos.

---

## Cómo actualizar la memoria

La memoria se actualiza en momentos específicos:

### Después de cada campaña (/save)
El `/save` es el momento de actualizar la memoria con lo aprendido.
Lo que se guarda:
- En `memoria/patrones/patrones.json`: el patrón estructurado de la
  campaña (qué se hizo, por qué se eligió, qué resultado tuvo)
- En `memoria/metricas/historico_metricas.json`: las métricas con contexto

**Cómo guardar un patrón útil:**
Un patrón útil no es un resumen — es un registro con suficiente detalle
para ser consultable y accionable. Incluye:
- El contexto en que se tomó cada decisión (qué del recon lo motivó)
- El resultado específico (no "funcionó bien" sino el número y qué lo explica)
- La condición bajo la cual aplica (no es universal — es "cuando X, funciona Y")
- Lo que no funcionó y por qué

**Ejemplo de patrón mal guardado:**
"El carrusel tuvo buen engagement. Usar carruseles en el futuro."

**Ejemplo de patrón bien guardado:**
"Carrusel de 5 slides con estilo sensorial (mármol, iluminación cálida,
vapor) para el Invictus tuvo engagement rate de 8.3% (3x el promedio de
Artilex). Contexto: se publicó el viernes 6pm durante tendencia de 'quiet
luxury' en TikTok. El copy usó tono íntimo ('el aroma que define cómo
te recuerdan'). Probable causa: combinación de tendencia activa + estilo
visual que conecta con esa tendencia + copy emocional. Aplica cuando:
hay tendencia estética activa que conecte con fragancias. No aplica para
campañas de conversión directa donde el copy informativo funciona mejor."

### Con estrategias externas (/learn)
Cuando se agrega conocimiento externo, se guarda procesado — no copiado.
Lo que se guarda en `memoria/estrategias/`:
- El principio extraído (no la táctica superficial)
- Por qué es relevante para Artilex específicamente
- En qué contexto aplica y en cuál no
- Cómo se diferencia de lo que Artilex ya hace

### Con el perfil de identidad (/identity)
Cuando se actualiza la identidad con nuevos materiales, el archivo
`memoria/identidad/artilex_parfum.md` se actualiza sin borrar lo anterior —
la identidad evoluciona, no se reemplaza. Se anota qué cambió y cuándo.

---

## Cómo crece la memoria con el tiempo

La primera campaña tiene poca memoria para consultar — es normal.
El agente trabaja más desde las estrategias externas y el recon.

Con cada campaña guardada, la memoria propia crece y se vuelve más
valiosa que el conocimiento externo, porque es específica a Artilex
y a su público real.

Después de 5-10 campañas, LixMarkt tiene suficiente contexto propio
para hacer recomendaciones muy específicas: "para un producto como este,
con este tipo de público, en este tipo de temporada, lo que ha funcionado
mejor es..." — ese nivel de especificidad no viene de ningún libro de
marketing ni de ninguna estrategia externa. Solo viene de la experiencia
acumulada de este negocio.

**Por eso el /save no es opcional.** Si no guardas, no aprendes. Si no
aprendes, la próxima campaña empieza desde el mismo punto que esta.

---

## Estructura de archivos de memoria

```
memoria/
├── identidad/
│   └── artilex_parfum.md          ← perfil de marca (base de todo)
│
├── patrones/
│   └── patrones.json              ← patrones propios acumulativos
│
├── metricas/
│   └── historico_metricas.json    ← historial de métricas acumulativo
│
├── estrategias/                   ← conocimiento externo procesado
│   └── [archivos .md por tema]
│
└── campanas/                      ← archivo completo por campaña
    └── [año]/[mes]/[nombre]/
        ├── recon.md
        ├── strategy.md
        ├── contenido.md
        ├── imagenes/
        ├── plan.md
        ├── metricas.md
        └── patron.md
```

**Regla de mantenimiento:** los archivos acumulativos (patrones.json,
historico_metricas.json) nunca se borran ni se reemplazan — solo se
agregan entradas nuevas. La historia completa siempre está disponible.

---

## Señales de memoria bien usada vs mal usada

**Memoria bien usada:**
- El recon referencia aprendizajes específicos de campañas anteriores
- La estrategia justifica sus decisiones con patrones históricos
- El contenido construye sobre lo que ha funcionado, no lo repite
- El /save guarda patrones con suficiente contexto para ser útiles meses después
- Con cada campaña, las recomendaciones son más específicas y acertadas

**Memoria mal usada (evitar):**
- Consultar la memoria sin buscar algo específico
- Usar los patrones como plantillas fijas
- Guardar patrones sin contexto ("el carrusel funcionó bien")
- No ejecutar /save por "no tener tiempo"
- Ignorar los patrones cuando el recon actual contradice la memoria
  (el contexto actual siempre pesa más que el histórico)