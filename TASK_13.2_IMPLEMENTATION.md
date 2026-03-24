# Task 13.2: Adicionar Monitoramento de Memória

## Implementação Concluída

### Objetivo
Implementar verificação de uso de memória e log warning se ultrapassar 500MB, conforme requisito 11.3.

### Alterações Realizadas

#### 1. automation_engine.py

**Imports adicionados:**
- `psutil`: Biblioteca para monitoramento de recursos do sistema
- `os`: Para obter o PID do processo

**Modificações na classe `GoogleMapsAutomation`:**

1. **Atributos adicionados no `__init__`:**
   ```python
   self.process = psutil.Process(os.getpid())
   self.memory_threshold_mb = 500  # Limite de 500MB conforme requisito 11.3
   ```

2. **Novo método `verificar_uso_memoria()`:**
   - Obtém informações de memória do processo atual usando `psutil`
   - Converte de bytes para megabytes
   - Registra o uso atual de memória no log
   - Dispara WARNING se ultrapassar 500MB
   - Inclui tratamento de erros

3. **Pontos de verificação adicionados:**
   - **Antes da extração:** Verifica memória antes de iniciar o processamento das empresas
   - **A cada 5 leads:** Verifica memória junto com a atualização de progresso
   - **Ao final da extração:** Verifica memória após conclusão

#### 2. requirements.txt

**Dependência adicionada:**
```
# Monitoramento de sistema
psutil==5.9.6
```

### Comportamento

O sistema agora monitora continuamente o uso de memória durante a extração:

1. **Log de informação:** A cada verificação, registra o uso atual de memória
   ```
   INFO - Uso de memória atual: 45.32 MB
   ```

2. **Log de warning:** Quando ultrapassa 500MB, dispara alerta
   ```
   WARNING - ALERTA: Uso de memória ultrapassou 500MB! Uso atual: 523.45 MB. 
   Considere reduzir o limite de leads ou reiniciar a aplicação.
   ```

### Testes Realizados

#### test_memory_monitoring.py
- Verifica inicialização correta dos atributos
- Testa execução do método `verificar_uso_memoria()`
- Simula aumento de uso de memória
- **Resultado:** ✓ PASSOU

#### test_memory_warning.py
- Reduz temporariamente o limite para 50MB
- Cria dados para ultrapassar o limite
- Verifica se o WARNING é disparado corretamente
- **Resultado:** ✓ PASSOU - WARNING disparado em 99.75 MB (limite de teste: 50MB)

### Conformidade com Requisitos

**Requisito 11.3:** "THE Lead_Extractor SHALL utilizar no máximo 500MB de memória RAM durante operação normal"

✓ **Implementado:**
- Sistema monitora uso de memória em tempo real
- Dispara warning se ultrapassar 500MB
- Permite identificar potenciais vazamentos de memória
- Fornece informações para o usuário tomar ações corretivas

### Benefícios

1. **Detecção precoce:** Identifica problemas de memória antes que causem falhas
2. **Diagnóstico:** Logs detalhados ajudam a identificar quando o uso de memória aumenta
3. **Ação preventiva:** Usuário pode reduzir limite de leads ou reiniciar aplicação
4. **Performance:** Não impacta significativamente a performance (verificações rápidas)

### Notas Técnicas

- **psutil.Process.memory_info().rss:** Usa RSS (Resident Set Size) que representa a memória física real usada
- **Verificações estratégicas:** Monitora a cada 5 leads para balancear precisão e performance
- **Thread-safe:** O método pode ser chamado de forma segura durante a extração assíncrona
