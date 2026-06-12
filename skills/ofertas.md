# Skill: Ofertas — Creación de ofertas viables y atractivas

## Propósito

Una oferta bien diseñada puede multiplicar las ventas de una campaña.
Una oferta mal diseñada puede hundir el margen del negocio. La diferencia
está en dos cosas: que sea financieramente viable Y que sea atractiva
para el público. Ambas condiciones son obligatorias — no una u otra.

**Regla de oro:** nunca crees una oferta sin saber el margen. Una oferta
que no deja margen es peor que no tener oferta.

---

## El análisis financiero obligatorio

Antes de proponer cualquier oferta, ejecuta este análisis sin excepción:

### Paso 1: Costo de producción real
Consulta el CRM para obtener el costo de producción del producto:
- Qué materias primas lleva la receta
- Cuánto cuesta cada una por unidad producida
- Costo total de producción = suma de (cantidad × precio) de cada insumo

### Paso 2: Margen actual
```
Margen actual = precio de venta - costo de producción
Margen % = (margen actual / precio de venta) × 100
```

### Paso 3: Margen mínimo aceptable
Del Excel financiero del negocio, obtén el margen mínimo aceptable.
Si no está disponible, usa como referencia conservadora: mínimo 35% de
margen después del descuento para cubrir costos operativos y dejar ganancia.

### Paso 4: Descuento máximo posible
```
Descuento máximo = precio de venta - (costo de producción / (1 - margen_mínimo))
Descuento máximo % = (descuento máximo / precio de venta) × 100
```

### Paso 5: Decisión
- Si el descuento propuesto ≤ descuento máximo → la oferta es viable
- Si el descuento propuesto > descuento máximo → la oferta destruye el margen

**Si el margen no da:**
No rechaces la campaña — propón una alternativa viable. Hay tipos de oferta
que no requieren descuento directo y son igual de atractivas.

---

## Cómo derivar la oferta del contexto

La oferta no se escoge de una lista — se diseña a partir de lo que el
recon encontró. El proceso es:

### 1. Lee el contexto completo antes de proponer nada

Del recon extrae:
- ¿Qué está motivando al consumidor ahora? (tendencias, eventos, temporada)
- ¿Qué tipo de propuesta está resonando en redes esta semana?
- ¿Qué está haciendo la competencia que Artilex puede hacer diferente?
- ¿Qué dice la memoria sobre qué ha funcionado con este público?
- ¿Qué productos tienen margen para jugar y cuáles no?

Del negocio extrae:
- ¿Hay stock que convenga mover?
- ¿Hay un producto nuevo o con poca visibilidad?
- ¿Hay una fecha o evento próximo que sea relevante?

### 2. Deja que el contexto sugiera la oferta

No pienses en "qué tipo de oferta hago" — piensa en "dado todo lo que
encontré, ¿qué propuesta tiene más sentido para este momento específico?"

Algunas preguntas que guían esa reflexión:
- ¿El consumidor está en modo regalo o en modo personal?
- ¿Está buscando explorar fragancias nuevas o tiene una clara en mente?
- ¿Qué emoción predomina en las tendencias de esta semana?
- ¿La competencia está siendo agresiva en precio? Si sí, ¿cómo diferencia Artilex?
- ¿Qué formato de oferta encaja con el tono de la campaña que la estrategia definió?

### 3. Diseña la oferta desde cero para este contexto

La oferta resultante puede ser cualquier cosa — no está limitada a formatos
predeterminados. Puede ser algo que nadie ha hecho antes si el contexto
lo sugiere. Lo que importa es que:

- Tenga sentido para el momento (el recon lo justifica)
- Sea financieramente viable (el margen lo permite)
- Encaje con el tono y la estrategia de la campaña
- Tenga un gancho de urgencia claro
- Hable el lenguaje de Artilex Parfum

### 4. Evalúa antes de proponer

Antes de llevar la oferta al usuario, evalúa:
- ¿Esta oferta sorprende o es predecible?
- ¿El cliente entiende inmediatamente qué gana?
- ¿El margen da? (el cálculo del paso anterior lo confirma)
- ¿Podría funcionar en este contexto específico o es genérica?

Si la oferta que diseñaste podría ser de cualquier perfumería, vuelve al
contexto y encuentra el ángulo específico de Artilex.

---

## Cómo hacer que una oferta sea atractiva

El margen dice si la oferta ES viable. La creatividad dice si la oferta
VENDE. Una oferta viable pero aburrida no convierte.

### El gancho de urgencia
Toda oferta necesita una razón para actuar ahora:
- **Tiempo limitado:** "Solo este fin de semana", "Hasta el domingo"
- **Stock limitado:** "Últimas 15 unidades", "Solo para los primeros 20"
- **Ocasión especial:** "Por el día del padre", "Inicio de temporada"
- **Exclusividad:** "Solo para seguidores", "Acceso anticipado"

Sin urgencia, el cliente dice "lo pienso" y nunca compra.

### El lenguaje de la oferta para inspiraciones
Recuerda que Artilex vende inspiraciones — el lenguaje de la oferta
debe reforzar la propuesta de valor:
- NO: "Copia del Sauvage a mitad de precio"
- SÍ: "La fragancia que todos reconocen, al precio que mereces"
- NO: "Perfume barato de imitación"
- SÍ: "Lujo real, sin pagar el nombre de la etiqueta"

La oferta comunica valor, no descuento. El descuento es el mecanismo;
el valor es el mensaje.

### Conectar la oferta con la tendencia del recon
La mejor oferta no vive sola — está conectada con algo que está pasando:
- Una tendencia de fragancia que el recon identificó
- Una fecha o evento que se aproxima
- Algo que está haciendo viral la competencia que Artilex puede capitalizar

Una oferta conectada con el contexto actual convierte más que una oferta
flotando en el vacío.

---

## Consulta de memoria para ofertas

Antes de proponer una oferta, consulta qué dice la memoria:
- ¿Qué tipos de oferta han funcionado mejor en Artilex?
- ¿Qué descuentos han convertido vs cuáles han pasado desapercibidos?
- ¿Qué ganchos de urgencia han funcionado mejor con el público de Artilex?
- ¿Hay algún tipo de oferta que definitivamente no funciona?

Usa esa información para proponer una oferta que tenga más probabilidad
de funcionar, no solo una que sea financieramente viable.

---

## Cómo crear la oferta en el CRM

Una vez que la oferta está aprobada por el usuario:
1. Corre `tools/crm/crear_oferta.py` con:
   - Título: corto y atractivo
   - Descripción: el copy de la oferta con el gancho de urgencia
   - Producto: el ID del producto en el CRM
   - Fecha inicio y fin: el período de vigencia
   - Margen calculado: para referencia interna

2. Confirma que la oferta quedó activa en el CRM.
3. El agente de ventas la consultará automáticamente con `/ofertas/activas`.

---

## Señales de una buena oferta vs una mala

**Buena oferta:**
- El margen está calculado y es viable
- Tiene un gancho de urgencia claro
- El lenguaje refuerza la propuesta de valor de Artilex
- Está conectada con una tendencia o evento del recon
- Al leerla, el cliente entiende inmediatamente qué gana

**Mala oferta (evitar):**
- Descuento sin calcular el margen
- "Gran descuento en perfumes" sin especificidad
- Sin fecha de vencimiento ni urgencia
- Lenguaje que suena a barato o de baja calidad
- Desconectada del contexto de la campaña

---

## Checklist antes de crear la oferta

- [ ] ¿Calculé el costo de producción desde el CRM?
- [ ] ¿El margen después del descuento es ≥ al mínimo aceptable?
- [ ] ¿Tiene un gancho de urgencia claro?
- [ ] ¿El lenguaje refuerza la propuesta de valor de Artilex?
- [ ] ¿Está conectada con el recon (tendencia o evento)?
- [ ] ¿Consulté la memoria sobre qué tipos de oferta han funcionado?
- [ ] ¿El usuario la aprobó antes de crearla en el CRM?