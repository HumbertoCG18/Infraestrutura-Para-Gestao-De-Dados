SELECT /*+ LEADING(dep_geo arr_geo) USE_HASH(f) */
    al.AIRLINE_NAME AS AIRLINE_NAME,
    ap.AIRPLANE_ID,
    apt.NAME AS AIRPLANE_TYPE,
    f.FLIGHT_ID
FROM 
    AIR_AIRPORTS_GEO dep_geo
    JOIN AIR_AIRPORTS dep ON dep.AIRPORT_ID = dep_geo.AIRPORT_ID
    JOIN AIR_AIRPORTS_GEO arr_geo ON arr_geo.COUNTRY = dep_geo.COUNTRY
    JOIN AIR_AIRPORTS arr ON arr.AIRPORT_ID = arr_geo.AIRPORT_ID
    JOIN AIR_FLIGHTS f ON f.FROM_AIRPORT_ID = dep.AIRPORT_ID 
                      AND f.TO_AIRPORT_ID = arr.AIRPORT_ID
    JOIN AIR_AIRLINES al ON f.AIRLINE_ID = al.AIRLINE_ID
    JOIN AIR_AIRPLANES ap ON f.AIRPLANE_ID = ap.AIRPLANE_ID
    JOIN AIR_AIRPLANE_TYPES apt ON ap.AIRPLANE_TYPE_ID = apt.AIRPLANE_TYPE_ID
WHERE 
    dep_geo.COUNTRY = 'BRAZIL'
    AND arr_geo.COUNTRY = 'BRAZIL';