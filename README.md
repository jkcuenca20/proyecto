# proyecto
proyecto
🏗️ Reto Final OpenShift: Sistema de Comentarios (Helm + GitHub Actions, 100% YAML)
🎯 Objetivo
Desplegar en OpenShift un sistema compuesto por frontend, backend-api, backend-data y base de datos, usando Helm y GitHub Actions.
Todo debe ser declarativo (YAML). No se permiten comandos manuales de oc para aplicar recursos.
📦 Requerimientos generales
Todo recurso (Deployments, Services, Routes, PVC, ConfigMaps, Secrets, HPA, NetworkPolicies) debe estar en YAML dentro de un chart de Helm.
El despliegue a OpenShift debe ejecutarse mediante GitHub Actions (CI/CD).
🧩 Componentes y relaciones
frontend → consume backend-api (HTTP).
backend-api → llama a backend-data (HTTP).
backend-data → se conecta a base de datos (TCP).
base de datos con PVC persistente (PostgreSQL o MongoDB).
🔒 NetworkPolicies (obligatorio)
Crear políticas que:
Permitan frontend → backend-api.
Permitan backend-api → backend-data.
Permitan backend-data → database.
Bloqueen todo tráfico no explícitamente permitido (intra-namespace y externo).
Deben usar labels consistentes en los Deployments/Pods para podSelector y from.
 
frontend → consume backend-api (HTTP).
backend-api → llama a backend-data (HTTP).
backend-data → se conecta a base de datos (TCP).
base de datos con PVC persistente (PostgreSQL o MongoDB).

🔒 NetworkPolicies (obligatorio)
Crear políticas que:
Permitan frontend → backend-api.
Permitan backend-api → backend-data.
Permitan backend-data → database.
Bloqueen todo tráfico no explícitamente permitido (intra-namespace y externo).
Deben usar labels consistentes en los Deployments/Pods para podSelector y from.