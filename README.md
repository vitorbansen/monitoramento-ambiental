## Casos de Uso

1. **Monitorar Temperatura**
   - **Descrição:** O sistema deve coletar e exibir a temperatura atual do ambiente. Os dados serão capturados por um sensor de temperatura conectado ao Arduino e enviados para a plataforma de nuvem.
   - **Ator Primário:** Usuário
   - **Pré-condições:** O sensor deve estar instalado e configurado corretamente. O Arduino deve estar conectado à internet.
   - **Fluxo Principal:**
     1. O sensor mede a temperatura ambiente.
     2. O Arduino envia os dados para a plataforma de nuvem.
     3. O sistema exibe a temperatura atual em um painel de controle.
   - **Pós-condições:** A temperatura atual é armazenada e atualizada em tempo real.

2. **Monitorar Umidade**
   - **Descrição:** O sistema deve coletar e exibir os níveis de umidade do ambiente. Os dados são capturados por um sensor de umidade e enviados para a nuvem.
   - **Ator Primário:** Usuário
   - **Pré-condições:** O sensor de umidade deve estar instalado e em funcionamento.
   - **Fluxo Principal:**
     1. O sensor mede a umidade do ar.
     2. O Arduino envia os dados para a plataforma de nuvem.
     3. O sistema exibe os níveis de umidade no painel de controle.
   - **Pós-condições:** Os níveis de umidade são atualizados em tempo real.

3. **Exibir Dados em Tempo Real**
   - **Descrição:** O sistema deve apresentar todos os dados coletados (temperatura e umidade) em um painel de controle interativo. Os dados devem ser atualizados automaticamente a cada nova coleta.
   - **Ator Primário:** Usuário
   - **Pré-condições:** Os sensores devem estar ativos e transmitindo dados.
   - **Fluxo Principal:**
     1. O sistema coleta dados dos sensores em intervalos regulares.
     2. Os dados são enviados e armazenados na nuvem.
     3. O painel de controle é atualizado automaticamente para refletir os dados mais recentes.
   - **Pós-condições:** O usuário tem acesso a informações em tempo real sobre as condições ambientais.

## Histórias de Usuário

1. **Visualizar Temperatura em Tempo Real**
   - **História:** Como um usuário, quero visualizar a temperatura em tempo real para monitorar as condições ambientais e tomar decisões informadas sobre a gestão do ambiente.
   - **Critérios de Aceitação:**
     - O sistema deve exibir a temperatura atual em graus Celsius.
     - A temperatura deve ser atualizada a cada 5 segundos.

2. **Visualizar Níveis de Umidade**
   - **História:** Como um usuário, quero visualizar os níveis de umidade em tempo real para entender melhor as condições do ambiente e agir se necessário.
   - **Critérios de Aceitação:**
     - O sistema deve exibir a umidade atual em porcentagem.
     - A umidade deve ser atualizada em tempo real, a cada 5 segundos.

3. **Receber Alertas de Condições Anormais**
   - **História:** Como um usuário, quero receber alertas quando a temperatura ou a umidade excederem limites predefinidos, para poder agir rapidamente e proteger o ambiente.
   - **Critérios de Aceitação:**
     - O sistema deve permitir que o usuário defina limites de temperatura e umidade.
     - O sistema deve enviar uma notificação quando os dados coletados ultrapassarem os limites definidos.
