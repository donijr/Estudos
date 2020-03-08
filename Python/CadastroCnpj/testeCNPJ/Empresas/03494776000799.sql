------------------------------------------
-- Script para Inclusão de Novas Empresas
------------------------------------------
declare
   --
   vn_multorg_id   number;
   vn_pessoa_id    number;
   vn_empresa_id   number;
   --
begin
   --
   -- Recuperação do registro da Mult-Organização
   --
   begin
      select mo.id
        into vn_multorg_id
        from csf_own.mult_org mo
       where mo.cd = '109'; -- cd
   exception
      when others then
         vn_multorg_id := 0;
   end;
   --
   -- Criação do registro Pessoa
   --
   select csf_own.pessoa_seq.nextval
     into vn_pessoa_id
     from dual;
   --
   insert into csf_own.pessoa ( id
                              , dm_tipo_incl
                              , cod_part
                              , nome
                              , dm_tipo_pessoa
                              , fantasia
                              , lograd
                              , nro
                              , cx_postal
                              , compl
                              , bairro
                              , cidade_id
                              , cep
                              , fone
                              , fax
                              , email
                              , pais_id
                              , multorg_id
                              , dm_st_proc
                              )
                       values ( vn_pessoa_id -- id
                              , 0 -- dm_tipo_incl
                              , '03494776000799' -- cod_part
                              , 'AMMO VAREJO LTDA' -- nome
                              , 1 -- dm_tipo_pessoa
                              , 'ARTEX' -- fantasia
                              , 'AVENIDA ARICANDUVA 5555' -- lograd
                              , '5555' -- nro
                              , '' -- cx_postal
                              , ': ARCO N 441;' -- compl
                              , 'JARDIM SANTA TEREZINHA (ZONA LESTE)' -- bairro
                              , (select ci.id from csf_own.cidade ci where ci.descr = 'Sao Paulo') -- cidade_id
                              , 03527900 -- cep 
                              , '1921022200' -- fone
                              , '' -- fax
                              , 'fiscal@ammovarejo.com.br' -- email
                              , (select es.pais_id from csf_own.estado es where es.id = (select ci.estado_id from csf_own.cidade ci where ci.descr = 'Sao Paulo')) -- pais_id
                              , vn_multorg_id -- multorg_id
                              , 1 -- dm_st_proc
                              );
   --
   -- Criação do registro Jurídico
   --
   insert into csf_own.juridica ( id
                                , pessoa_id
                                , num_cnpj
                                , num_filial
                                , dig_cnpj
                                , ie
                                , iest
                                , im
                                , cnae
                                , suframa
                                )
                         values ( csf_own.juridica_seq.nextval -- id
                                , vn_pessoa_id -- pessoa_id
                                , 03494776 -- num_cnpj
                                , 0007 -- num_filial
                                , 99 -- dig_cnpj
                                , '' -- ie
                                , '' -- iest
                                , '' -- im
                                , '' -- cnae
                                , '' -- suframa
                                );
   --
   -- Criação do registro Empresa
   --
   select csf_own.empresa_seq.nextval
     into vn_empresa_id
     from dual;
   --
   insert into csf_own.empresa ( id
                               , pessoa_id
                               , dm_situacao
                               , dm_tp_amb
                               , dm_tp_impr
                               , dm_forma_emiss
                               , dt_ini_integr
                               , default_cons_stat
                               , caminho_chave_jks
                               , senha_chave_jks
                               , caminho_cert_pfx
                               , senha_cert_pfx
                               , nro_tentativas_comunic
                               , max_qtd_nfe_lote
                               , max_qtd_impressao
                               , email_nome
                               , email_ender_remet
                               , email_template_subject
                               , email_template_body
                               , email_template_body_canc
                               , email_body_cobr_xml_terc
                               , nro_tent_com_scan
                               , nro_tent_com_dpec
                               , dir_integra
                               , multorg_id
                               )
                        values ( vn_empresa_id -- id
                               , vn_pessoa_id -- pessoa_id
                               , 1 -- dm_situacao
                               , 2 -- dm_tp_amb
                               , 1 -- dm_tp_impr
                               , 1 -- dm_forma_emiss
                               , sysdate -- dt_ini_integr
                               , 0 -- default_cons_stat
                               , 'certraiz_compliance.jks' -- caminho_chave_jks
                               , 'compliance' -- senha_chave_jks
                               , '' -- caminho_cert_pfx
                               , '' -- senha_cert_pfx
                               , 30 -- nro_tentativas_comunic
                               , 1 -- max_qtd_nfe_lote
                               , 1 -- max_qtd_impressao
                               , 'teste' -- email_nome
                               , 'cliente@compliancefiscal.com.br' -- email_ender_remet
                               , 'Nota Fiscal Eletrônica Nro:#nro_documento#/Série:#serie_documento# emitida por #remetente_nota_fantasia#' -- email_template_subject
                               , '---------------------------------------------------------
                                  -- N A O   R E S P O N D E R   A   E S S E   E M A I L --
                                  ---------------------------------------------------------
                                  Email gerado automaticamente pelo servico: Compliance-Nfe
                                  	         Compliance Solucoes Fiscais
                                          Nfe Segura e com reducao de custos.
                                        www.compliancefiscal.com.br 16.35169600
                                  ---------------------------------------------------------

                                  A(o) #razao_social_destinatario#

                                    As #hora_aprovacao_lote#  foi  aprovada  a emissao  da
                                  seguinte nota fiscal em formato eletronico:

                                  EMITENTE:
                                  =========
                                  Razao Social.: #razao_social_emitente#
                                  CNPJ/CPF.....: #cnpj_emitente#
                                  Telefone.....: #telefone_emitente#

                                  DESTINATARIO
                                  ============
                                  Razao Social.: #razao_social_destinatario#
                                  CNPJ/CPF.....: #cnpj_destinatario#

                                  DETALHES
                                  ========
                                  Chave Acesso.: #nro_chave_acesso#
                                  Documento....: #nro_documento# / Serie: #serie_documento#
                                  Data Emissao.: #data_emissao#
                                  Valor Total..: #valor_total#'
                               , '-- N A O   R E S P O N D E R   A   E S S E   E M A I L --
                                  ---------------------------------------------------------
                                  Email gerado automaticamente pelo servico: Compliance-Nfe
                                  	         Compliance Solucoes Fiscais
                                          Nfe Segura e com reducao de custos.
                                        www.compliancefiscal.com.br 16.35169600
                                  ---------------------------------------------------------
                                  A(o) #razao_social_destinatario#

                                    Cancelamento de Nota Fiscal Eletronica:
                                  EMITENTE:
                                  =========
                                  Razao Social.: #razao_social_emitente#
                                  CNPJ/CPF.....: #cnpj_emitente#
                                  Telefone.....: #telefone_emitente#

                                  DESTINATÁRIO
                                  ============
                                  Razao Social.: #razao_social_destinatario#
                                  CNPJ/CPF.....: #cnpj_destinatario#

                                  DETALHES
                                  ========
                                  Chave Acesso.: #nro_chave_acesso#
                                  Documento....: #nro_documento# / Serie: #serie_documento#
                                  Data Emissao.: #data_emissao#
                                  Valor Total..: #valor_total#'
                               , '--------------------------------------------------------- -- N Ã O   R E S P O N D E R   A   E S S E   E M A I L -- --------------------------------------------------------- Email gerado automaticamente pelo serviço: Compliance-Nfe  À(o) #razao_social_fornecedor#    Solicitamos o envio do XML da NF-e abaixo:  EMITENTE: ========= Razão Social.: #razao_social_fornecedor#  DESTINATÁRIO ============ Razão Social.: #razao_social_empresa# CNPJ/CPF.....: #cnpj_empresa# Telefone.....: #telefone_empresa#  DETALHES ======== Chave Acesso.: #nro_chave_acesso# Documento....: #nro_documento# / Série: #serie_documento#'
                               , 5 -- nro_tent_com_scan
                               , 5 -- nro_tent_com_dpec
                               , '' -- dir_integra /complianceServer/ComplianceFiscal/Integra/03965963000118/
                               , vn_multorg_id -- multorg_id
                               );
   --
   insert into csf_own.usuario_empresa ( id
                                       , usuario_id
                                       , empresa_id
                                       , dm_acesso
                                       , dm_empr_default
                                       )
                                values ( csf_own.usuempr_seq.nextval
                                       , (select usuario_id from mult_org where cd = '109') -- usuario_id
                                       , vn_empresa_id -- empresa_id
                                       , 1 -- dm_acesso
                                       , 0 -- dm_empr_default
                                       );
   --
   -- Criação do registro Valores de Parâmetros - Saída para Impressora com Erro de Validação
   --
   insert into csf_own.csf_param_vl ( id
                                    , csfparametro_id
                                    , id_ref
                                    , seq
                                    , vl
                                    , dm_tp_param
                                    , obj_referen_id
                                    )
                             values ( csf_own.csfparamvl_seq.nextval -- id
                                    , (select cp.id from csf_own.csf_parametro cp where cp.ident_int = 'TIPO_LOG_SAIDA_IMPR') -- csfparametro_id
                                    , vn_empresa_id -- id_ref
                                    , 1 -- seq
                                    , 1 -- vl
                                    , 6 -- dm_tp_param
                                    , (select ct.id from csf_own.csf_tipo_log ct where ct.cd = 'ERRO_VALIDA') -- obj_referen_id
                                    );
   --
   -- Criação do registro Valores de Parâmetros - Saída para Impressora com Erro de Impressão
   --
   insert into csf_own.csf_param_vl ( id
                                    , csfparametro_id
                                    , id_ref
                                    , seq
                                    , vl
                                    , dm_tp_param
                                    , obj_referen_id
                                    )
                             values ( csf_own.csfparamvl_seq.nextval -- id
                                    , (select cp.id from csf_own.csf_parametro cp where cp.ident_int = 'TIPO_LOG_SAIDA_IMPR') -- csfparametro_id
                                    , vn_empresa_id -- id_ref
                                    , 1 -- seq
                                    , 1 -- vl
                                    , 6 -- dm_tp_param
                                    , (select ct.id from csf_own.csf_tipo_log ct where ct.cd = 'ERRO_IMP_ARQ') -- obj_referen_id
                                    );
   --
   --
   -- Efetivar os processos
   --
   commit;
   --
end;
/
