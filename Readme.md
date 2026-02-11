# Content-Based Recommender System

Sistema de recomendação implícita baseado em similaridade de conteúdo.

### Como Funciona

1. **watch** `/watch` - Registra visualização de vídeo
   - Pondera a duração (máx 60 segundos = peso 1)
   - Atualiza o perfil do usuário

2. **recommend** `/recommend` - Retorna videos ranqueados
   - Calcula similarity usando dot product
   - Ordena por score descendente

### Endpoints

```
POST /watch
{
  "video": "python_basico",
  "seconds": 45
}

GET /recommend
```

### Instalação

```bash
pip install fastapi uvicorn numpy pydantic
```

### Executar

```bash
uvicorn app.main:app --reload
```