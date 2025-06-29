mongodb_setup = """
// =====================================================
// SCRIPT SETUP - MONGODB
// Database: GasPricesBrazil
// =====================================================

// Conectar ao banco de dados
use GasPricesBrazil;

// Criar coleção de preços de combustíveis com validação
db.createCollection("fuelPrices", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["estado", "regiao", "produto", "data_coleta", "preco_medio_revenda"],
         properties: {
            estado: {
               bsonType: "string",
               description: "Código do estado (2 caracteres) - obrigatório"
            },
            nome_estado: {
               bsonType: "string",
               description: "Nome completo do estado"
            },
            regiao: {
               bsonType: "string",
               enum: ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
               description: "Região do Brasil - obrigatório"
            },
            produto: {
               bsonType: "string",
               enum: ["GASOLINA COMUM", "ETANOL", "DIESEL", "DIESEL S10", "GNV"],
               description: "Tipo de combustível - obrigatório"
            },
            data_coleta: {
               bsonType: "date",
               description: "Data da coleta dos dados - obrigatório"
            },
            ano: {
               bsonType: "int",
               minimum: 2004,
               maximum: 2025,
               description: "Ano da coleta"
            },
            mes: {
               bsonType: "int",
               minimum: 1,
               maximum: 12,
               description: "Mês da coleta"
            },
            preco_medio_revenda: {
               bsonType: "double",
               minimum: 0,
               description: "Preço médio de revenda (R$/litro) - obrigatório"
            },
            preco_medio_distribuicao: {
               bsonType: "double",
               minimum: 0,
               description: "Preço médio de distribuição (R$/litro)"
            },
            desvio_padrao_revenda: {
               bsonType: "double",
               minimum: 0,
               description: "Desvio padrão do preço de revenda"
            },
            desvio_padrao_distribuicao: {
               bsonType: "double",
               minimum: 0,
               description: "Desvio padrão do preço de distribuição"
            },
            coef_variacao_revenda: {
               bsonType: "double",
               description: "Coeficiente de variação de revenda"
            },
            coef_variacao_distribuicao: {
               bsonType: "double",
               description: "Coeficiente de variação de distribuição"
            },
            numero_postos_pesquisados: {
               bsonType: "int",
               minimum: 1,
               description: "Número de postos pesquisados"
            },
            unidade_medida: {
               bsonType: "string",
               enum: ["R$/litro", "R$/m³"],
               description: "Unidade de medida do preço"
            },
            metadata: {
               bsonType: "object",
               properties: {
                  fonte: {
                     bsonType: "string",
                     description: "Fonte dos dados (ANP)"
                  },
                  created_at: {
                     bsonType: "date",
                     description: "Data de criação do registro"
                  },
                  updated_at: {
                     bsonType: "date",
                     description: "Data de atualização do registro"
                  }
               }
            }
         }
      }
   }
});

// Criar coleção de estatísticas regionais
db.createCollection("regionalStats", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["regiao", "ano", "produto"],
         properties: {
            regiao: {
               bsonType: "string",
               enum: ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"],
               description: "Região do Brasil - obrigatório"
            },
            ano: {
               bsonType: "int",
               minimum: 2004,
               maximum: 2025,
               description: "Ano de referência - obrigatório"
            },
            produto: {
               bsonType: "string",
               enum: ["GASOLINA COMUM", "ETANOL", "DIESEL", "DIESEL S10", "GNV"],
               description: "Tipo de combustível - obrigatório"
            },
            estatisticas: {
               bsonType: "object",
               properties: {
                  preco_medio_anual: {
                     bsonType: "double",
                     minimum: 0,
                     description: "Preço médio anual da região"
                  },
                  preco_minimo: {
                     bsonType: "double",
                     minimum: 0,
                     description: "Menor preço registrado no ano"
                  },
                  preco_maximo: {
                     bsonType: "double",
                     minimum: 0,
                     description: "Maior preço registrado no ano"
                  },
                  variacao_percentual: {
                     bsonType: "double",
                     description: "Variação percentual em relação ao ano anterior"
                  },
                  total_postos: {
                     bsonType: "int",
                     minimum: 0,
                     description: "Total de postos na região"
                  }
               }
            },
            estados_incluidos: {
               bsonType: "array",
               items: {
                  bsonType: "string"
               },
               description: "Lista de estados incluídos na estatística"
            }
         }
      }
   }
});

// Criar índices para otimização de consultas
db.fuelPrices.createIndex({ "estado": 1, "ano": 1, "produto": 1 });
db.fuelPrices.createIndex({ "regiao": 1, "data_coleta": 1 });
db.fuelPrices.createIndex({ "produto": 1, "preco_medio_revenda": 1 });
db.fuelPrices.createIndex({ "data_coleta": 1 });
db.fuelPrices.createIndex({ "estado": 1, "produto": 1, "ano": 1, "mes": 1 });

db.regionalStats.createIndex({ "regiao": 1, "ano": 1, "produto": 1 }, { unique: true });
db.regionalStats.createIndex({ "ano": 1 });

// Criar índices de texto para busca
db.fuelPrices.createIndex({ 
   "nome_estado": "text", 
   "produto": "text" 
});

print("✅ Banco de dados GasPricesBrazil configurado com sucesso!");
print("✅ Coleções criadas: fuelPrices, regionalStats");
print("✅ Validações de schema aplicadas");
print("✅ Índices criados para otimização de consultas");
"""

with open('03_mongodb_setup.js', 'w', encoding='utf-8') as f:
    f.write(mongodb_setup)

print("✅ Arquivo '03_mongodb_setup.js' criado com sucesso!")
print("\n📋 ESTRUTURA MONGODB:")
print("• fuelPrices: Preços de combustíveis por estado/data")
print("• regionalStats: Estatísticas agregadas por região")
print("• Validações de schema implementadas")
print("• Índices otimizados para consultas")