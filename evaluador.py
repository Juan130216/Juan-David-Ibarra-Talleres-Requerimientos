import re

# 1. LISTAS DE CONTROL
# Palabras vagas que restan especificidad
PALABRAS_VAGAS = [
    "rápido", "lento", "fácil", "difícil", "bueno", "malo",
    "aceptable", "adecuado", "robusto", "eficiente", "seguro",
    "amigable", "intuitivo", "flexible"
]

# Roles comunes del negocio para evaluar relevancia
ROLES_NEGOCIO = [
    "usuario", "cliente", "administrador", "docente", 
    "estudiante", "coordinador", "sistema", "recepcionista"
]

# Promesas irrealistas para verificar si es alcanzable
TERMINOS_IRREALES = [
    "100%", "nunca fallará", "cero errores", "siempre activo", 
    "infinito", "en 0 segundos", "100 años"
]

# 2. FUNCIONES DE EVALUACIÓN (CRITERIOS SMART-V)
def es_especifico(req: str) -> bool:
    """Específico: no contiene palabras vagas."""
    texto = req.lower()
    encontradas = [p for p in PALABRAS_VAGAS if p in texto]
    return len(encontradas) == 0

def es_medible(req: str) -> bool:
    """Medible: contiene al menos un número o porcentaje."""
    tiene_numero = bool(re.search(r"\d+", req))
    tiene_porcentaje = "%" in req
    return tiene_numero or tiene_porcentaje

def es_alcanzable(req: str) -> bool:
    """Alcanzable: no promete absolutismos ni métricas imposibles."""
    texto = req.lower()
    imposibles = [t for t in TERMINOS_IRREALES if t in texto]
    return len(imposibles) == 0

def es_relevante(req: str) -> bool:
    """Relevante: identifica un actor del negocio o justificación."""
    texto = req.lower()
    menciona_rol = any(rol in texto for rol in ROLES_NEGOCIO)
    menciona_proposito = any(p in texto for p in ["para", "permita", "con el fin de", "solicitado por"])
    return menciona_rol or menciona_proposito

def tiene_id(req: str) -> bool:
    """Identificable: comienza con un ID tipo REQ-001."""
    return bool(re.match(r"^REQ-\d{3}", req.strip()))

def es_verificable(req: str) -> bool:
    """Verificable: menciona una condición o criterio concreto."""
    palabras_clave = [
        "cuando", "si", "debe", "máximo", "mínimo",
        "menos de", "más de", "al menos", "exactamente"
    ]
    texto = req.lower()
    return any(p in texto for p in palabras_clave)

def evaluar_requisito(req: str) -> dict:
    """Evalúa un requisito contra los 6 criterios del modelo SMART-V."""
    resultado = {
        "Texto": req,
        "Específico": es_especifico(req),
        "Medible": es_medible(req),
        "Alcanzable": es_alcanzable(req),
        "Relevante": es_relevante(req),
        "Identificable": tiene_id(req),
        "Verificable": es_verificable(req)
    }
    resultado["Puntaje"] = sum(1 for k, v in resultado.items() if k != "Texto" and v is True)
    return resultado

# 3. MODO INTERACTIVO (EJECUCIÓN)
if __name__ == "__main__":
    print("=== EVALUADOR DE REQUISITOS SMART-V ===")
    print("Escribe 'salir' para terminar.\n")
    
    while True:
        mi_requisito = input("Escribe tu requisito: ")
        
        if mi_requisito.lower().strip() == "salir":
            print("¡Hasta luego!")
            break
            
        if not mi_requisito.strip():
            continue

        evaluacion = evaluar_requisito(mi_requisito)
        
        print("\n--- RESULTADO DE LA EVALUACIÓN ---")
        for criterio, valor in evaluacion.items():
            if criterio != "Texto":
                estado = "✅ Cumple" if valor is True else ("❌ No cumple" if valor is False else valor)
                print(f"  • {criterio}: {estado}")
        
        puntaje = evaluacion["Puntaje"]
        if puntaje == 6:
            print("👉 VEREDICTO: ¡EXCELENTE REQUISITO! (6/6)\n")
        elif puntaje >= 4:
            print(f"👉 VEREDICTO: REQUISITO ACEPTABLE ({puntaje}/6) - Revisa los puntos con ❌.\n")
        else:
            print(f"👉 VEREDICTO: REQUISITO DEFICIENTE ({puntaje}/6) - Debes reestructurarlo.\n")