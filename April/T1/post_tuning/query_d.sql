SELECT /*+ INDEX(b IDX_BOOKINGS_FLIGHT) */
    f.FLIGHTNO,
    dep.NAME AS DEPARTURE_AIRPORT,
    arr.NAME AS ARRIVAL_AIRPORT,
    p.FIRSTNAME || ' ' || p.LASTNAME AS PASSENGER_NAME,
    b.SEAT
FROM 
    AIR_FLIGHTS f
    JOIN AIR_BOOKINGS b ON f.FLIGHT_ID = b.FLIGHT_ID
    JOIN AIR_PASSENGERS p ON b.PASSENGER_ID = p.PASSENGER_ID
    JOIN AIR_AIRPORTS dep ON f.FROM_AIRPORT_ID = dep.AIRPORT_ID
    JOIN AIR_AIRPORTS arr ON f.TO_AIRPORT_ID = arr.AIRPORT_ID
ORDER BY 
    f.FLIGHTNO, p.LASTNAME, p.FIRSTNAME;