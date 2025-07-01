"""
Sistema BSC Simplificado para Auditoría de Recibos
Versión funcional y completa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import json

# Configuración
plt.style.use('default')
np.random.seed(42)

def generar_datos_auditoria(n_recibos=1000):
    """Genera datos sintéticos para auditoría de recibos"""
    
    # Generar fechas de los últimos 6 meses
    fecha_inicio = datetime.now() - timedelta(days=180)
    fechas = [fecha_inicio + timedelta(days=x) for x in range(180)]
    
    datos = []
    
    for i in range(n_recibos):
        # Datos básicos
        recibo_id = f"REC-{i+1:06d}"
        fecha = np.random.choice(fechas)
        tipo_recibo = np.random.choice(['Simple', 'Complejo', 'Muy Complejo'], p=[0.6, 0.3, 0.1])
        
        # Monto según complejidad
        if tipo_recibo == 'Simple':
            monto = np.random.normal(100, 30)
        elif tipo_recibo == 'Complejo':
            monto = np.random.normal(500, 150)
        else:
            monto = np.random.normal(2000, 500)
        monto = max(10, monto)
        
        # Auditor
        auditor = np.random.choice(['Ana García', 'Carlos López', 'María Rodríguez', 'Juan Pérez', 'Laura Martín'])
        
        # Tiempo de auditoría
        if tipo_recibo == 'Simple':
            tiempo = np.random.normal(12, 3)
        elif tipo_recibo == 'Complejo':
            tiempo = np.random.normal(24, 6)
        else:
            tiempo = np.random.normal(48, 12)
        tiempo = max(1, tiempo)
        
        # Estado y errores
        estado = np.random.choice(['Aprobado', 'Rechazado', 'Pendiente'], p=[0.75, 0.15, 0.10])
        
        if estado == 'Aprobado':
            errores = np.random.poisson(0.5)
            satisfaccion = np.random.normal(4.2, 0.5)
        elif estado == 'Rechazado':
            errores = np.random.poisson(3)
            satisfaccion = np.random.normal(2.8, 0.7)
        else:
            errores = np.random.poisson(1)
            satisfaccion = np.random.normal(3.5, 0.6)
        
        satisfaccion = np.clip(satisfaccion, 1, 5)
        
        # Costo
        costo_base = 10 if tipo_recibo == 'Simple' else 20 if tipo_recibo == 'Complejo' else 40
        costo = costo_base + np.random.normal(0, 2)
        costo = max(5, costo)
        
        # Automatización
        automatizacion = np.random.choice([True, False], p=[0.65, 0.35])
        
        datos.append({
            'recibo_id': recibo_id,
            'fecha': fecha.strftime('%Y-%m-%d'),
            'tipo_recibo': tipo_recibo,
            'monto': round(monto, 2),
            'auditor': auditor,
            'tiempo_auditoria_horas': round(tiempo, 1),
            'estado': estado,
            'errores_encontrados': errores,
            'satisfaccion_cliente': round(satisfaccion, 1),
            'costo_auditoria': round(costo, 2),
            'automatizacion_usada': automatizacion
        })
    
    return pd.DataFrame(datos)

def calcular_kpis_bsc(df):
    """Calcula todos los KPIs del BSC"""
    
    kpis = {}
    
    # PERSPECTIVA FINANCIERA
    kpis['financiera'] = {
        'costo_promedio_recibo': df['costo_auditoria'].mean(),
        'costo_total': df['costo_auditoria'].sum(),
        'valor_detectado': df[df['errores_encontrados'] > 0]['monto'].sum(),
        'roi_auditoria': (df[df['errores_encontrados'] > 0]['monto'].sum() / df['costo_auditoria'].sum()) if df['costo_auditoria'].sum() > 0 else 0,
        'ahorro_automatizacion': df[df['automatizacion_usada'] == False]['costo_auditoria'].mean() - df[df['automatizacion_usada'] == True]['costo_auditoria'].mean()
    }
    
    # PERSPECTIVA DEL CLIENTE
    kpis['cliente'] = {
        'satisfaccion_promedio': df['satisfaccion_cliente'].mean() / 5,  # Normalizar a 0-1
        'tasa_aprobacion': len(df[df['estado'] == 'Aprobado']) / len(df),
        'tiempo_promedio_horas': df['tiempo_auditoria_horas'].mean(),
        'tasa_reclamaciones': len(df[df['estado'] == 'Rechazado']) / len(df),
        'clientes_satisfechos': len(df[df['satisfaccion_cliente'] >= 4]) / len(df)
    }
    
    # PERSPECTIVA DE PROCESOS INTERNOS
    total_auditados = len(df[df['estado'] != 'Pendiente'])
    errores_proceso = len(df[(df['estado'] == 'Aprobado') & (df['errores_encontrados'] > 2)])
    
    kpis['procesos'] = {
        'precision_auditoria': 1 - (errores_proceso / total_auditados) if total_auditados > 0 else 0,
        'tasa_automatizacion': len(df[df['automatizacion_usada'] == True]) / len(df),
        'tasa_deteccion_errores': len(df[df['errores_encontrados'] > 0]) / len(df),
        'eficiencia_promedio': len(df) / df['tiempo_auditoria_horas'].sum(),  # recibos por hora total
        'calidad_proceso': len(df[df['errores_encontrados'] <= 1]) / len(df)
    }
    
    # PERSPECTIVA DE APRENDIZAJE Y CRECIMIENTO
    kpis['aprendizaje'] = {
        'auditores_activos': len(df['auditor'].unique()),
        'diversidad_tipos': len(df['tipo_recibo'].unique()) / 3,  # Normalizado
        'competencia_promedio': df.groupby('auditor')['satisfaccion_cliente'].mean().mean() / 5,
        'mejora_automatizacion': 0.05,  # Simulado - mejora mensual
        'capacitacion_efectividad': 0.85  # Simulado
    }
    
    return kpis

def crear_dashboard_matplotlib(df, kpis):
    """Crea dashboard usando matplotlib"""
    
    fig, axes = plt.subplots(2, 4, figsize=(20, 12))
    fig.suptitle('BALANCED SCORECARD - AUDITORÍA DE RECIBOS', fontsize=20, fontweight='bold', y=0.95)
    
    # Colores para cada perspectiva
    colors = {
        'financiera': '#1f77b4',
        'cliente': '#2ca02c', 
        'procesos': '#ff7f0e',
        'aprendizaje': '#9467bd'
    }
    
    # FILA 1: PERSPECTIVA FINANCIERA Y CLIENTE
    
    # 1. Costo promedio por recibo (Financiera)
    ax1 = axes[0, 0]
    costo_actual = kpis['financiera']['costo_promedio_recibo']
    meta_costo = 15.0
    
    bars = ax1.bar(['Actual', 'Meta'], [costo_actual, meta_costo], 
                   color=[colors['financiera'], 'lightgray'], alpha=0.8)
    ax1.set_title('Costo Promedio por Recibo\n(Perspectiva Financiera)', fontweight='bold')
    ax1.set_ylabel('USD')
    
    # Añadir valores en las barras
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'${height:.2f}', ha='center', va='bottom', fontweight='bold')
    
    # 2. ROI de Auditoría (Financiera)
    ax2 = axes[0, 1]
    roi = kpis['financiera']['roi_auditoria']
    
    wedges, texts, autotexts = ax2.pie([roi, max(0, 20-roi)], 
                                       labels=['ROI Actual', 'Potencial'], 
                                       colors=[colors['financiera'], 'lightgray'],
                                       autopct='%1.1f', startangle=90)
    ax2.set_title('ROI de Auditoría\n(Perspectiva Financiera)', fontweight='bold')
    
    # 3. Satisfacción del Cliente
    ax3 = axes[0, 2]
    satisfaccion = kpis['cliente']['satisfaccion_promedio']
    meta_satisfaccion = 0.9
    
    # Gráfico de gauge simulado
    angles = np.linspace(0, np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)
    
    ax3.plot(x, y, 'k-', linewidth=3)
    ax3.fill_between(x[:int(satisfaccion*100)], 0, y[:int(satisfaccion*100)], 
                     color=colors['cliente'], alpha=0.7)
    ax3.set_xlim(-1.2, 1.2)
    ax3.set_ylim(-0.2, 1.2)
    ax3.set_aspect('equal')
    ax3.axis('off')
    ax3.set_title('Satisfacción del Cliente\n(Perspectiva Cliente)', fontweight='bold')
    ax3.text(0, -0.1, f'{satisfaccion:.1%}', ha='center', va='center', 
             fontsize=16, fontweight='bold')
    
    # 4. Tiempo promedio de auditoría
    ax4 = axes[0, 3]
    tiempo_actual = kpis['cliente']['tiempo_promedio_horas']
    meta_tiempo = 24
    
    bars = ax4.bar(['Actual', 'Meta'], [tiempo_actual, meta_tiempo], 
                   color=[colors['cliente'], 'lightgray'], alpha=0.8)
    ax4.set_title('Tiempo Promedio Auditoría\n(Perspectiva Cliente)', fontweight='bold')
    ax4.set_ylabel('Horas')
    
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}h', ha='center', va='bottom', fontweight='bold')
    
    # FILA 2: PERSPECTIVA PROCESOS Y APRENDIZAJE
    
    # 5. Precisión de Auditoría (Procesos)
    ax5 = axes[1, 0]
    precision = kpis['procesos']['precision_auditoria']
    meta_precision = 0.95
    
    # Gráfico de gauge
    angles = np.linspace(0, np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)
    
    ax5.plot(x, y, 'k-', linewidth=3)
    ax5.fill_between(x[:int(precision*100)], 0, y[:int(precision*100)], 
                     color=colors['procesos'], alpha=0.7)
    ax5.set_xlim(-1.2, 1.2)
    ax5.set_ylim(-0.2, 1.2)
    ax5.set_aspect('equal')
    ax5.axis('off')
    ax5.set_title('Precisión de Auditoría\n(Perspectiva Procesos)', fontweight='bold')
    ax5.text(0, -0.1, f'{precision:.1%}', ha='center', va='center', 
             fontsize=16, fontweight='bold')
    
    # 6. Tasa de Automatización (Procesos)
    ax6 = axes[1, 1]
    automatizacion = kpis['procesos']['tasa_automatizacion']
    meta_automatizacion = 0.7
    
    bars = ax6.bar(['Actual', 'Meta'], [automatizacion, meta_automatizacion], 
                   color=[colors['procesos'], 'lightgray'], alpha=0.8)
    ax6.set_title('Tasa de Automatización\n(Perspectiva Procesos)', fontweight='bold')
    ax6.set_ylabel('Porcentaje')
    ax6.set_ylim(0, 1)
    
    for bar in bars:
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                f'{height:.1%}', ha='center', va='bottom', fontweight='bold')
    
    # 7. Competencia Promedio (Aprendizaje)
    ax7 = axes[1, 2]
    competencia = kpis['aprendizaje']['competencia_promedio']
    meta_competencia = 0.8
    
    # Gráfico de gauge
    angles = np.linspace(0, np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)
    
    ax7.plot(x, y, 'k-', linewidth=3)
    ax7.fill_between(x[:int(competencia*100)], 0, y[:int(competencia*100)], 
                     color=colors['aprendizaje'], alpha=0.7)
    ax7.set_xlim(-1.2, 1.2)
    ax7.set_ylim(-0.2, 1.2)
    ax7.set_aspect('equal')
    ax7.axis('off')
    ax7.set_title('Competencia Promedio\n(Perspectiva Aprendizaje)', fontweight='bold')
    ax7.text(0, -0.1, f'{competencia:.1%}', ha='center', va='center', 
             fontsize=16, fontweight='bold')
    
    # 8. Auditores Activos (Aprendizaje)
    ax8 = axes[1, 3]
    auditores = kpis['aprendizaje']['auditores_activos']
    
    # Gráfico de barras por auditor
    productividad_auditor = df.groupby('auditor').size()
    
    bars = ax8.bar(range(len(productividad_auditor)), productividad_auditor.values, 
                   color=colors['aprendizaje'], alpha=0.8)
    ax8.set_title('Productividad por Auditor\n(Perspectiva Aprendizaje)', fontweight='bold')
    ax8.set_ylabel('Recibos Auditados')
    ax8.set_xticks(range(len(productividad_auditor)))
    ax8.set_xticklabels([name.split()[0] for name in productividad_auditor.index], rotation=45)
    
    plt.tight_layout()
    plt.savefig('./dashboard_bsc_matplotlib.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("✅ Dashboard guardado como 'dashboard_bsc_matplotlib.png'")

def generar_reporte_ejecutivo(kpis):
    """Genera reporte ejecutivo en texto"""
    
    reporte = """
    ═══════════════════════════════════════════════════════════════
                    BALANCED SCORECARD - AUDITORÍA DE RECIBOS
                              REPORTE EJECUTIVO
    ═══════════════════════════════════════════════════════════════
    
    🏦 PERSPECTIVA FINANCIERA
    ────────────────────────────────────────────────────────────────
    • Costo promedio por recibo: ${:.2f} USD
    • ROI de auditoría: {:.2f}x
    • Valor total detectado: ${:,.2f} USD
    • Ahorro por automatización: ${:.2f} USD
    
    👥 PERSPECTIVA DEL CLIENTE  
    ────────────────────────────────────────────────────────────────
    • Satisfacción promedio: {:.1%}
    • Tasa de aprobación: {:.1%}
    • Tiempo promedio de auditoría: {:.1f} horas
    • Tasa de reclamaciones: {:.1%}
    
    ⚙️ PERSPECTIVA DE PROCESOS INTERNOS
    ────────────────────────────────────────────────────────────────
    • Precisión de auditoría: {:.1%}
    • Tasa de automatización: {:.1%}
    • Tasa de detección de errores: {:.1%}
    • Eficiencia promedio: {:.3f} recibos/hora
    
    🎓 PERSPECTIVA DE APRENDIZAJE Y CRECIMIENTO
    ────────────────────────────────────────────────────────────────
    • Auditores activos: {} personas
    • Competencia promedio: {:.1%}
    • Diversidad de tipos manejados: {:.1%}
    • Efectividad de capacitación: {:.1%}
    
    📊 EVALUACIÓN GENERAL
    ────────────────────────────────────────────────────────────────
    """.format(
        kpis['financiera']['costo_promedio_recibo'],
        kpis['financiera']['roi_auditoria'],
        kpis['financiera']['valor_detectado'],
        kpis['financiera']['ahorro_automatizacion'],
        kpis['cliente']['satisfaccion_promedio'],
        kpis['cliente']['tasa_aprobacion'],
        kpis['cliente']['tiempo_promedio_horas'],
        kpis['cliente']['tasa_reclamaciones'],
        kpis['procesos']['precision_auditoria'],
        kpis['procesos']['tasa_automatizacion'],
        kpis['procesos']['tasa_deteccion_errores'],
        kpis['procesos']['eficiencia_promedio'],
        kpis['aprendizaje']['auditores_activos'],
        kpis['aprendizaje']['competencia_promedio'],
        kpis['aprendizaje']['diversidad_tipos'],
        kpis['aprendizaje']['capacitacion_efectividad']
    )
    
    # Evaluación de cumplimiento
    metas = {
        'costo_ok': kpis['financiera']['costo_promedio_recibo'] <= 15.0,
        'satisfaccion_ok': kpis['cliente']['satisfaccion_promedio'] >= 0.9,
        'tiempo_ok': kpis['cliente']['tiempo_promedio_horas'] <= 24,
        'precision_ok': kpis['procesos']['precision_auditoria'] >= 0.95,
        'automatizacion_ok': kpis['procesos']['tasa_automatizacion'] >= 0.7,
        'competencia_ok': kpis['aprendizaje']['competencia_promedio'] >= 0.8
    }
    
    cumplimiento = sum(metas.values()) / len(metas) * 100
    
    if cumplimiento >= 80:
        estado = "🟢 EXCELENTE"
    elif cumplimiento >= 60:
        estado = "🟡 BUENO"
    else:
        estado = "🔴 REQUIERE ATENCIÓN"
    
    reporte += f"""
    Cumplimiento general de metas: {cumplimiento:.1f}%
    Estado del sistema: {estado}
    
    RECOMENDACIONES:
    """
    
    if not metas['costo_ok']:
        reporte += "\n    • Optimizar costos de auditoría mediante mayor automatización"
    if not metas['satisfaccion_ok']:
        reporte += "\n    • Mejorar comunicación y tiempos de respuesta al cliente"
    if not metas['precision_ok']:
        reporte += "\n    • Reforzar capacitación en procesos de auditoría"
    if not metas['automatizacion_ok']:
        reporte += "\n    • Acelerar adopción de herramientas automatizadas"
    
    reporte += "\n\n    ═══════════════════════════════════════════════════════════════\n"
    
    return reporte

def main():
    """Función principal"""
    print("🚀 Iniciando Sistema BSC para Auditoría de Recibos")
    print("📊 Generando datos sintéticos...")
    
    # Generar datos
    df = generar_datos_auditoria(1000)
    print(f"✅ Generados {len(df)} registros de auditoría")
    
    # Guardar datos
    df.to_csv('./datos_auditoria_recibos.csv', index=False)
    print("✅ Datos guardados como CSV")
    
    # Calcular KPIs
    print("🔢 Calculando KPIs del BSC...")
    kpis = calcular_kpis_bsc(df)
    
    # Guardar KPIs
    with open('./kpis_bsc.json', 'w') as f:
        # Convertir numpy types a tipos nativos de Python para JSON
        kpis_json = {}
        for perspectiva, valores in kpis.items():
            kpis_json[perspectiva] = {}
            for kpi, valor in valores.items():
                if isinstance(valor, (np.integer, np.floating)):
                    kpis_json[perspectiva][kpi] = float(valor)
                else:
                    kpis_json[perspectiva][kpi] = valor
        json.dump(kpis_json, f, indent=2)
    print("✅ KPIs guardados como JSON")
    
    # Crear dashboard
    print("📈 Creando dashboard visual...")
    crear_dashboard_matplotlib(df, kpis)
    
    # Generar reporte
    print("📋 Generando reporte ejecutivo...")
    reporte = generar_reporte_ejecutivo(kpis)
    
    with open('./reporte_ejecutivo_bsc.txt', 'w', encoding='utf-8') as f:
        f.write(reporte)
    print("✅ Reporte guardado como TXT")
    
    # Mostrar reporte en consola
    print(reporte)
    
    return df, kpis

if __name__ == "__main__":
    df, kpis = main()

