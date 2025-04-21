-- Query E: Pós-tuning - simulação de acesso hash em cluster
SELECT /*+ 
       ORDERED                  
       LEADING(f)               
       USE_HASH(b)              -- Simula acesso hash entre tabelas "clusterizadas"
       USE_HASH(p al dep)       -- Otimiza junções com tabelas "externas" 
     */
    f.FLIGHTNO,
    TO_CHAR(f.DEPARTURE, 'YYYY-MM-DD HH24:MI') AS DEPARTURE_TIME,
    b.SEAT,
    p.FIRSTNAME || ' ' || p.LASTNAME AS PASSENGER_NAME,
    al.AIRLINE_NAME,
    dep.NAME AS DEPARTURE_AIRPORT
FROM 
    AIR_FLIGHTS f                                   -- "Primeira tabela no cluster"
    JOIN AIR_BOOKINGS b ON f.FLIGHT_ID = b.FLIGHT_ID -- "Segunda tabela no cluster"
    JOIN AIR_PASSENGERS p ON b.PASSENGER_ID = p.PASSENGER_ID -- Tabela externa 1
    JOIN AIR_AIRLINES al ON f.AIRLINE_ID = al.AIRLINE_ID     -- Tabela externa 2
    JOIN AIR_AIRPORTS dep ON f.FROM_AIRPORT_ID = dep.AIRPORT_ID -- Tabela externa 3
WHERE 
    f.DEPARTURE > SYSDATE - 365  -- Filtra para voos do último ano
    AND ROWNUM <= 50;