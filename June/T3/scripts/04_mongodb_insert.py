# Criando o script de inserção de dados para MongoDB
mongodb_insert = """
// =====================================================
// SCRIPT INSERÇÃO - MONGODB
// Inserção de dados de preços de combustíveis
// =====================================================

// Conectar ao banco de dados
use GasPricesBrazil;

// Inserir dados de preços de combustíveis (2022-2024)
db.fuelPrices.insertMany([
    // São Paulo - Gasolina
    {
        estado: "SP",
        nome_estado: "São Paulo",
        regiao: "Sudeste",
        produto: "GASOLINA COMUM",
        data_coleta: new Date("2024-01-15"),
        ano: 2024,
        mes: 1,
        preco_medio_revenda: 5.89,
        preco_medio_distribuicao: 4.12,
        desvio_padrao_revenda: 0.287,
        desvio_padrao_distribuicao: 0.145,
        coef_variacao_revenda: 0.0487,
        coef_variacao_distribuicao: 0.0352,
        numero_postos_pesquisados: 1245,
        unidade_medida: "R$/litro",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    },
    {
        estado: "SP",
        nome_estado: "São Paulo",
        regiao: "Sudeste",
        produto: "ETANOL",
        data_coleta: new Date("2024-01-15"),
        ano: 2024,
        mes: 1,
        preco_medio_revenda: 3.89,
        preco_medio_distribuicao: 2.67,
        desvio_padrao_revenda: 0.234,
        desvio_padrao_distribuicao: 0.123,
        coef_variacao_revenda: 0.0601,
        coef_variacao_distribuicao: 0.0461,
        numero_postos_pesquisados: 987,
        unidade_medida: "R$/litro",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    },
    // Rio de Janeiro - Gasolina
    {
        estado: "RJ",
        nome_estado: "Rio de Janeiro",
        regiao: "Sudeste",
        produto: "GASOLINA COMUM",
        data_coleta: new Date("2024-01-15"),
        ano: 2024,
        mes: 1,
        preco_medio_revenda: 6.12,
        preco_medio_distribuicao: 4.23,
        desvio_padrao_revenda: 0.298,
        desvio_padrao_distribuicao: 0.156,
        coef_variacao_revenda: 0.0487,
        coef_variacao_distribuicao: 0.0369,
        numero_postos_pesquisados: 678,
        unidade_medida: "R$/litro",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    },
    // Minas Gerais - Gasolina
    {
        estado: "MG",
        nome_estado: "Minas Gerais",
        regiao: "Sudeste",
        produto: "GASOLINA COMUM",
        data_coleta: new Date("2024-01-15"),
        ano: 2024,
        mes: 1,
        preco_medio_revenda: 5.78,
        preco_medio_distribuicao: 4.05,
        desvio_padrao_revenda: 0.312,
        desvio_padrao_distribuicao: 0.167,
        coef_variacao_revenda: 0.0540,
        coef_variacao_distribuicao: 0.0412,
        numero_postos_pesquisados: 892,
        unidade_medida: "R$/litro",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    },
    // Bahia - Gasolina
    {
        estado: "BA",
        nome_estado: "Bahia",
        regiao: "Nordeste",
        produto: "GASOLINA COMUM",
        data_coleta: new Date("2024-01-15"),
        ano: 2024,
        mes: 1,
        preco_medio_revenda: 5.95,
        preco_medio_distribuicao: 4.18,
        desvio_padrao_revenda: 0.345,
        desvio_padrao_distribuicao: 0.189,
        coef_variacao_revenda: 0.0580,
        coef_variacao_distribuicao: 0.0452,
        numero_postos_pesquisados: 567,
        unidade_medida: "R$/litro",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    },
    // Paraná - Gasolina
    {
        estado: "PR",
        nome_estado: "Paraná",
        regiao: "Sul",
        produto: "GASOLINA COMUM",
        data_coleta: new Date("2024-01-15"),
        ano: 2024,
        mes: 1,
        preco_medio_revenda: 5.67,
        preco_medio_distribuicao: 4.01,
        desvio_padrao_revenda: 0.278,
        desvio_padrao_distribuicao: 0.134,
        coef_variacao_revenda: 0.0490,
        coef_variacao_distribuicao: 0.0334,
        numero_postos_pesquisados: 445,
        unidade_medida: "R$/litro",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    },
    // Dados históricos - 2023
    {
        estado: "SP",
        nome_estado: "São Paulo",
        regiao: "Sudeste",
        produto: "GASOLINA COMUM",
        data_coleta: new Date("2023-12-15"),
        ano: 2023,
        mes: 12,
        preco_medio_revenda: 5.45,
        preco_medio_distribuicao: 3.89,
        desvio_padrao_revenda: 0.267,
        desvio_padrao_distribuicao: 0.132,
        coef_variacao_revenda: 0.0490,
        coef_variacao_distribuicao: 0.0339,
        numero_postos_pesquisados: 1198,
        unidade_medida: "R$/litro",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    },
    // Diesel
    {
        estado: "SP",
        nome_estado: "São Paulo",
        regiao: "Sudeste",
        produto: "DIESEL",
        data_coleta: new Date("2024-01-15"),
        ano: 2024,
        mes: 1,
        preco_medio_revenda: 4.98,
        preco_medio_distribuicao: 3.67,
        desvio_padrao_revenda: 0.198,
        desvio_padrao_distribuicao: 0.098,
        coef_variacao_revenda: 0.0398,
        coef_variacao_distribuicao: 0.0267,
        numero_postos_pesquisados: 987,
        unidade_medida: "R$/litro",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    },
    // GNV
    {
        estado: "RJ",
        nome_estado: "Rio de Janeiro",
        regiao: "Sudeste",
        produto: "GNV",
        data_coleta: new Date("2024-01-15"),
        ano: 2024,
        mes: 1,
        preco_medio_revenda: 4.12,
        preco_medio_distribuicao: 2.98,
        desvio_padrao_revenda: 0.156,
        desvio_padrao_distribuicao: 0.089,
        coef_variacao_revenda: 0.0379,
        coef_variacao_distribuicao: 0.0299,
        numero_postos_pesquisados: 234,
        unidade_medida: "R$/m³",
        metadata: {
            fonte: "ANP - Agência Nacional do Petróleo",
            created_at: new Date(),
            updated_at: new Date()
        }
    }
]);

// Inserir estatísticas regionais
db.regionalStats.insertMany([
    {
        regiao: "Sudeste",
        ano: 2024,
        produto: "GASOLINA COMUM",
        estatisticas: {
            preco_medio_anual: 5.93,
            preco_minimo: 5.67,
            preco_maximo: 6.12,
            variacao_percentual: 8.07,
            total_postos: 2815
        },
        estados_incluidos: ["SP", "RJ", "MG", "ES"]
    },
    {
        regiao: "Sul",
        ano: 2024,
        produto: "GASOLINA COMUM",
        estatisticas: {
            preco_medio_anual: 5.71,
            preco_minimo: 5.45,
            preco_maximo: 5.89,
            variacao_percentual: 7.23,
            total_postos: 1234
        },
        estados_incluidos: ["RS", "SC", "PR"]
    },
    {
        regiao: "Nordeste",
        ano: 2024,
        produto: "GASOLINA COMUM",
        estatisticas: {
            preco_medio_anual: 6.08,
            preco_minimo: 5.78,
            preco_maximo: 6.34,
            variacao_percentual: 9.15,
            total_postos: 1789
        },
        estados_incluidos: ["BA", "PE", "CE", "MA", "PB", "RN", "AL", "SE", "PI"]
    },
    {
        regiao: "Centro-Oeste",
        ano: 2024,
        produto: "GASOLINA COMUM",
        estatisticas: {
            preco_medio_anual: 5.84,
            preco_minimo: 5.56,
            preco_maximo: 6.12,
            variacao_percentual: 7.89,
            total_postos: 678
        },
        estados_incluidos: ["GO", "MT", "MS", "DF"]
    },
    {
        regiao: "Norte",
        ano: 2024,
        produto: "GASOLINA COMUM",
        estatisticas: {
            preco_medio_anual: 6.15,
            preco_minimo: 5.89,
            preco_maximo: 6.45,
            variacao_percentual: 8.67,
            total_postos: 456
        },
        estados_incluidos: ["AM", "PA", "AC", "RO", "RR", "AP", "TO"]
    }
]);

// Verificações e estatísticas
print("✅ Dados inseridos com sucesso!");
print("📊 RESUMO DOS DADOS:");
print("Registros de preços: " + db.fuelPrices.countDocuments());
print("Estatísticas regionais: " + db.regionalStats.countDocuments());

// Consulta de teste - Preços por região
print("\\n🔍 CONSULTA TESTE - Preços médios por região (Gasolina 2024):");
db.fuelPrices.aggregate([
    {
        $match: {
            produto: "GASOLINA COMUM",
            ano: 2024
        }
    },
    {
        $group: {
            _id: "$regiao",
            preco_medio: { $avg: "$preco_medio_revenda" },
            total_postos: { $sum: "$numero_postos_pesquisados" }
        }
    },
    {
        $sort: { preco_medio: -1 }
    }
]).forEach(printjson);

// Consulta de teste - Estados com maior variação de preços
print("\\n🔍 CONSULTA TESTE - Estados com maior variação (Gasolina):");
db.fuelPrices.find(
    { produto: "GASOLINA COMUM", ano: 2024 },
    { 
        estado: 1, 
        nome_estado: 1, 
        preco_medio_revenda: 1, 
        coef_variacao_revenda: 1,
        _id: 0 
    }
).sort({ coef_variacao_revenda: -1 }).limit(5).forEach(printjson);
"""

with open('04_mongodb_insert.js', 'w', encoding='utf-8') as f:
    f.write(mongodb_insert)

print("✅ Arquivo '04_mongodb_insert.js' criado com sucesso!")
print("\n📊 DADOS MONGODB:")
print("• 9 registros de preços de combustíveis")
print("• 5 estatísticas regionais agregadas")
print("• Dados de 2023-2024 para análise temporal")
print("• Consultas de teste incluídas")